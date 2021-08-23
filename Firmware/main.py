# imports
import os
import threading       
import subprocess                                                                                               
import signal
import sys 
import subprocess
import time
import board
import digitalio
import neopixel
from requests import get
import json
from gatt_server import BleApplication, WeatherStationAdvertisement, WeatherService, RgbColorService, SystemService
from repeated_timer import RepeatedTimer
from UIHandler import *
from btnHandler import *
import qrcode

### params
WEATHER_SERVICE_INDEX = 0
RGB_COLOR_SERVICE_INDEX = 1
SYSTEM_SERVICE_INDEX = 2

DELAY_WEATHER_REQUEST = 1.0 # seconds
DELAY_DETECT_MANUAL_SHUTDOWN = 1.0

timer_update = None
timer_system = None

base = 'https://api.openweathermap.org/data/2.5/weather'
city = 'id=%s'
units = 'units=metric'
appid = 'appid=c6206d175419aecde9ee5a6c233a3830'
url = '%s?%s&%s&%s' % (base, city, units, appid)

# shutdown_pin = board.D4
# shutdown_button = digitalio.DigitalInOut(shutdown_pin)
# shutdown_button.direction = digitalio.Direction.INPUT
# shutdown_button.pull = digitalio.Pull.UP
# system_stopped = False

pixels_pin = board.D18
pixels_count = 3
pixels_order = neopixel.GRB
pixels = neopixel.NeoPixel(pixels_pin,
                pixels_count,
                brightness = 1.0,
                auto_write = False,
                pixel_order = pixels_order)

def getControllerID():
    #cmd="(echo -e 'show\nquit' | sudo bluetoothctl | grep Controller)"
    cmd="./getControllerID.sh"
    result = subprocess.run(cmd,shell=True, stdout=subprocess.PIPE)
    g=result.stdout
    m=g.decode('utf-8')
    k=m.split(' ')
    print(k)
    ControllerAddress=k[2]
    print(ControllerAddress)
    return ControllerAddress
    #time.sleep(0.5)
    # mp=os.system(cmd)
    # print(mp)
    #print(open('tmp', 'r').read())
    
    
    
### weather requests
def getCurrentWeather():
    if system_stopped:
        return

    try:
        city_id = ble_app.services[WEATHER_SERVICE_INDEX].get_city_id()

        data = get(url % (city_id), timeout = 5).json()
        temperature = int(data['main']['temp'])
        weather_id = data['weather'][0]['id']
        print('Request response: %s°C (weather: %s)' % (temperature, weather_id), flush=True)

        return [temperature, weather_id]
    except Exception as e:
        print('Request connection error: %s' % e, flush=True)
        pass

### neopixels
def selectColorByDegrees(degrees):
    if degrees <= 0:
        return (255, 255, 255) # white
    elif degrees > 0 and degrees <= 10:
        return (0, 153, 255) # blue
    elif degrees > 10 and degrees <= 15:
        return (0, 204, 0) # green
    elif degrees > 15 and degrees <= 20:
        return (255, 255, 0) # yellow
    elif degrees > 20 and degrees <= 30:
        return (204, 102, 0) # orange
    else:
        return (204, 0, 0) # red

def updateNeopixelColor(degrees):
    if system_stopped:
        return

    color = selectColorByDegrees(degrees)
    print('Color selected: {}'.format(color), flush=True)
    pixels.fill(color)
    pixels.show()

def setNeopixelColor(colors):
    rgb = [int(x) for x in colors.split(",")]
    print('Colors rgb: ', rgb, flush=True)
    pixels.fill((rgb[0], rgb[1], rgb[2]))
    pixels.show()

def stopNeopixels():
    pixels.fill((0,0,0))
    pixels.show()

### system
def stop():
    if not timer_update is None and timer_update.isRunning():
        timer_update.stop()
    stopNeopixels()
    if not timer_system is None and timer_system.isRunning():
        timer_system.stop()

# def shutdown():
#     stop()
#     print('Shutdown system.')
#     os.system("sudo shutdown -h now")

### commands
tempV=0
#degreesV=None
def updateWeather():
    global tempV,degreesV
    #print('---', flush=True)
    #print('Update weather', flush=True)
    #data = getCurrentWeather()
    data = [12,11]
    if not data:
        print('Error: weather data is None', flush=True)
        return

    degrees = data[0]
    weather_id = data[1]
    
    ble_app.services[WEATHER_SERVICE_INDEX].set_degrees(degrees)
    
    ble_app.services[WEATHER_SERVICE_INDEX].set_weather_id(weather_id)
    ###test statements
    ble_app.services[WEATHER_SERVICE_INDEX].set_drive_len(str(tempV+1))
    ble_app.services[WEATHER_SERVICE_INDEX].set_drive_time(str(tempV+2))
    ble_app.services[WEATHER_SERVICE_INDEX].set_avg_force(str(tempV+3))
    ble_app.services[WEATHER_SERVICE_INDEX].set_peak_force(str(tempV+4))
    ble_app.services[WEATHER_SERVICE_INDEX].set_drag_factor(str(tempV+5))
    ble_app.services[WEATHER_SERVICE_INDEX].set_ypr(str(tempV+6))
    ble_app.services[WEATHER_SERVICE_INDEX].set_lattlng(str(tempV+7))
    tempV=tempV+1
    #time.sleep(0.4)
    #updateNeopixelColor(degrees)

def fetchIpAddress():
    command = 'hostname -I'
    proc = subprocess.Popen(command, stdout = subprocess.PIPE, shell = True)
    proc = proc.communicate()[0]
    ip_address = str(proc).split(" ")[0].split('\'')[1]

    print ("GATT application ip address %s" % ip_address, flush=True)
    ble_app.services[SYSTEM_SERVICE_INDEX].set_ip_address(ip_address)

# def shouldShutdown():
#     if not shutdown_button.value:
#         print('Should shutdown system..', flush=True)
#         shutdown()

# execution
ble_app = BleApplication()
ble_app.add_service(WeatherService(WEATHER_SERVICE_INDEX))
ble_app.add_service(RgbColorService(RGB_COLOR_SERVICE_INDEX))
ble_app.add_service(SystemService(SYSTEM_SERVICE_INDEX))
ble_app.register()

ble_adv = WeatherStationAdvertisement(0)
ble_adv.register()

timer_update = RepeatedTimer(DELAY_WEATHER_REQUEST, updateWeather)
#timer_system = RepeatedTimer(DELAY_DETECT_MANUAL_SHUTDOWN, shouldShutdown)

try:
    print('GATT application running')
    fetchIpAddress()
    
    myThread = threading.Thread(target=ble_app.run)
    myThread.daemon = True
    myThread.start()
    #ble_app.run()
    print("Configuring UI")
    configUI()
    contID=getControllerID()
    img = qrcode.make(contID)
    type(img) 
    img.save(f'qr.png')
    setQRCode(contID)
    print('running UI')
    while 1:
        totalTimeElapsed="Total TIME Elapsed"
        strokesPM=ble_app.services[WEATHER_SERVICE_INDEX].get_degrees()
        driveTime=ble_app.services[WEATHER_SERVICE_INDEX].get_drive_time()
        avgForce=ble_app.services[WEATHER_SERVICE_INDEX].get_avg_force()
        peakForce=ble_app.services[WEATHER_SERVICE_INDEX].get_peaks_force()
        dragFactor=ble_app.services[WEATHER_SERVICE_INDEX].get_drag_factor()
        ypr=ble_app.services[WEATHER_SERVICE_INDEX].get_ypr()
        latlng=ble_app.services[WEATHER_SERVICE_INDEX].get_latlng()

        mainUI(totalTimeElapsed,strokesPM,driveTime,avgForce,peakForce,dragFactor,ypr,latlng,widgetsPos[getCurPos()])
        
        
        
except KeyboardInterrupt:
    ble_app.quit()
    pass

stop()

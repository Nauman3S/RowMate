
import time
from tkinter.constants import NO
import board
import adafruit_bno055
import serial

# i2c = board.I2C()
# sensor = adafruit_bno055.BNO055_I2C(i2c)

# If you are going to use UART uncomment these lines
#uart = busio.UART(board.TX, board.RX)
uart=None
sensor=None
try:
    uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
    sensor = adafruit_bno055.BNO055_UART(uart)
except Exception as e:
    print("Please conencct the IMU (BNO085) Properly and re-run the program for the chagnes to take effect.")

last_val = 0xFFFF


def temperature():
    global last_val  # pylint: disable=global-statement
    result = sensor.temperature
    if abs(result - last_val) == 128:
        result = sensor.temperature
        if abs(result - last_val) == 128:
            return 0b00111111 & result
    last_val = result
    return result
def getYPR():
    global sensor
    v=""
    try:
        v=sensor.euler
    except Exception as e:
        v="Y=0.0,P=0.0,R=0.0"
    return v

# while True:
#     print("Temperature: {} degrees C".format(sensor.temperature))
#     """
#     print(
#         "Temperature: {} degrees C".format(temperature())
#     )  # Uncomment if using a Raspberry Pi
#     """
#     print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
#     print("Magnetometer (microteslas): {}".format(sensor.magnetic))
#     print("Gyroscope (rad/sec): {}".format(sensor.gyro))
#     print("Euler angle: {}".format(sensor.euler))
#     print("Quaternion: {}".format(sensor.quaternion))
#     print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
#     print("Gravity (m/s^2): {}".format(sensor.gravity))
#     print()

#     time.sleep(1)
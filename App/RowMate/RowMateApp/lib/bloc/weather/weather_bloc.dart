import 'dart:async';
import 'dart:convert';
import 'dart:ffi';

import 'package:bloc/bloc.dart';
import 'package:flutter_blue/flutter_blue.dart';

import 'package:rowmate/bloc/weather/weather_event.dart';
import 'package:rowmate/bloc/weather/weather_state.dart';

import 'package:rowmate/data/cities_data.dart';
import 'package:rowmate/models/averageforce.dart';
import 'package:rowmate/models/dragfactor.dart';
import 'package:rowmate/models/drivelen.dart';
import 'package:rowmate/models/drivetime.dart';
import 'package:rowmate/models/lattlng.dart';
import 'package:rowmate/models/peakforce.dart';

import 'package:rowmate/models/weather.dart';
import 'package:rowmate/models/city.dart';
import 'package:rowmate/models/ypr.dart';

class WeatherBloc extends Bloc<WeatherEvent, WeatherState> {
  final Guid _WEATHER_CHARACTERISTIC_GUID =
      Guid('00000001-8cb1-44ce-9a66-001dca0941a6');
  final Guid _RESUME_WEATHER_CHARACTERISTIC_GUID =
      Guid('00000002-8cb1-44ce-9a66-001dca0941a6');
  final BluetoothService _bleService;
  StreamSubscription<List<int>> _streamBleWeatherCharacteristic;

  WeatherBloc(BluetoothService bleService)
      : assert(bleService != null),
        _bleService = bleService,
        super(WeatherInitial());

  @override
  Stream<WeatherState> mapEventToState(WeatherEvent event) async* {
    if (event is ListenToUpdates) {
      yield* _mapListenToUpdates();
    }

    if (event is RestartUpdates) {
      restartUpdates();
    }

    if (event is WeatherReceived) {
      yield* _mapWeatherReceived(event);
    }
  }

  Stream<WeatherState> _mapListenToUpdates() async* {
    yield WeatherInitial();

    final characteristic = _bleService.characteristics
        .firstWhere((c) => c.uuid == _WEATHER_CHARACTERISTIC_GUID);
    await characteristic.setNotifyValue(true);

    _streamBleWeatherCharacteristic = characteristic.value.listen((value) {
      print('W: value received : $value');
      if (value == null || value.isEmpty) {
        print('W: value is empty');
        return;
      }

      var data = utf8.decode(value);
      print('W: Data decoded : $data');

      var dataReceived = data.split(',');
      print('W: Data received: $dataReceived');

      var dataTemp = dataReceived[0];
      var temperature = dataTemp.substring(2);
      var dataWeather = dataReceived[1];
      var weatherId = dataWeather.substring(2);

      var dLen = dataReceived[3];
      var dFLen = dLen.substring(2);
      var drivelen = Drivelen((dFLen));

      var dTime = dataReceived[4];
      var dFTime = dTime.substring(2);
      var drivetimev = Drivetime((dFTime));

      var avgForce = dataReceived[5];
      var avgFFroce = avgForce.substring(2);
      var averageForce = Averageforce((avgFFroce));

      var peakForce = dataReceived[6];
      var peakFForce = peakForce.substring(2);
      var peakForcev = Peakforce((peakFForce));

      var dragFactor = dataReceived[7];
      var dragFFactor = dragFactor.substring(2);
      var dragFactroV = Dragfactor((dragFFactor));

      var ypR = dataReceived[8];
      var yprF = ypR.substring(2);
      var yprV = Ypr((yprF));

      var lattLng = dataReceived[8];
      var lattFLng = lattLng.substring(2);
      var lattLngV = Lattlng((lattFLng));

      var weather = Weather(temperature, int.parse(weatherId), dFLen, dFTime,
          avgFFroce, peakFForce, dragFFactor, yprF, lattFLng);

      var dataCity = dataReceived[2];
      var cityId = dataCity.substring(2);
      var city = City(int.parse("123"));

      // var citiesData = CitiesData();
      // citiesData.cities.forEach((element) {
      //   if (element.containsValue(city.id)) {
      //     city.name = element['name'];
      //     city.icon = element['icon'];
      //   }
      // });

      add(WeatherReceived(weather, city, drivelen, drivetimev, averageForce,
          peakForcev, dragFactroV, yprV, lattLngV));
    });
  }

  void restartUpdates() async {
    final characteristic = _bleService.characteristics
        .firstWhere((c) => c.uuid == _RESUME_WEATHER_CHARACTERISTIC_GUID);
    await characteristic.write([]);
  }

  Stream<WeatherState> _mapWeatherReceived(WeatherReceived event) async* {
    yield WeatherUpdated(
        event.weather,
        event.city,
        event.drivelen,
        event.drivetime,
        event.averageforce,
        event.peakforce,
        event.dragfactor,
        event.ypr,
        event.lattlng);
  }

  @override
  Future<void> close() {
    _streamBleWeatherCharacteristic?.cancel();
    return super.close();
  }
}

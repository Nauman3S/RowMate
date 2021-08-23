import 'package:equatable/equatable.dart';

import 'package:rowmate/models/city.dart';

import 'package:rowmate/models/weather.dart';
import 'package:rowmate/models/dragfactor.dart';
import 'package:rowmate/models/drivelen.dart';
import 'package:rowmate/models/drivetime.dart';
import 'package:rowmate/models/lattlng.dart';
import 'package:rowmate/models/peakforce.dart';
import 'package:rowmate/models/averageforce.dart';
import 'package:rowmate/models/ypr.dart';

abstract class WeatherState extends Equatable {
  @override
  List<Object> get props => [];
}

class WeatherInitial extends WeatherState {}

class WeatherUpdated extends WeatherState {
  final Weather weather;
  final City city;
  final Drivelen drivelen;
  final Drivetime drivetime;
  final Averageforce averageforce;
  final Peakforce peakforce;
  final Dragfactor dragfactor;
  final Ypr ypr;
  final Lattlng lattlng;

  WeatherUpdated(
      this.weather,
      this.city,
      this.drivelen,
      this.drivetime,
      this.averageforce,
      this.peakforce,
      this.dragfactor,
      this.ypr,
      this.lattlng);

  @override
  List<Object> get props => [
        this.weather,
        this.city,
        this.drivelen,
        this.drivetime,
        this.averageforce,
        this.peakforce,
        this.dragfactor,
        this.ypr,
        this.lattlng
      ];
}

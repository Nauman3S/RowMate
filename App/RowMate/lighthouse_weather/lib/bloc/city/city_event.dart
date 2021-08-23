import 'package:equatable/equatable.dart';

abstract class CityEvent extends Equatable {
  @override
  List<Object> get props => [];
}

class ChangeCity extends CityEvent {
  final String cityId;

  ChangeCity(this.cityId);

  @override
  List<Object> get props => [this.cityId];
}

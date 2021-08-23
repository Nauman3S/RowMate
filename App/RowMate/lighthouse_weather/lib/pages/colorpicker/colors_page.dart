import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_blue/flutter_blue.dart' show Guid;
import 'package:flutter_colorpicker/flutter_colorpicker.dart';
import 'package:rowmate/pages/commons/appname_widget.dart';
import 'package:material_design_icons_flutter/material_design_icons_flutter.dart';

import 'package:rowmate/bloc/bluetooth/bluetooth.dart';
import 'package:rowmate/bloc/colors/colors.dart';
import 'package:rowmate/bloc/weather/weather.dart';

import 'package:rowmate/pages/commons/background_widget.dart';
import 'package:rowmate/pages/commons/button_widget.dart';
import 'package:syncfusion_flutter_charts/charts.dart';
import 'package:syncfusion_flutter_charts/sparkcharts.dart';

class ColorsPage extends StatefulWidget {
  @override
  ColorsPageState createState() {
    return ColorsPageState();
  }
}

class ColorsPageState extends State<ColorsPage> {
  //final Guid _RGB_COLOR_SERVICE_GUID = Guid('00000000-8194-4451-aaf5-7874c7c16a27');
  final Guid _WEATHER_SERVICE_GUID =
      Guid('00000000-8cb1-44ce-9a66-001dca0941a6');
  Color currentColor = Color(0xff375670);

  @override
  Widget build(BuildContext context) {
    var bleBloc = BlocProvider.of<BleBloc>(context);
    bleBloc.add(Listening());

    return BlocProvider(
        create: (_) => WeatherBloc(
            bleBloc.getServiceByGuid(_WEATHER_SERVICE_GUID))
          ..add(
              ListenToUpdates()), //ColorsBloc(bleBloc.getServiceByGuid(_RGB_COLOR_SERVICE_GUID)),
        child:
            BlocBuilder<WeatherBloc, WeatherState>(builder: (context, state) {
          //BlocBuilder<ColorsBloc, ColorsState>(builder: (context, state) {
          return Scaffold(
              body: Stack(
            children: [
              BackgroundImage('bg_colors'),
              _showContent(state),
              //_setAction(context)
            ],
          ));
        }));
  }

  Widget _showContent(WeatherState state) {
    final double statusBarHeight = MediaQuery.of(context).padding.top;

    if (state is WeatherUpdated) {
      return Container(
          alignment: Alignment.topCenter,
          padding: EdgeInsets.only(
              left: 10.0, right: 10.0, top: statusBarHeight + 100.0),
          child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: <Widget>[
                Column(
                  children: [
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        Card(
                          color: Colors.transparent,
                          elevation: 0.4,
                          child: Text(
                            "Drive Time: ",
                            style: TextStyle(
                                fontWeight: FontWeight.w400,
                                fontSize: 30.0,
                                color: Colors.white),
                          ),
                        ),
                        Text(
                          state.weather.drivetime,
                          style: TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 30.0,
                              color: Colors.white),
                        )
                      ],
                    ),
                    SizedBox(height: 15),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        Text(
                          "Strokes/m: ",
                          style: TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 30.0,
                              color: Colors.white),
                        ),
                        Text(
                          state.weather.strokespm,
                          style: TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 30.0,
                              color: Colors.white),
                        )
                      ],
                    ),
                    SizedBox(height: 15),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        Text(
                          "Drive Length: ",
                          style: TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 30.0,
                              color: Colors.white),
                        ),
                        Text(
                          state.weather.drivelen,
                          style: TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 30.0,
                              color: Colors.white),
                        )
                      ],
                    ),
                    SizedBox(height: 15),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        Text(
                          "Avg Force: ",
                          style: TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 30.0,
                              color: Colors.white),
                        ),
                        Text(
                          state.weather.averageforce,
                          style: TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 30.0,
                              color: Colors.white),
                        )
                      ],
                    ),
                    SizedBox(height: 15),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        Text(
                          "Peak Force: ",
                          style: TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 30.0,
                              color: Colors.white),
                        ),
                        Text(
                          state.weather.peakforce,
                          style: TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 30.0,
                              color: Colors.white),
                        )
                      ],
                    ),
                    SizedBox(height: 15),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        Text(
                          "Drag Factor: ",
                          style: TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 30.0,
                              color: Colors.white),
                        ),
                        Text(
                          state.weather.dragfactor,
                          style: TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 30.0,
                              color: Colors.white),
                        )
                      ],
                    ),
                    SizedBox(height: 15),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        Text(
                          "YPR: ",
                          style: TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 30.0,
                              color: Colors.white),
                        ),
                        Text(
                          state.weather.ypr,
                          style: TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 30.0,
                              color: Colors.white),
                        )
                      ],
                    ),
                    SizedBox(height: 15),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        Text(
                          "LattLng: ",
                          style: TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 30.0,
                              color: Colors.white),
                        ),
                        Text(
                          state.weather.lattlng,
                          style: TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 30.0,
                              color: Colors.white),
                        )
                      ],
                    ),
                  ],
                ),
                // Text(state.weather.temperature,
                //     style: TextStyle(
                //         fontWeight: FontWeight.w200,
                //         fontSize: 50.0,
                //         color: Colors.white)),
                // Flexible(
                //     child: Container(
                //   padding: EdgeInsets.only(top: 10.0, left: 10),
                //   child: Column(
                //     mainAxisAlignment: MainAxisAlignment.start,
                //     crossAxisAlignment: CrossAxisAlignment.start,
                //     mainAxisSize: MainAxisSize.min,
                //     children: [
                //       Text('°C',
                //           style:
                //               TextStyle(fontSize: 20.0, color: Colors.white)),
                //       Text(state.city.name,
                //           overflow: TextOverflow.ellipsis,
                //           style: TextStyle(
                //               fontWeight: FontWeight.w500,
                //               fontSize: 24.0,
                //               color: Colors.white)),
                //       Container(
                //           padding: const EdgeInsets.only(top: 5.0),
                //           child: Icon(
                //             state.weather.icon,
                //             size: 42.0,
                //             color: Colors.white,
                //             semanticLabel: 'Weather',
                //           )),
                //     ],
                //   ),
                // )),
              ]));
    }

    return Container(alignment: Alignment.topCenter, child: AppNameWidget());
  }

  Widget _setAction(BuildContext context) {
    var colorsBloc = BlocProvider.of<ColorsBloc>(context);

    return Container(
        alignment: Alignment.bottomCenter,
        padding: EdgeInsets.only(left: 40.0, right: 40.0, bottom: 20.0),
        child: Card(
          color: Colors.transparent,
          elevation: 0.5,
          child: Container(
              padding: EdgeInsets.only(top: 20.0),
              child: ButtonWidget(
                  label: 'Update the color',
                  iconData: MdiIcons.palette,
                  action: () => colorsBloc.add(ChangeColors([
                        currentColor.red,
                        currentColor.green,
                        currentColor.blue
                      ])))),
        ));
  }
}

import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_blue/flutter_blue.dart' show Guid;

import 'package:rowmate/bloc/bluetooth/bluetooth.dart';
import 'package:rowmate/bloc/city/city.dart';

import 'package:rowmate/data/cities_data.dart';

import 'package:rowmate/models/city.dart';

import 'package:rowmate/pages/commons/background_widget.dart';
import 'package:rowmate/pages/cities/city_item_widget.dart';

class CitiesPage extends StatefulWidget {
  @override
  CitiesPageState createState() {
    return CitiesPageState();
  }
}

class CitiesPageState extends State<CitiesPage> {
  final Guid _WEATHER_SERVICE_GUID =
      Guid('00000000-8cb1-44ce-9a66-001dca0941a6');
  TextEditingController _outputController;
  @override
  initState() {
    super.initState();
    this._outputController = new TextEditingController();
  }

  void _showDialog() {
    // flutter defined function
    showDialog(
      context: context,
      builder: (BuildContext context) {
        // return object of type Dialog
        return AlertDialog(
          title: new Text("Piece Settings"),
          content: new Text("Setting sent"),
          actions: <Widget>[
            // usually buttons at the bottom of the dialog
            new ElevatedButton(
              child: new Text("Ok"),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }

  Widget build(BuildContext context) {
    var bleBloc = BlocProvider.of<BleBloc>(context);

    return BlocProvider(
        create: (_) =>
            CityBloc(bleBloc.getServiceByGuid(_WEATHER_SERVICE_GUID)),
        child: BlocBuilder<CityBloc, CityState>(builder: (context, state) {
          return Scaffold(
              body: Stack(
            children: [
              BackgroundImage('bg_cities'),
              Center(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: <Widget>[
                    SizedBox(height: 90),
                    Text(
                      "Set Piece",
                      style: TextStyle(
                          fontWeight: FontWeight.w200,
                          fontSize: 20.0,
                          color: Colors.white),
                    ),
                    SizedBox(height: 50),
                    TextField(
                      controller: this._outputController,
                      autofocus: true,
                      textAlign: TextAlign.center,
                      maxLines: 1,
                      style: TextStyle(
                        color: Colors.orange,
                        fontWeight: FontWeight.w500,
                        fontSize: 25.0,
                      ),
                      decoration: InputDecoration(
                          icon: Icon(Icons.add_box_rounded),
                          border: OutlineInputBorder(),
                          fillColor: Colors.white,
                          filled: true,
                          focusedBorder: OutlineInputBorder(
                            borderSide: const BorderSide(
                                color: Colors.white, width: 2.0),
                            borderRadius: BorderRadius.circular(25.0),
                          ),
                          hintText: 'Enter a piece term'),
                    ),
                    SizedBox(height: 50),
                    ElevatedButton(
                        onPressed: () {
                          print(this._outputController.text);
                          _pickCity(context, this._outputController.text);
                          _showDialog();
                        },
                        child: new Text('Send')),
                  ],
                ),
              ),
            ],
          ));
        }));
  }

  void _pickCity(BuildContext context, String n) {
    var cityBloc = BlocProvider.of<CityBloc>(context);
    cityBloc.add(ChangeCity(n));
  }

  Widget _showContent(CityState state) {
    if (state is CityUpdatingFailed) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
        content: const Text('An error occurred, the city is not updated'),
        duration: const Duration(seconds: 3),
      ));
    }

    if (state is CityUpdated) {
      WidgetsBinding.instance.addPostFrameCallback((_) {
        Navigator.pop(context);
      });
    }

    return GridView.count(
      crossAxisCount: 3,
      children: _getCityItems(),
    );
  }

  List<Widget> _getCityItems() {
    var list = List<Widget>();
    var citiesData = CitiesData();
    citiesData.cities.forEach((element) {
      var city =
          City(element['id'], name: element['name'], icon: element['icon']);
      var item = CityItem(city);
      list.add(item);
    });
    return list;
  }
}

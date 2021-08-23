import 'package:flutter/material.dart';

import 'package:rowmate/pages/bluetooth/bluetooth_widget.dart';
import 'package:rowmate/pages/commons/background_widget.dart';
import 'package:rowmate/pages/commons/appname_widget.dart';

class LandingPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          BackgroundImage('bg_bluetooth'),
          Column(
            children: [
              AppNameWidget(),
              BluetoothWidget(),
            ],
          ),
        ],
      ),
    );
  }
}

import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:material_design_icons_flutter/material_design_icons_flutter.dart';

import 'package:rowmate/bloc/bluetooth/bluetooth.dart';

import 'package:rowmate/pages/bluetooth/bluetooth_info_widget.dart';
import 'package:rowmate/pages/commons/button_widget.dart';
import 'package:qrscan/qrscan.dart' as scanner;
import 'package:permission_handler/permission_handler.dart';

class BluetoothWidget extends StatefulWidget {
  @override
  BluetoothWidgetState createState() {
    return BluetoothWidgetState();
  }
}

class BluetoothWidgetState extends State<BluetoothWidget> {
  TextEditingController _outputController;
  @override
  initState() {
    super.initState();

    this._outputController = new TextEditingController();
  }

  @override
  Widget build(BuildContext context) {
    final bleBloc = BlocProvider.of<BleBloc>(context);

    return _showContent(bleBloc);
  }

  String qrV = "";

  Future _scan(BleBloc bleBloc) async {
    await Permission.camera.request();
    String barcode = await scanner.scan();

    if (barcode == null) {
      print('nothing return.');
    } else {
      // this._outputController.text = barcode;
      this.qrV = barcode;
      // AlertDialog(title: Text(this.qrV));
      this._outputController.text = barcode;
      print("Setting UID");
      print(this._outputController.text);
      bleBloc.setUID(this._outputController.text);
      print("connecting");
      bleBloc.add(Scanning());
      return barcode;
    }
  }

  // void scanIt(BleBloc bleBloc) {
  //   // print("scanning");
  //   // _scan();
  //   print("Setting UID");
  //   print(this._outputController.text);
  //   bleBloc.setUID(this._outputController.text);
  //   print("connecting");
  //   bleBloc.add(Scanning());
  // }

  Widget _showContent(BleBloc bleBloc) {
    var _state = bleBloc.state;
    //bleBloc.setUID("B8:27:EB:32:DE:89");
// bleBloc.add(Scanning())
    if (_state is BleEnabled) {
      return Expanded(
        child: Stack(children: [
          BluetoothInfo(icon: MdiIcons.bluetooth, label: 'Ready to connect'),
          _showAction(MdiIcons.bluetoothAudio, 'Scan and Connect',
              () => _scan(bleBloc)),
          Container(
            padding: const EdgeInsets.all(120.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Container(
                  width: 50.0,
                  child: TextField(
                    controller: this._outputController,
                    maxLines: 2,
                    style: TextStyle(color: Colors.white),
                  ),
                ),
                // Text(
                //   "UID",
                //   style: TextStyle(
                //       fontWeight: FontWeight.w200,
                //       fontSize: 20.0,
                //       color: Colors.white),
                // ),
                //ElevatedButton(child: new Text('Click me'))
              ],
            ),
          )
        ]),
      );
    }

    if (_state is BleDisabled) {
      Permission.bluetooth.request();
      Permission.location.request();
      return BluetoothInfo(
          icon: MdiIcons.bluetoothOff,
          label: 'Turn bluetooth and location on.');
    }

    if (_state is BleScanning) {
      return Column(children: [
        BluetoothInfo(
            icon: MdiIcons.bluetoothAudio,
            label: 'Connecting to ' + this._outputController.text),
        Container(
          margin: EdgeInsets.all(16.0),
          child: CircularProgressIndicator(
            valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
          ),
        )
      ]);
    }

    if (_state is BleFailure) {
      return Expanded(
          child: Stack(children: [
        BluetoothInfo(icon: MdiIcons.alertCircle, label: 'An error occured'),
        _showAction(MdiIcons.refresh, 'Retry to connect',
            () => bleBloc.add(Scanning())),
      ]));
    }

    return Column(children: [
      BluetoothInfo(icon: MdiIcons.bluetoothSettings, label: 'Checking..'),
      Container(
        margin: EdgeInsets.all(16.0),
        child: CircularProgressIndicator(
          valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
        ),
      )
    ]);
  }

  Widget _showAction(IconData icon, String label, Function action) {
    return Container(
      alignment: Alignment.bottomCenter,
      padding: EdgeInsets.only(left: 40.0, right: 40.0, bottom: 20.0),
      child: Card(
          color: Colors.transparent,
          elevation: 0.5,
          child: Container(
            padding: EdgeInsets.only(top: 20.0),
            child: ButtonWidget(label: label, iconData: icon, action: action),
          )),
    );
  }
}

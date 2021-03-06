import 'package:flutter/material.dart';

class Weather extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Text('New York', style: new TextStyle(color: Colors.white)),
        Text('Rain', style: new TextStyle(color: Colors.white, fontSize: 32.0)),
        Text('72°F',  style: new TextStyle(color: Colors.white)),
        Image.network('https://openweathermap.org/img/w/01d.png'),
        Text('Jul 04, 2021', style: new TextStyle(color: Colors.white)),
        Text('05:08', style: new TextStyle(color: Colors.white)),
      ],
    );
  }
}
import 'package:flutter/material.dart';

class WeatherItem extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('New York', style: new TextStyle(color: Colors.black)),
            Text('Rain', style: new TextStyle(color: Colors.black, fontSize: 24.0)),
            Text('72°F',  style: new TextStyle(color: Colors.black)),
            Image.network('https://openweathermap.org/img/w/01d.png'),
            Text('Jul 04, 2021', style: new TextStyle(color: Colors.black)),
            Text('05:08', style: new TextStyle(color: Colors.black)),
          ],
        ),
      ),
    );
  }
}
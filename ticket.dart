import 'package:flutter/material.dart';
import 'package:metrorun/screens/wrapper.dart';

class Ticket extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.cyan[200],
      appBar: AppBar(
        centerTitle: true,
        backgroundColor: Colors.green,
        title: Text(
          'TICKET',
          style: TextStyle(
            color: Colors.white,
            fontSize: 25.0,
          ),
        ),
      ),

      body: Container(
        child: ListView(
          children: <Widget>[
          
            Center(
              child: Text(
                'PAYMENT SUCCESSFUL !! 
                Scan the QR CODE below : ',
                style: TextStyle(
                  fontSize: 50.0,
                  fontWeight: FontWeight.w800,
                ),
              ),
            )

            getImageAsset(),

            Padding(
              padding: EdgeInsets.symmetric(horizontal: 150.0),
              child: ButtonTheme(
                minWidth: 200.0,
                height: 50.0,
                child: RaisedButton(
                  shape: new RoundedRectangleBorder(
                    borderRadius: new BorderRadius.circular(50.0),
                  ),
                elevation: 5.0,
                splashColor: Colors.yellowAccent,
                color: Colors.green,
                textColor: Colors.white,
              ),
            ),

          ],
        ),
      ),
    );
  }
}

Widget getImageAsset() {
  AssetImage assetImage = AssetImage('assets/QRcode.png');
  Image image = Image(image: assetImage, width: 400.0, height: 400.0,);

  return Container(
    child: image,
    margin: EdgeInsets.symmetric(vertical: 20.0, horizontal:20.0),
  );
}

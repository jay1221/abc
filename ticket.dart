import 'package:flutter/material.dart';
import 'package:metrorun/screens/services/home.dart';
import 'package:metrorun/screens/shared/loading.dart';
            
class Home extends StatefulWidget {
  final Function toggleView;

  Home({this.toggleView});

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  //final AuthService _auth = AuthService();
  final _formKey = GlobalKey<FormState>();
  bool loading = false;

  @override
  Widget build(BuildContext context) {
    return loading ? Loading() : Scaffold(
            backgroundColor: Colors.cyan[100],
            appBar: AppBar(
              backgroundColor: Colors.green,
              elevation: 5.0,
              title: Text('TICKET'),
            ),
            body: Container(
              padding: EdgeInsets.symmetric(vertical: 20.0, horizontal: 50.0),
              child: Form(
                key: _formKey,
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
            ));
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


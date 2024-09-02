import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:calculatorode/constants/colors.dart';
import 'package:calculatorode/screens/result_screen.dart';
import '../widgets/textField.dart';
import 'package:http/http.dart' as http;

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final TextEditingController _controller = TextEditingController();
  bool _loading = false;

  Future<void> _handleButtonPress() async {
    final userInput = _controller.text;
    if (userInput.isNotEmpty) {
      setState(() {
        _loading = true;
      });

      final response = await http.post(
        Uri.parse('http://your-backend-url/solve'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'equation': userInput}),
      );

      setState(() {
        _loading = false;
      });

      if (response.statusCode == 200) {
        final solution = jsonDecode(response.body)['solution'];
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => ResultScreen(
              userInput: userInput,
              answer: solution,
            ),
          ),
        );
      } else {
        // Handle error
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Error solving ODE')),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final screenHeight = MediaQuery.of(context).size.height;
    final padding = EdgeInsets.symmetric(horizontal: 20, vertical: 25);
    final decoration = BoxDecoration(
      color: AppColors.primaryColor,
      borderRadius: BorderRadius.vertical(top: Radius.circular(30)),
    );

    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        title: const Text("ODE Calculator"),
        backgroundColor: Colors.blue,
      ),
      body: Column(
        children: [
          CustomTextField(controller: _controller),
          const Spacer(),
          Container(
            padding: padding,
            decoration: decoration,
            child: Column(
              children: [
                ElevatedButton(
                  onPressed: _handleButtonPress,
                  child: Text(
                    "ANSWER",
                    style: TextStyle(fontSize: 32, fontFamily: "ComputerModern"),
                  ),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.green,
                    padding: EdgeInsets.symmetric(horizontal: 32, vertical: 16),
                  ),
                ),
              ],
            ),
          ),
          if (_loading) CircularProgressIndicator(),
        ],
      ),
    );
  }
}

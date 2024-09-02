import 'package:flutter/material.dart';
import '../constants/colors.dart';

class ResultScreen extends StatelessWidget {
  final String userInput;
  final String answer;

  const ResultScreen({super.key, required this.userInput, required this.answer});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("ODE Calculator Result"),
        backgroundColor: Colors.blue,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Question:',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, fontFamily: "ComputerModern"),
            ),
            SizedBox(height: 10),
            Text(
              userInput,
              style: TextStyle(fontSize: 20, fontFamily: "ComputerModern"),
            ),
            SizedBox(height: 30),
            Text(
              'Answer:',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, fontFamily: "ComputerModern"),
            ),
            SizedBox(height: 10),
            Text(
              answer,
              style: TextStyle(fontSize: 20, fontFamily: "ComputerModern"),
            ),
          ],
        ),
      ),
    );
  }
}

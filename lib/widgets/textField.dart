import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import '../constants/colors.dart';

class CustomTextField extends StatelessWidget {
  final TextEditingController controller;

  const CustomTextField({super.key, required this.controller});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 25, vertical: 30),
      child: TextField(
        controller: controller,
        textAlign: TextAlign.center,
        maxLines: 1,
        decoration: InputDecoration(
          hintText: "x^2y'+xy=0",
          hintStyle: TextStyle(
              fontSize: 30, color: Colors.grey, fontFamily: "ComputerModern"),
          fillColor: AppColors.primaryColor,
          filled: true,
        ),
        style: const TextStyle(fontSize: 30, fontFamily: "ComputerModern"),
        autofocus: true,
        autocorrect: false,
        showCursor: true,
      ),
    );
  }
}

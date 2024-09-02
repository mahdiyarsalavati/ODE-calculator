import 'package:flutter/material.dart';
import '../constants/colors.dart';

class Button extends StatelessWidget {
  const Button({
    Key? key,
    required this.label,
    required this.onPressed,
    this.color = AppColors.secondaryColor,
    this.shape = "CircleAvatar",
  }) : super(key: key);

  final String label;
  final Color color;
  final String shape;
  final void Function(String) onPressed;

  @override
  Widget build(BuildContext context) {
    if (shape == "CircleAvatar") {
      return Material(
        elevation: 6,
        color: AppColors.primaryColor,
        borderRadius: BorderRadius.circular(50),
        child: CircleAvatar(
          radius: 33,
          backgroundColor: color,
          child: TextButton(
            onPressed: () => onPressed(label),
            child: Text(
              label,
              style: TextStyle(fontSize: 32, fontWeight: FontWeight.w600),
            ),
          ),
        ),
      );
    } else if (shape == "rectangle") {
      return Material(
        elevation: 6,
        color: AppColors.primaryColor,
        borderRadius: BorderRadius.circular(15),
        child: Container(
          width: 390,
          height: 60,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: color,
            borderRadius: BorderRadius.circular(70),
          ),
          child: TextButton(
            onPressed: () => onPressed(label),
            child: Text(
              label,
              style: TextStyle(fontSize: 32, fontWeight: FontWeight.w600),
            ),
          ),
        ),
      );
    }
    return Material(
      elevation: 6,
      color: AppColors.primaryColor,
      borderRadius: BorderRadius.circular(15),
      child: Container(
        width: 72,
        height: 110,
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: color,
          borderRadius: BorderRadius.circular(70),
        ),
        child: TextButton(
          onPressed: () => onPressed(label),
          child: Text(
            label,
            style: TextStyle(fontSize: 32, fontWeight: FontWeight.w600),
          ),
        ),
      ),
    );
  }
}

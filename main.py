'''
This is the Mental Aptitude and Mood Examiner and Extrapolator Software.(M.A.M.E.E.S)
Author : I. Varnasseri G.
Enterprise production date : 24-05-28.
This software is designed to examine, extrapolate and provide reports regarding mental 
aptitude and mood related data. This software aims to collect data about the following:
    I- The mental aptitude examiner: is composed of the following:
            1- Numeric Memory : Consisting of a memory test similar to that of number
               memory test on humanbenchmark.com
            
            2- Multiplication test : consisting of a multiplication test involving 
               Numbers with two or three digits.

            3- Determinant calculation : Calculating the determinants of 2x2 matrices
               with at least three digit entries. And 3x3 with at least two digit nums.

    II- The mood Examiner : is composed of the following:
            1- General mood questionaire taken exactly 1h before bedtime.

            2- General O.C.D. questionaire taken exactly 1h before bedtime.

            3- Weight.
'''
'''
General mood questionaire:
On a scale of 1-10 :

1- How would you rate your last night sleep?
    1-1- How many hours did you sleep last night?
    1-2- How would you rate your mood before your last night's sleep?
    1-3- What time did you wake up today?

2- How would you rate your apetite today?
    2-1- How many meals have you had today?
    2-2- How many snacks have you had today?
    2-3- How many calories did you get today?
    2-4- How many drinks did you have today?

3- How would you rate you mood today?
    3-1- How would you rate your mood right after waking up?
    3-2- How would you rate your mood around the middle of the day?
    3-3- How would you rate your mood around the night?

4- How would you rate your cognitive performance today?
    4-1- How would you rate your chess performance today?
    4-2- How would you rate your mathematical performance today?
    4-3- How would you rate your verbal performance today?
    4-4- How would you rate your common sense performance?

5- How would you rate the volume of your thoughts?

'''

'''
General O.C.D. questionaire

1- How many times did you wash your hands today?

2- How would you rate the number of your hand washes today, compared 
   to yesterday? (from -5(less) to 5(more))

3- How would you rate the number of your intrusive thoughts?

'''

import matplotlib.pyplot as plt 
import math 
import time
import datetime
import arithmetic_game as ag

FILES = ["ma1.txt",
"ma2.txt",
"ma3.txt",
"me111.txt",
"me112.txt",
"me113.txt",
"me121.txt",
 "me122.txt",
"me123.txt",
"me124.txt",
"me131.txt",
"me132.txt",
"me133.txt",
"me141.txt",
"me142.txt",
"me143.txt",
"me144.txt",
"me15.txt",
"me21.txt",
"me22.txt","me23.txt"]

print("The battery will commence now.")


# Create a question class


# Read the file `data/quiz.csv` to create a list of questions


# Randomly choose 10 question


# For each question display it in the following format followed by a prompt for answer
"""
<Question text>
1. Option 1
2. Option 2
3. Option 3
4. Option 4

Answer :: 
"""
import csv
score = 0
score = int(score)
f = open("quiz.csv",'r')

d=csv.reader(f)

next(f) #To Skip Header Row

k = 0

adm = str(input(""))

for row in d:

    if str(row[0])==adm:

       print("Que:= ", row[1])

       print("01 = ", row[2])

       print("02 = ", row[3])

       print("03 = ", row[4])

       print("04 = ", row[5])

       #print("Key = ", row[6])

       answer = input("Key: ")
       if answer ==str(row[6]):
           print("Correct!")
           score = score + 1
       else:
           print("Incorrect, Correct Answer is " + str(row[6]))

       print("Your current score is " + str(score) + " out of 10")
# Keep score for all right and wrong answer


# Take an extra step and output the correct answer for all wrong answers at the end

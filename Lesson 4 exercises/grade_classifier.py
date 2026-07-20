# # Practical Task
# Task Overview 

# Build a student grade classifier called grade_classifier.py that takes a learner’s name and marks for three subjects, calculates an average, assigns a grade and a status (Pass/Fail), and displays a full report card. The program must correctly use conditionals for all grade and status logic.

# Requirements 

# Collect learner name and marks for three subjects (as floats) using input()
# Calculate the average mark across the three subjects
# Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
# Assign Pass status if the average is 50 or above, Fail otherwise
# Flag any individual subject mark below 40 as ‘needs intervention’
# Display a formatted report card showing all inputs, the average, the grade, the status, and any intervention flags
# Outcome of Task 

# At the end of this task, you should be competent in writing if, elif, and else statements to control program flow based on conditions, using the comparison operators (==, !=, <, >, <=, >=) correctly in conditions, combining conditions using the logical operators and, or, and not, using the in keyword to check membership in a list or string, and nesting conditional statements while distinguishing between the appropriate use of elif and separate if statements. Before progressing to the next unit, complete the Unit 5 Quiz to check your understanding of the key concepts covered, identify any areas that may need further practice, and reinforce your learning.

learners_name = input("Please enter the your name: ")
subject1 = (float(input("Please enter your marks out of 100 for subject 1: ")))
subject2 = (float(input("Please enter your marks out of 100 for subject 2: ")))
subject3 = (float(input("Please enter your marks out of 100 for subject 3: ")))

AverageMark  = (subject1 + subject2 + subject3) / 3
Pass = (AverageMark >= 50-100)
Fail = (AverageMark <= 0-50 )

if (AverageMark >= 80) == "A" :
    print (f"{learners_name}, "" your Grade status is a A ")

elif (AverageMark >= 70) == "B":
    print (f"{learners_name}, "" your Grade status is a B ")
    
elif (AverageMark >= 60) == "C":
    print (f"{learners_name}, "" your Grade status is a C ")

elif (AverageMark >= 50) == "D":
    print (f"{learners_name}, "" your Grade status is a D ")
    
elif (AverageMark <= 50) == "F":
    print (f"{learners_name}, "" your Grade status is a F ")
    
    status = "Pass" if AverageMark>= 50 else "Fail"
    
intervention_subjects = []
if subject1 < 40:
    intervention_subjects.append("Subject 1")
if subject2 < 40:
    intervention_subjects.append("Subject 2")
if subject3 < 40:
    intervention_subjects.append("Subject 3")
    
print("          REPORT CARD")

print(f"Learner Name   : {learners_name}")
print(f"Subject 1 mark : {subject1:.1f}")
print(f"Subject 2 mark : {subject2:.1f}")
print(f"Subject 3 mark : {subject3:.1f}")
print(f"Average mark   : {AverageMark:.1f}")
print(f"Status         : {status}")
    



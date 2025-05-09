# getting the raw scores from the user
print("give me the score out of 60 for the first exam.")
exam1_score = int(input("> "))
print("give me the score out of 75 for the second exam")
exam2_score = int(input("> "))
print("give me the score out of 120 for the project.")
project_score = int(input("> "))

# getting the initial percentages
exam1_percent = exam1_score / 60
exam2_percent = exam2_score / 75
project_percent = project_score / 120

# rounding the percentages
exam1_percent = round(exam1_percent, 2)
exam2_percent = round(exam2_percent, 2)
project_percent = round(project_percent, 2)

# converting the percentages by their weightings for the final percentages
exam1_final = exam1_percent * 25
exam2_final = exam2_percent * 30
project_final = project_percent * 45

# calculating the final percentage
total_percent = round(exam1_final + exam2_final + project_final)

# outputting stuff
print(f"scored {exam1_percent * 100}% on the first exam.")
print(f"scored {exam2_percent * 100}% on the second exam.")
print(f"scored {project_percent * 100}% on the project.")
print(f"total score: {exam1_score + exam2_score + project_score} out of 255 ({total_percent}%)")
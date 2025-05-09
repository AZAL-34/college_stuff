print("give me your name.")
name = input("> ")
print("give me a score from 0 to 35.")
score = int(input("> "))
if score == 0:
    print(f"wow {name}, you failed HARD.")
elif score == 35:
    print("nerd.")
elif score > 0 and score < 35:
    print(f"alright {name}, i guess {score} is an alright score.")
elif score > 35:
    print("cheater.")
elif score < 0:
    print("reverse cheater.")
else:
    print("if you're reading this, i messed up somehow.")
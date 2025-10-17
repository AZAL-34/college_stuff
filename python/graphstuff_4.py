import matplotlib.pyplot as plt

slices = [13, 11, 12, 5, 4]
languages = ["C", "Python", "Java", "C++", "C#"]
cols = ["#3ba740", "#a8d47a", "#ffffff", "#ababab", "#000000"]

plt.pie(slices, labels = languages, colors = cols, startangle = 115, shadow = True, explode = (0, 0.1, 0, 0, 0), autopct = "%1.1f%%")
plt.title("Interesting Graph\nCheck it Out")
plt.show()
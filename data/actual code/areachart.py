import matplotlib.pyplot as plt

years = [2019, 2020, 2021, 2022, 2023]
programming = [40, 50, 60, 80, 90]
web_development = [20, 30, 50, 70, 80]
data_science = [10, 20, 30, 60, 70]
plt.fill_between(years, programming, color = "#FF80C0", alpha = 0.5, label = "Programming")
plt.fill_between(years, web_development, color = "#40C0FF", alpha = 0.5, label = "Web Development")
plt.fill_between(years, data_science, color = "#8000FF", alpha = 0.5, label = "Data Science")
plt.title("dpddpddpddpddpddpdd")
plt.xlabel("years")
plt.ylabel("students")
plt.legend()
plt.show()
import pandas as pd

def prinegrpreger(str):
    print(str)

assessment_dpdd_yr1 = pd.DataFrame({
    "Name":["John", "John", "John", "Sam", "Sam", "Sam", "Frank", "Frank", "Frank", "Owen", "Owen", "Owen"],
    "Assessment No":[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    "Programming, Problem Solving and ESP":[22, 21, 14, 20, 23, 22, 21, 12, 15, 15, 21, 22],
    "Data":[21, 20, 19, 17, 25, 17, 20, 15, 19, 19, 21, 21],
    "Business Context":[18, 17, 15, 22, 21, 19, 17, 18, 12, 17, 16, 20],
    "Emerging Issues and Legislation":[20, 22, 24, 24, 25, 22, 22, 22, 18, 22, 22, 20],
    "Digital Environments and Security":[21, 24, 23, 19, 16, 16, 19, 16, 23, 23, 19, 19]
})

maxprog = assessment_dpdd_yr1["Programming, Problem Solving and ESP"].max()
maxdata = assessment_dpdd_yr1["Data"].max()
maxbusi = assessment_dpdd_yr1["Business Context"].max()
maxlegi = assessment_dpdd_yr1["Emerging Issues and Legislation"].max()
maxsecu = assessment_dpdd_yr1["Digital Environments and Security"].max()
prinegrpreger(assessment_dpdd_yr1)
import random
import fn

responses = ["uh... sure.", "oh, HELL no.", "maybe.", "ask fahim.", "probably, but i wouldn't put money on it.", "probably not.", "YES. YES. YES."]

while True:
    fn.printy("ask me a question.")
    question = input("> ")
    if question == ("is blake still pissed that i turned his pc off that one time"):
        break
    else:
        fn.printy(random.choice(responses))








































days_since_i_turned_blakes_pc_off = 63
full_weeks = 9
weeks = "exactly"
full_months = 2
months = "over"
full_years = 0
years = "over"
original_date = ["Thursday", 26, "September", 2024]
stillPissed = False # ??????????????
fn.printy(f"{stillPissed}.")
fn.printy(f"it has been {days_since_i_turned_blakes_pc_off} days since it happened.")
fn.printy("this number is equivalent to:")
fn.printy(f"{weeks} {full_weeks} weeks.")
fn.printy(f"{months} {full_months} months.")
fn.printy(f"{years} {full_years} years.")
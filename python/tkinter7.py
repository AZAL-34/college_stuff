import tkinter as tk
from datetime import datetime
import math, time

root = tk.Tk()
root.title("Analogue Clock")

CLOCK_WIDTH = 400
CLOCK_HEIGHT = 400
CLOCK_CENTER_X = CLOCK_WIDTH // 2
CLOCK_CENTER_Y = CLOCK_HEIGHT // 2
CLOCK_RADIUS = min(CLOCK_WIDTH, CLOCK_HEIGHT) // 2 - 20

def draw_clock():
    current_time = datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
    canvas.delete("all")
    canvas.create_oval(CLOCK_CENTER_X - CLOCK_RADIUS, CLOCK_CENTER_Y - CLOCK_RADIUS, CLOCK_CENTER_X + CLOCK_RADIUS, CLOCK_CENTER_Y + CLOCK_RADIUS, width=5)
    hour_angle = math.radians((hour % 12) * 30 - 90)
    hour_x = CLOCK_CENTER_X + 0.6
    hour_angle = math.radians((hour % 12) * 30 - 90)
    hour_x = CLOCK_CENTER_X + 0.6 * CLOCK_RADIUS * math.cos(hour_angle)
    hour_y = CLOCK_CENTER_Y + 0.6 * CLOCK_RADIUS * math.sin(hour_angle)
    canvas.create_line(CLOCK_CENTER_X, CLOCK_CENTER_Y, hour_x, hour_y, width=4)
    minute_angle = math.radians(minute * 6 - 90)
    minute_x = CLOCK_CENTER_X + 0.8 * CLOCK_RADIUS * math.cos(minute_angle)
    minute_y = CLOCK_CENTER_Y + 0.8 * CLOCK_RADIUS * math.sin(minute_angle)
    canvas.create_line(CLOCK_CENTER_X, CLOCK_CENTER_Y, minute_x, minute_y, width=3)
    second_angle = math.radians(second * 6 - 90)
    second_x = CLOCK_CENTER_X + 0.9 * CLOCK_RADIUS * math.cos(second_angle)
    second_y = CLOCK_CENTER_Y + 0.9 * CLOCK_RADIUS * math.sin(second_angle)
    canvas.create_line(CLOCK_CENTER_X, CLOCK_CENTER_Y, second_x, second_y, width=2)
    canvas.create_oval(CLOCK_CENTER_X - 5, CLOCK_CENTER_Y - 5, CLOCK_CENTER_X + 5, CLOCK_CENTER_Y + 5, width=5, fill="black") 
    root.after(1000, draw_clock)




def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root2.after(1000, update_time)  # Update every 1000 milliseconds (1 second)
# Create the main window
root2 = tk.Tk()
root2.title("Digital Clock")
# Create a label to display the time
clock_label = tk.Label(root2, text="", font=("Comic Sans", 48))
clock_label.pack(padx=20, pady=20)
# Start updating the time
update_time()
# Start the Tkinter event loop
canvas = tk.Canvas(root, width=CLOCK_WIDTH, height=CLOCK_HEIGHT)
canvas.pack()
draw_clock()
root.mainloop()
root2.mainloop()
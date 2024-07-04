from tkinter import messagebox
import requests
import tkinter
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rips = 0
timerr = None



import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"][0]['question']
print(question_data)
# ---------------------------- TIMER RESET ------------------------------- #

radwan = True
def restart_timer():
    time(0)
    label.config(text="typing speed test ", font=(FONT_NAME, 30, 'bold'), fg=GREEN, background=YELLOW)
    canvas.itemconfig(timer_update, text='00:00')


khaled = False

def time(count):
        minutes = math.floor(count / 60)
        seconds = count % 60
        if seconds < 10:
            seconds = f'0{seconds}'
        if count >= 0:
            canvas.itemconfig(timer_update, text=f'{minutes}:{seconds}')
            global timerr
            timerr = window.after(1000, time, count + 1)



def check():
    global count
    minutes = math.floor(count / 60)
    seconds = count % 60
    if website_entry.get() == question_data:
        messagebox.showinfo(title='Awsome', message=f'uou manged it in {minutes}:{seconds}')
    else:
        messagebox.showerror(title="Error", message="Please enter valid input")






window = tkinter.Tk()
window.title("welcome to tomato reminder")
window.config(padx=100, pady=50)
window.configure(background='#f7f5dd')

canvas = tkinter.Canvas(width=200, height=224, bg='#f7f5dd', highlightthickness=0)
timer_update = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, 'bold'), fill='white')
canvas.grid(column=0, row=1)

label = tkinter.Label(text="typing speed test ", font=(FONT_NAME, 30, 'bold'), fg=GREEN, background=YELLOW)
label.grid(row=0, column=1)

label2 = tkinter.Label(text=question_data, font=(FONT_NAME, 20, 'bold'), fg=GREEN, background=YELLOW)
label2.grid(row=1, column=1)


start_button = tkinter.Button(window, text="check", highlightthickness=0, command=check)
start_button.grid(row=2, column=0)

stop = tkinter.Button(window, text="start", highlightthickness=0, command=restart_timer)
stop.grid(row=2, column=2)


website_entry = tkinter.Entry(width=100, highlightthickness=0, font=(FONT_NAME))
website_entry.grid(row=2, column=1, columnspan=1)
website_entry.focus()

window.mainloop()
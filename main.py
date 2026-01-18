from dotenv import load_dotenv
load_dotenv()

import requests
from tkinter import *
from function import convert_currency

window = Tk()
window.minsize(300, 100)
window.resizable(False, False)
window.title("Currency Converter")
window.config(bg="#012030")

def count():
    try:
        notification_label.config(text="")

        amount = float(amount_input.get())
        currency_from = from_currency_var.get()
        currency_to = to_currency_var.get()

        result = convert_currency(amount, currency_from, currency_to)

        result_var.set(f"{result:.2f}")

    except ValueError:
        notification_label.config(text="❌ Invalid amount or API response")

    except requests.exceptions.Timeout:
        notification_label.config(text="⏰ API timeout")

    except requests.exceptions.RequestException:
        notification_label.config(text="❌ API connection error")


# Color
main_color = "#012030"
text_color= "#fff"

# Entry
amount_input = StringVar(value="0")
amount = Entry(window, textvariable=amount_input, width=20, font=("Arial", 12), justify="center")
amount.grid(row=0, column=0, padx=10, pady=10)

# Dropdowns
from_currency_var = StringVar(value="CZK")
drop_down_options1 = OptionMenu(window, from_currency_var, "CZK", "EUR", "USD")
drop_down_options1.config(bg=main_color, fg=text_color)
drop_down_options1.grid(row=0, column=1)

to_currency_var = StringVar(value="EUR")
drop_down_options2 = OptionMenu(window, to_currency_var, "CZK", "EUR", "USD")
drop_down_options2.config(bg=main_color, fg=text_color)
drop_down_options2.grid(row=1, column=1)

# Button
count_button = Button(window, text="Convert", font=("Arial", 12), command=count)
count_button.grid(row=0, column=3, padx=10, pady=10)

# Label
result_var = StringVar(value="0")
result_label = Label(window, textvariable=result_var, bg=main_color, fg=text_color, font=("Arial", 12, "bold"))
result_label.grid(row=1, column=0)

notification_label = Label(bg=main_color, fg=text_color, font=("Arial", 12))
notification_label.grid(row=2, column=0)

# Function for amount
def select_all(event):
    event.widget.select_range(0, END)
    event.widget.icursor(END)

def clear_zero(event):
    if amount_input.get() == "0":
        amount_input.set("")

amount.bind("<FocusIn>", select_all)
amount.bind("<KeyPress>", clear_zero)

# Main Loop
window.mainloop()
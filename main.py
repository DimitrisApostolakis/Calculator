from tkinter import *


def button_press(num):
    global calculation

    if str(num) in "%*-+/.":
        if calculation and calculation[-1] in "%*-+/.":
            calculation = calculation[:-1]  # Remove the last symbol

    calculation += str(num)
    equation_label.set(calculation)


# Delete one character from the equation label.
def del_button():
    global calculation
    calculation = calculation[:-1]
    equation_label.set(calculation)


# Calculating the equation.
def equals():
    global calculation

    try:
        result = str(eval(calculation))
        equation_label.set(result)

        calculation = result
    except ZeroDivisionError:
        equation_label.set("Zero Division Error")
    except SyntaxError:
        equation_label.set("Syntax Error")
    except ValueError:
        equation_label.set("Out of limits.")


def clear():
    global calculation
    calculation = ""
    equation_label.set(calculation)


window = Tk()
window.title("Calculator")
window.geometry("364x585")
window.configure(bg="#1f2024")
img = PhotoImage(file="icon.png")
window.iconphoto(False, img)
window.resizable(width=False, height=False)

calculation = ""

equation_label = StringVar()

calculation_label = Label(window, textvariable=equation_label, font=("Arial", 18), bg="#1a1c1c", width=24, height=2,
                          fg="white")
calculation_label.pack(fill="both", expand=True)

frame = Frame(window)
frame.pack()

# Creating the buttons for the numbers 1-9 and out of the loop we create the 0 button separately.
for i in range(1, 10):
    number_buttons = Button(frame, text=str(i), height=4, width=9, font=25,
                            command=lambda current_number=i: button_press(current_number), bg="grey", fg="white")
    number_buttons.grid(row=(9 - i) // 3 + 1, column=(i - 1) % 3)

number0_button = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press("0"), bg="grey",
                        fg="white")
number0_button.grid(row=4, column=1)

decimal_button = Button(frame, text=".", height=4, width=9, font=35, command=lambda: button_press("."), bg="#1f2024",
                        fg="white")
decimal_button.grid(row=4, column=2)

# Operators
modulo_button = Button(frame, text="%", height=4, width=9, font=35, command=lambda: button_press("%"), bg="#1f2024",
                       fg="white")
modulo_button.grid(row=0, column=0)

power_button = Button(frame, text="^2", height=4, width=9, font=35, command=lambda: button_press("**2"), fg="white",
                      bg="#1f2024")
power_button.grid(row=0, column=1)

root_button = Button(frame, text="^1/2", height=4, width=9, font=35, command=lambda: button_press("**1/2"), fg="white",
                     bg="#1f2024")
root_button.grid(row=0, column=2)

multi_button = Button(frame, text="*", height=4, width=9, font=35, command=lambda: button_press("*"), fg="white",
                      bg="#1f2024")
multi_button.grid(row=1, column=3)

minus_button = Button(frame, text="-", height=4, width=9, font=35, command=lambda: button_press("-"), fg="white",
                      bg="#1f2024")
minus_button.grid(row=2, column=3)

plus_button = Button(frame, text="+", height=4, width=9, font=35, command=lambda: button_press("+"), fg="white",
                     bg="#1f2024")
plus_button.grid(row=3, column=3)

divide_button = Button(frame, text="/", height=4, width=9, font=35, command=lambda: button_press("/"), fg="white",
                       bg="#1f2024")
divide_button.grid(row=4, column=0)

equal_button = Button(frame, text="=", height=4, width=9, font=35, command=equals, bg="#20a898")
equal_button.grid(row=4, column=3)

# GUI Operations
clear_button = Button(window, text="C", height=3, width=16, font=35, command=clear, fg="white", bg="#1f2024")
clear_button.pack(fill="both", expand=True)

del_button = Button(frame, text="DEL", height=4, width=9, font=35, command=del_button, fg="#a30b25", bg="#1f2024")
del_button.grid(row=0, column=3)

window.mainloop()

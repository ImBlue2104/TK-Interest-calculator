from tkinter import Tk, Entry, Label, Button

# Create window
root = Tk()
root.title("Interest Calculator")
root.geometry("400x400")

# Title of app
Label(root, text="Welcome to the Interest Calculator!", fg='white', bg='black').pack()
Label(root, text="Enter parameters to calculate compound and simple interest.", fg='white', bg='black').pack()

# Labels
Label(root, text="Enter Principal (amount):", bg='light grey').pack()
p_input = Entry(root)
p_input.pack()

Label(root, text="Enter Time (years):", bg='light grey').pack()
t_input = Entry(root)
t_input.pack()

Label(root, text="Enter Interest (%):", bg='light grey').pack()
i_input = Entry(root)
i_input.pack()
in:#daydream-bulletin%20cocClear
# Calculation function
def calc():
    p = float(p_input.get())
    t = float(t_input.get())
    i = float(i_input.get()) / 100   # convert % to decimal

    simple_int = p * i * t
    comp_int = p * (1 + i)**t

    Label(root, text=f"Simple Interest = {simple_int:.2f}", bg='light grey').pack()
    Label(root, text=f"Compound Interest = {comp_int:.2f}", bg='light grey').pack()

# Button
Button(root, text='Calculate', command=calc, bg='brown', fg='white').pack()

root.mainloop()

from tkinter import *


def calculate():
    choice = radio_used()
    value_mile = int(entry_box.get())
    if choice == 1:
        value_km = value_mile * 1.60934
        result.config(text=f'{value_km}')
    elif choice == 2:
        value_m = value_mile * 1.60934*1000
        result.config(text=f'{value_m}')


def radio_used():
    choice = radio_state.get()
    return choice


window = Tk()
window.config(padx=10, pady=10)
window.minsize(width=300, height=100)
window.title('Mile to Km Converter')

entry_box = Entry(width=15)
entry_box.grid(column=2, row=1)

label_mile = Label(text='Miles')
label_mile.config(padx=5)
label_mile.grid(column=3, row=1)

label_is_equal = Label(text='is equal to ')
label_is_equal.grid(column=1, row=2)

result = Label(text='0')
result.grid(column=2, row=2)

radio_state = IntVar()
radio_km = Radiobutton(text='Km', value=1, variable=radio_state, command=radio_used)
radio_km.grid(column=3, row=2)
radio_m = Radiobutton(text='m', value=2, variable=radio_state, command=radio_used)
radio_m.grid(column=4, row=2)


calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(column=2, row=3)




window.mainloop()

from tkinter import *

def calculate():
    value_mile = int(entry_box.get())
    value_km = value_mile * 1.60934
    result.config(text=f'{value_km}')

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

label_km = Label(text='Km')
label_km.grid(column=3, row=2)

calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(column=2, row=3)




window.mainloop()

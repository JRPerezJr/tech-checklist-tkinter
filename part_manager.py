from tkinter import messagebox, Tk, StringVar, Listbox, W, END, Label, Entry, Scrollbar, Button, NumberVar
from db import Database
from tkinter.ttk import Combobox

# Create window object
app = Tk()
string = StringVar()
number = NumberVar()
combo = Combobox(app)


db = Database('store.db')


def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    if repair_order_text.get() == '' or vin_number_text.get() == '' or part_desc_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'All Fields Required')
        return
    db.insert(repair_order_text.get(), vin_number_text.get(),
              part_desc_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (repair_order_text.get(), vin_number_text.get(),
                            part_desc_text.get(), price_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        repair_order_entry.delete(0, END)
        repair_order_entry.insert(END, selected_item[1])
        vin_number_entry.delete(0, END)
        vin_number_entry.insert(END, selected_item[2])
        part_desc_entry.delete(0, END)
        part_desc_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], repair_order_text.get(), vin_number_text.get(),
              part_desc_text.get(), price_text.get())
    populate_list()


def clear_text():
    repair_order_entry.delete(0, END)
    vin_number_entry.delete(0, END)
    part_desc_entry.delete(0, END)
    price_entry.delete(0, END)


Main
main = Label(app, text='Welcome Willkommen!', font=('Arial Bold', 50))
main.grid(row=10, column=0)
# Repair Order
repair_order_text = string
repair_order_label = Label(app, text='Repair Order',
                           font=('bold', 14), pady=20)
repair_order_label.grid(row=0, column=0, sticky=W)
repair_order_entry = Entry(app, textvariable=repair_order_text)
repair_order_entry.grid(row=0, column=1)

# VIN number
vin_number_text = string
vin_number_label = Label(app, text='VIN Number', font=('bold', 14))
vin_number_label.grid(row=0, column=2, sticky=W)
vin_number_entry = Entry(app, textvariable=vin_number_text)
vin_number_entry.grid(row=0, column=3)

# Part Description
part_desc_text = string
part_desc_label = Label(app, text='Parts Description', font=('bold', 14))
part_desc_label.grid(row=1, column=1, sticky=W)
part_desc_entry = Entry(app, textvariable=part_desc_text)
part_desc_entry.grid(row=1, column=2)

# Price
price_text = string
price_label = Label(app, text='Price', font=('bold', 14))
price_label.grid(row=1, column=3, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=4)

# Parts Quantity
part_quantity_number = number
combo['values'] = (1, 2, 4, 5, 6, 7, 8, 9, 10, 'Text')
combo.current(1)
combo.grid(row=1, column=0)

# Parts List (Listbox)
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add Part', bg='green', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Part', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Part', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

app.title('BMW Technician Parts Request Manager')
app.geometry('700x350')

# Populate data
populate_list()

# Start program
app.mainloop()


# To create an executable, install pyinstaller and run
# '''
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py
# '''

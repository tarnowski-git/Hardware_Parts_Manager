import tkinter as tk
from tkinter import Frame, messagebox, StringVar, Label, Entry, Listbox, Scrollbar, Button
from db import Database

# Instanciate databse object
db = Database("store.db")


class MainApplication(tk.Frame):
    """Main class of application"""

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.selected_item = 0  # Init selected item var
        self.configure_gui()
        self.create_widgets()
        self.setup_layout()

    def configure_gui(self):
        """Setting general configurations of the application"""
        self.master.title("Hardware Manager")
        self.master.geometry("700x350")

    def create_widgets(self):
        """Creating the widgets of the application"""
        # Part
        self.part_text = StringVar()
        self.part_label = Label(
            self.master, text="Part Name", font=("bold", 14), pady=20)
        self.part_entry = Entry(self.master, textvariable=self.part_text)
        # Customer
        self.customer_text = StringVar()
        self.customer_label = Label(
            self.master, text="Customer", font=("bold", 14))
        self.customer_entry = Entry(
            self.master, textvariable=self.customer_text)
        # Retailer
        self.retailer_text = StringVar()
        self.retailer_label = Label(
            self.master, text="Retailer", font=("bold", 14))
        self.retailer_entry = Entry(
            self.master, textvariable=self.retailer_text)
        # Price
        self.price_text = StringVar()
        self.price_label = Label(self.master, text="Price", font=("bold", 14))
        self.price_entry = Entry(self.master, textvariable=self.price_text)
        # Part List (ListBox)
        self.parts_list = Listbox(self.master, height=8, width=100, border=0)
        # Create scrollbar
        self.scrollbar = Scrollbar(self.master)
        # Buttons
        self.add_btn = Button(self.master, text="Add Part",
                              width=12, command=self.add_item)
        self.remove_btn = Button(self.master, text="Remove Part",
                                 width=12, command=self.remove_item)
        self.update_btn = Button(self.master, text="Update Part",
                                 width=12, command=self.update_item)
        self.clear_btn = Button(self.master, text="Clear Input",
                                width=12, command=self.clear_text)

    def setup_layout(self):
        """Setup grid system"""
        self.part_label.grid(row=0, column=0, sticky=tk.W)
        self.part_entry.grid(row=0, column=1)
        self.customer_label.grid(row=0, column=2, sticky=tk.W)
        self.customer_entry.grid(row=0, column=3)
        self.retailer_label.grid(row=1, column=0, sticky=tk.W)
        self.retailer_entry.grid(row=1, column=1)
        self.price_label.grid(row=1, column=2, sticky=tk.W)
        self.price_entry.grid(row=1, column=3)
        self.parts_list.grid(row=3, column=0, columnspan=4,
                             rowspan=6, pady=20, padx=20)
        self.scrollbar.grid(row=3, column=4, rowspan=6, sticky=tk.N+tk.S)
        self.add_btn.grid(row=2, column=0, pady=20)
        self.remove_btn.grid(row=2, column=1)
        self.update_btn.grid(row=2, column=2)
        self.clear_btn.grid(row=2, column=3)

    def bind_widgets(self):
        # Set scroll to listbox
        self.scrollbar.configure(command=self.parts_list.yview)
        self.parts_list.configure(yscrollcommand=self.scrollbar.set)
        # Bind select
        self.parts_list.bind("<<ListboxSelect>>", self.select_item)

    def add_item(self):
        pass

    def remove_item(self):
        pass

    def update_item(self):
        pass

    def clear_text(self):
        pass

    def select_item(self):
        pass


# def populate_list():
#     parts_list.delete(0, END)
#     for row in db.fetch():
#         parts_list.insert(END, row)
# def add_item():
#     if part_text.get() == "" or customer_text.get() == "" or retailer_text.get() == "" or price_text.get() == "":
#         messagebox.showerror("Required Fields", "Please include all fields")
#         return None
#     db.insert(part_text.get(), customer_text.get(),
#               retailer_text.get(), price_text.get())
#     parts_list.delete(0, END)
#     parts_list.insert(END, (part_text.get(), customer_text.get(),
#                             retailer_text.get(), price_text.get()))
#     clear_text()
#     populate_list()
# def select_item(event):
#     try:
#         global selected_item
#         index = parts_list.curselection()[0]
#         selected_item = parts_list.get(index)
#         part_entry.delete(0, END)
#         part_entry.insert(END, selected_item[1])
#         customer_entry.delete(0, END)
#         customer_entry.insert(END, selected_item[2])
#         retailer_entry.delete(0, END)
#         retailer_entry.insert(END, selected_item[3])
#         price_entry.delete(0, END)
#         price_entry.insert(END, selected_item[4])
#     except IndexError:
#         pass
# def remove_item():
#     db.remove(selected_item[0])
#     clear_text()
#     populate_list()
# def update_item():
#     db.update(selected_item[0], part_text.get(), customer_text.get(),
#               retailer_text.get(), price_text.get())
#     populate_list()
# def clear_text():
#     part_entry.delete(0, END)
#     customer_entry.delete(0, END)
#     retailer_entry.delete(0, END)
#     price_entry.delete(0, END)
#     parts_list.select_clear(0, END)


# ensure a consistent GUI size
# app.grid_propagate(False)


# Populate data
# populate_list()
# populate_list()


root = tk.Tk()
# Create window object
app = MainApplication(master=root)

# Start program
app.mainloop()

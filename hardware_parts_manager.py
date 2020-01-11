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
        self.configure_gui()
        self.create_widgets()
        self.setup_layout()
        self.bind_widgets()
        # Init selected item var
        self.selected_item = 0
        # Populate initial list
        self.populate_list()

    def configure_gui(self):
        """Setting general configurations of the application"""
        self.master.title("Hardware Manager")
        self.master.geometry("700x350")
        self.master.resizable(0, 0)

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
        """Binding widgets when it needed"""
        # Set scroll to listbox
        self.scrollbar.configure(command=self.parts_list.yview)
        self.parts_list.configure(yscrollcommand=self.scrollbar.set)
        # Bind select
        self.parts_list.bind("<<ListboxSelect>>", self.select_item)

    def populate_list(self):
        """Delete items before update. So when you keep pressing
        it doesnt keep getting (pretending by calling this twice)"""
        self.parts_list.delete(0, tk.END)
        # Loop through records
        for row in db.fetch():
            self.parts_list.insert(tk.END, row)

    def select_item(self, event):
        """Runs when some item in the Listbox is selected"""
        try:
            # Get index
            index = self.parts_list.curselection()[0]
            # Get selected item
            self.selected_item = self.parts_list.get(index)
            # Add text to entries
            self.part_entry.delete(0, tk.END)
            self.part_entry.insert(tk.END, self.selected_item[1])
            self.customer_entry.delete(0, tk.END)
            self.customer_entry.insert(tk.END, self.selected_item[2])
            self.retailer_entry.delete(0, tk.END)
            self.retailer_entry.insert(tk.END, self.selected_item[3])
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(tk.END, self.selected_item[4])
        except IndexError:
            pass

    def add_item(self):
        """Add new item"""
        if self.part_text.get() == "" or self.customer_text.get() == "" or self.retailer_text.get() == "" or self.price_text.get() == "":
            messagebox.showerror(
                "Required Fields", "Please include all fields")
            return None
        # Insert into DB
        db.insert(self.part_text.get(), self.customer_text.get(),
                  self.retailer_text.get(), self.price_text.get())
        # Clear list
        self.parts_list.delete(0, tk.END)
        # Insert into list
        self.parts_list.insert(tk.END, (self.part_text.get(), self.customer_text.get(),
                                        self.retailer_text.get(), self.price_text.get()))
        self.clear_text()
        self.populate_list()

    def remove_item(self):
        """Remove selected item"""
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    def update_item(self):
        """Update selected item"""
        db.update(self.selected_item[0], self.part_text.get(), self.customer_text.get(),
                  self.retailer_text.get(), self.price_text.get())
        self.populate_list()

    def clear_text(self):
        """Clear all text fields"""
        self.part_entry.delete(0, tk.END)
        self.customer_entry.delete(0, tk.END)
        self.retailer_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.parts_list.select_clear(0, tk.END)



# Start program
if __name__ == '__main__':
    root = tk.Tk()
    app = MainApplication(master=root)
    app.mainloop()
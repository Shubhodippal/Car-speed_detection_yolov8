import tkinter as tk

def on_selection_change(*args):
    selected_item.set(var.get())
    print("Selected item:", selected_item.get())

# Create the main window
root = tk.Tk()
root.title("Dropdown Menu Example")

# Create a variable to store the selected item
selected_item = tk.StringVar()

# List of items for the drop-down menu
items = ["Item 1", "Item 2", "Item 3", "Item 4"]

# Create a drop-down menu
var = tk.StringVar(root)
var.set(items[0])  # Set the default item
dropdown_menu = tk.OptionMenu(root, var, *items, command=on_selection_change)
dropdown_menu.pack(padx=20, pady=20)

# Button to get the selected item
selected_button = tk.Button(root, text="Get Selected Item", command=lambda: print("Button Clicked: ", selected_item.get()))
selected_button.pack(padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()

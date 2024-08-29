from currency_converter import CurrencyConverter
import tkinter as tk

# Initialize the CurrencyConverter
c = CurrencyConverter()

# Create the main window
window = tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")

def clicked():
    amount = int(entry1.get())
    cur1 = entry2.get()
    cur2 = entry3.get()
    data = c.convert(amount, cur1, cur2)
    label4 = tk.Label(window, text=data, font=("Segoe Script", 20, "bold"))
    label4.place(x=200, y=300)

# Add a label with the correct font specification and place it
label = tk.Label(window, text="Currency Converter", font=("Segoe Script", 20, "bold"))
label.place(x=120, y=40)

label1 = tk.Label(window, text="Enter amount here: ", font=("Papyrus", 14, "bold"))
label1.place(x=70, y=100)

label2 = tk.Label(window, text="Enter your Currency here: ", font=("Papyrus", 14, "bold"))
label2.place(x=1, y=150)

label3 = tk.Label(window, text="Enter your desired Currency: ", font=("Papyrus", 14, "bold"))
label3.place(x=1, y=200)

# Correct placement of the button
button = tk.Button(window, text="Click", font=("Papyrus", 14, "bold"), command=clicked)
button.place(x=220, y=250)

# Create Entry widgets separately before placing them
entry1 = tk.Entry(window)
entry1.place(x=270, y=110)

entry2 = tk.Entry(window)
entry2.place(x=270, y=155)

entry3 = tk.Entry(window)
entry3.place(x=295, y=205)

# Start the Tkinter event loop
window.mainloop()

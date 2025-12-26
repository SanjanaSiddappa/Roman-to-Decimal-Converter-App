import tkinter as tk
from tkinter import messagebox

def roman_to_decimal(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = roman_numerals.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

def convert():
    roman = entry.get().upper()
    if not roman or any(ch not in "IVXLCDM" for ch in roman):
        messagebox.showerror("Error", "Invalid Roman numeral")
        return
    
    decimal = roman_to_decimal(roman)
    result_label.config(text=f"Decimal: {decimal}")

# Creating UI
root = tk.Tk()
root.title("Roman to Decimal Converter")
root.geometry("400x300")
root.configure(bg="pink")

frame = tk.Frame(root, bg="pink")
frame.pack(expand=True)

tk.Label(frame, text="Enter Roman Numeral:", fg="navy blue", font=("Gabriola", 24),bg="pink").pack(pady=10)
entry = tk.Entry(frame, font=("Times New Roman", 15), width=15)
entry.pack(pady=10)

tk.Button(frame, text="Convert", fg="darkgreen", bg="lightblue",font=("Comic Sans MS", 14), command=convert).pack(pady=10)

result_label = tk.Label(frame, text="Decimal:", font=("Times New Roman", 20), bg="pink")
result_label.pack(pady=10)

root.mainloop()

import tkinter as tk
from tkinter import ttk

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
    return result

def try_decryptions():
    output_box.delete("1.0", tk.END)  # Clear previous output

    text = input_entry.get()
    try:
        start_shift = int(shift_entry.get())
        if not (1 <= start_shift <= 25):
            raise ValueError
    except ValueError:
        output_box.insert(tk.END, "Please enter a valid shift number (1-25).")
        return

    for shift in range(start_shift, 26):
        decrypted = decrypt(text, shift)
        output_box.insert(tk.END, f"Shift {shift:2}: {decrypted}\n")

# Setup GUI
root = tk.Tk()
root.title("Nicolaj's Enchryption/Decryption Tool")

tk.Label(root, text="Encrypted Message:").pack()
input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=5)

tk.Label(root, text="Start Shift Number (1-25):").pack()
shift_entry = tk.Entry(root, width=10)
shift_entry.pack(pady=5)

decrypt_button = ttk.Button(root, text="Try Decrypting", command=try_decryptions)
decrypt_button.pack(pady=10)

output_box = tk.Text(root, height=15, width=60)
output_box.pack()

root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Məhsul məlumatları (ad, qiymət)
products = [
    ("Alma", 1.6),
    ("Armud", 1.5),
    ("Banan", 3.0),
    ("Üzüm", 2.4),
    ("Şaftalı", 2.7),
    ("Nar", 1.9),
    ("Kivi", 2.5),
    ("Portağal", 2.3),
    ("Mango", 3.1),
    ("Ananas", 3.4)
]

# Pəncərə yaradılır
root = tk.Tk()
root.title("Məhsullar və Çəki ilə Qiymət ")

# Checkbutton-lar üçün dəyişənlər
check_vars = []
weight_entries = []

# Məhsulları siyahıya əlavə etmək
for i, (name, price) in enumerate(products):
    var = tk.IntVar()
    chk = tk.Checkbutton(root, text=name, variable=var)
    chk.grid(row=i, column=0, sticky='w')
    check_vars.append((var, name, price))

    weight_entry = tk.Entry(root, width=5)
    weight_entry.grid(row=i, column=1)
    weight_entry.insert(0, "1")
    weight_entries.append(weight_entry)

# Qiymətləri göstərmək üçün funksiya
def show_prices():
    info = ""
    for var, name, price in check_vars:
        info += f"{name}: {price} AZN / kq\n"
    messagebox.showinfo("Məhsulların Qiymətləri", info)

# Ümumi qiyməti hesablayan funksiya
def calculate_total(event=None):
    total = 0
    for i, (var, name, price) in enumerate(check_vars):
        if var.get():
            try:
                weight = float(weight_entries[i].get())
                total += price * weight
            except ValueError:
                messagebox.showerror("Xəta", f"{name} üçün çəkini düzgün daxil et!")
                return
    messagebox.showinfo("Ümumi Qiymət", f"Ümumi məbləğ: {round(total, 2)} AZN")
# Price düyməsi
price_btn = tk.Button(root, text="Price", command=show_prices)
price_btn.grid(row=0, column=2, padx=10)

# Klaviaturadan Enter basılmasını izləmək
root.bind('<Return>', calculate_total)

root.mainloop()
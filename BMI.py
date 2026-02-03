import tkinter as tk
from tkinter import messagebox
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        weight_unit = weight_unit_var.get()
        if weight_unit == "kg":
            weight_kg = weight
        else: 
            weight_kg = weight * 0.453592
        height_unit = height_unit_var.get()
        if height_unit == "cm":
            height_cm = float(entry_height_cm.get())
            height_m = height_cm / 100
        else:
            feet = float(entry_height_ft.get())
            inches = float(entry_height_in.get())
            height_m = ((feet * 12) + inches) * 0.0254
        bmi = round(weight_kg / (height_m ** 2), 2)
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        label_result.config(text=f"BMI: {bmi} ({category})")
    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numeric values")
def clear_fields():
    entry_weight.delete(0, tk.END)
    entry_height_cm.delete(0, tk.END)
    entry_height_ft.delete(0, tk.END)
    entry_height_in.delete(0, tk.END)
    label_result.config(text="")
def toggle_height_fields(*args):
    if height_unit_var.get() == "cm":
        frame_cm.grid()
        frame_ft_in.grid_remove()
    else:
        frame_ft_in.grid()
        frame_cm.grid_remove()
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")
height_unit_var = tk.StringVar(value="cm")
height_unit_var.trace("w", toggle_height_fields)
tk.Label(root, text="Height Unit").grid(row=0, column=0, pady=5)
tk.OptionMenu(root, height_unit_var, "cm", "ft+in").grid(row=0, column=1)
frame_cm = tk.Frame(root)
tk.Label(frame_cm, text="Height (cm)").grid(row=0, column=0)
entry_height_cm = tk.Entry(frame_cm)
entry_height_cm.grid(row=0, column=1)
frame_cm.grid(row=1, column=0, columnspan=2)
frame_ft_in = tk.Frame(root)
tk.Label(frame_ft_in, text="Feet").grid(row=0, column=0)
entry_height_ft = tk.Entry(frame_ft_in, width=5)
entry_height_ft.grid(row=0, column=1)
tk.Label(frame_ft_in, text="Inches").grid(row=0, column=2)
entry_height_in = tk.Entry(frame_ft_in, width=5)
entry_height_in.grid(row=0, column=3)
frame_ft_in.grid(row=1, column=0, columnspan=2)
frame_ft_in.grid_remove()
tk.Label(root, text="Weight").grid(row=2, column=0, pady=5)
entry_weight = tk.Entry(root)
entry_weight.grid(row=2, column=1)
weight_unit_var = tk.StringVar(value="kg")
tk.OptionMenu(root, weight_unit_var, "kg", "lb").grid(row=2, column=2)
tk.Button(root, text="Calculate BMI", command=calculate_bmi)\
    .grid(row=3, column=0, columnspan=3, pady=10)
tk.Button(root, text="Clear", command=clear_fields)\
    .grid(row=4, column=0, columnspan=3)
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.grid(row=5, column=0, columnspan=3, pady=15)
root.mainloop()

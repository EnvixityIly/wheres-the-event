import tkinter as tk

root = tk.Tk()
root.title("Inches to Cm calculator")
root.geometry("400x400")
root.configure(bg="#000000")

def convertertocm():
    cm = float(entry.get()) *2.54
    result_label.config(text=str(cm)+"cm")

instruction_label = tk.Label(root,text="Enter length in inches:",font=("Algerian", 20, "bold"), fg = "black")
instruction_label.pack(pady=20)

entry = tk.Entry(root,font=("Arial", 16),width = 10)
entry.pack(pady=10)

convert_button = tk.Button(root,text="Convert",font=("Times New Roman", 15,"bold"), width = 20 , height = 2, bg = "#fff700", fg = "black", command = convertertocm)
convert_button.pack(pady=20)

result_label = tk.Label(root,text = "", font = ("Times New Roman", 15, "bold"))
result_label.pack(pady=20)

root.mainloop()
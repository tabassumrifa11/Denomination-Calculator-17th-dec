import tkinter as tk
import re

def check_password_strength():
    password = password_entry.get()
    length_criteria = len(password) >= 8
    digit_criteria = bool(re.search(r"\d", password))
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    symbol_criteria = bool(re.search(r"[!@#$%^&*().,?\":{}<>|]", password))
    
    criteria_met = sum([length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, symbol_criteria])
    
    if criteria_met <= 2:
        strength = "Weak"
    elif criteria_met == 3 or criteria_met == 4:
        strength = "Medium"
    else:
        strength = "Strong"
        
    result_label.config(text=f"Password Strength = {strength}", fg="#007BFF")
    
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

password_label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
password_label.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength, bg="#1E88E5", fg="#FFFFFF", font=("Arial", 12))
check_button.pack(pady=10)

password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack(pady=5)


result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
import tkinter as tk
import secrets
import string

def generate_password():
    length = length_var.get()
    chars = string.ascii_letters + string.digits + ('!@#$%^&*()-_=+[]{}|;:\'",.<>?/' if include_symbols.get() else '')
    password = ''.join(secrets.choice(chars) for _ in range(length))
    output.config(state='normal')
    output.delete(0, tk.END)
    output.insert(0, password)
    output.config(state='readonly')

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output.get())

root = tk.Tk()
root.title("パスジェネ1.0")

output = tk.Entry(root, width=50, state='readonly', justify='center')
output.pack(pady=5)
frame = tk.Frame(root)
frame.pack()
tk.Label(frame, text="桁数:").pack(side='left')
length_var = tk.IntVar(value=18)
tk.Entry(frame, textvariable=length_var, width=5).pack(side='left')
include_symbols = tk.BooleanVar(value=True)
tk.Checkbutton(frame, text="記号", variable=include_symbols).pack(side='left')
tk.Button(frame, text="生成", command=generate_password).pack(side='left')
tk.Button(frame, text="コピー", command=copy_to_clipboard).pack(side='left')
tk.Label(root, text="桁数と記号の有無を決め、生成を押下。\nPythonのsecrets使用。\n© 2024/06/08 hiko & ChatGPT (GPT-4o)").pack()

root.mainloop()

import tkinter as tk

def submit():
    nome = nome_entry.get()
    email = email_entry.get()

    print("Nome: ", nome)
    print("Email: ", email)

root = tk.Tk()
root.title("Formulário de Inscrição")

frame = tk.Frame(root)
frame.pack(padx=50, pady=20)

nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1)

email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1)

submit_button = tk.Button(frame, text="Submeter", command=submit)
submit_button.grid(row=2, columnspan=2, pady=10)

root.mainloop()
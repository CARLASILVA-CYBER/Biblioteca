import tkinter as tk
import pymysql

# Configuração de Conexão ao MySQL
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="biblioteca"
)

def listar_livros():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    books = cursor.fetchall()
    for book in books:
        print(f"{book[1]} by {book[2]}")

root = tk.Tk()
root.title("Administração da Biblioteca")

btn_listar = tk.Button(root, text="Listar Livros", command=listar_livros)
btn_listar.pack()

root.mainloop()

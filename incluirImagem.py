from tkinter.filedialog import askopenfilename
from psycopg2 import OperationalError
from tkinter import messagebox

def alteraIMG(conexao, IDALUNO):
    try:
        caminho = askopenfilename()
        cursor = conexao.cursor()
        query = f"""UPDATE alunos SET local_image = '{caminho}' WHERE id_aluno = '{IDALUNO}'"""
        cursor.execute(query)
        conexao.commit()
        cursor.close()
    except OperationalError as e:
        messagebox.showwarning(message=f"{e}")

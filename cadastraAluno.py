from psycopg2 import OperationalError
from tkinter import messagebox

def cadastrar(conexao, Nome_completo_btn, Data_nasc_btn, Nome_pai_btn, Nome_mae_btn, Endereco_btn, Bairro_btn, Data_inicio_btn):
    try:
        cursor = conexao.cursor()
        query = f"""INSERT INTO alunos
VALUES (DEFAULT, '{Nome_completo_btn}', 
'{Data_nasc_btn[6:10]}{Data_nasc_btn[3:5]}{Data_nasc_btn[0:2]}', 
'{Nome_pai_btn}', 
'{Nome_mae_btn}', 
'{Endereco_btn}', 
'{Bairro_btn}', 
'{Data_inicio_btn[6:10]}{Data_inicio_btn[3:5]}{Data_inicio_btn[0:2]}')"""
        cursor.execute(query)
        conexao.commit()
        cursor.close()
    except OperationalError as e:
        messagebox.showwarning(message=f"{e}")
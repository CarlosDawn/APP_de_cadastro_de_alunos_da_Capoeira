from psycopg2 import OperationalError
from tkinter import messagebox

def alterarAluno(conexao, Nome_completo_btn, Data_nasc_btn, Nome_pai_btn, Nome_mae_btn, Endereco_btn, Bairro_btn, Data_inicio_btn, nome):
    cursor = conexao.cursor()
    try:
        queryAltera = f"""UPDATE alunos SET nome_completo = '{Nome_completo_btn}', 
data_nasc = '{Data_nasc_btn[6:10]}{Data_nasc_btn[3:5]}{Data_nasc_btn[0:2]}',
nome_pai = '{Nome_pai_btn}', nome_mae = '{Nome_mae_btn}',
endereco = '{Endereco_btn}', bairro =  '{Bairro_btn}',
data_inicio = '{Data_inicio_btn[6:10]}{Data_inicio_btn[3:5]}{Data_inicio_btn[0:2]}' WHERE id_aluno = '{nome}'"""
        cursor.execute(queryAltera)
        conexao.commit()
        cursor.close()
    except OperationalError as e:
        messagebox.showwarning(message=f"{e}")

def excluir(conexao, nome):
    cursor = conexao.cursor()
    try:
        queryExclui = f"DELETE FROM alunos WHERE id_aluno = '{nome}'"
        cursor.execute(queryExclui)
        conexao.commit()
        cursor.close()
    except OperationalError as e:
        messagebox.showwarning(message=f"{e}")
from tkinter import *

def Buscar(cursor, nome_aluno_btn, lb_Lista):
    if (nome_aluno_btn == ''):
        lb_Lista.delete(0, 'end')
        queryAll = f"""select * from alunos
        order by nome_completo;"""
        cursor.execute(queryAll)
        allRegistros = cursor.fetchall()

        listaALL = []

        for registro in allRegistros:
            listaALL.append(f"{registro[0]}{' ' * 25}{registro[1]} | Bairro: {registro[6]}")
        for registro_lista in listaALL:
            lb_Lista.insert(END, registro_lista)

    else:
        lb_Lista.delete(0, 'end')
        query = f"""select * from public.alunos;"""
        cursor.execute(query)
        registros = cursor.fetchall()

        lista = []

        for registro in registros:
            for nome in registro[1].split():
                if nome_aluno_btn.get().lower() in nome.lower():
                    lista.append(f"{registro[0]}{' ' * 25}{registro[1]} | Bairro: {registro[6]}")
        for registro_lista in lista:
            lb_Lista.insert('end', registro_lista)

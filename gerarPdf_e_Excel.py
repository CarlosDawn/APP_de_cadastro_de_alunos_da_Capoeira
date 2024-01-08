from psycopg2 import OperationalError
from tkinter import messagebox
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def gerarListaExcel(conexao):
    try:
        writer = pd.ExcelWriter('ListaDeAlunos/Alunos.xlsx', engine="xlsxwriter")
        workbook = writer.book
        ws = workbook.add_worksheet('Alunos')

        formataCabeca = workbook.add_format({
            'font_color': 'white',
            'font_size': 11,
            'bg_color': '#228B22',
            'align': 'center',
            'valign': 'vcenter',
            'font_name': 'Gill Sans MT',
            'bold': True,
            'text_wrap': True
        })

        formataLinha = workbook.add_format({
            'font_name': 'Gill Sanas MT',
            'font_size': 10,
            'bg_color': '#E4E4E4',
            'font_color': '#000000',
            'valign': 'vcenter',
            'align': 'center'
        })

        formataLinha2 = workbook.add_format({
            'font_name': 'Gill Sanas MT',
            'font_size': 10,
            'bg_color': '#C0C0C0',
            'font_color': '#000000',
            'valign': 'vcenter',
            'align': 'center'
        })

        merge_format = workbook.add_format(
            {
                "fg_color": "#00bf63",
            }
        )

        ws.set_column("A:A", 9)
        ws.set_column("B:B", 28)
        ws.set_column("C:C", 13)
        ws.set_column("D:G", 28)
        ws.set_column("H:H", 13)

        ws.merge_range("A1:H12", "", merge_format)
        ws.insert_image("B1", "Imagem_FORM/imgexcel.png", {"x_scale": 0.94, "y_scale": 0.81})

        listaCabecalho = ["Codigo", "Nome Completo", "Data de Nasc.", "Nome do Pai", "Nome da Mãe", "Endereço",
                          "Bairro",
                          "Data de Inicio"]
        for num_colum, cel in enumerate(listaCabecalho):
            ws.write(12, num_colum, cel, formataCabeca)

        cursor = conexao.cursor()
        try:
            query = f"""select * from public.alunos"""
            cursor.execute(query)
            conexao.commit()
        except OperationalError as e:
            messagebox.showwarning(message=f"{e}")

        listaRegistro = cursor.fetchall()

        linha = 13
        coluna = 0

        for registro in listaRegistro:
            for valor in registro:
                if linha % 2 == 0:
                    ws.write(linha, coluna, valor, formataLinha)
                else:
                    ws.write(linha, coluna, valor, formataLinha2)
                coluna += 1
            linha += 1
            coluna = 0

        linhaData = 13
        for registro in listaRegistro:
            if linhaData % 2 == 0:
                ws.write(linhaData, 2, f"{registro[2][6:8]}/{registro[2][4:6]}/{registro[2][0:4]}", formataLinha)
                ws.write(linhaData, 7, f"{registro[7][6:8]}/{registro[7][4:6]}/{registro[7][0:4]}", formataLinha)
            else:
                ws.write(linhaData, 2, f"{registro[2][6:8]}/{registro[2][4:6]}/{registro[2][0:4]}", formataLinha2)
                ws.write(linhaData, 7, f"{registro[7][6:8]}/{registro[7][4:6]}/{registro[7][0:4]}", formataLinha2)
            linhaData += 1
        writer.close()
        messagebox.showinfo(message="Lista Gerada com Sucesso")
    except OperationalError as e:
        messagebox.showwarning(message=f"{e}")


def gerarFormularioPDF(id, conexao):
    cursor = conexao.cursor()
    try:
        query = f"""select * from public.alunos where id_aluno = '{id.strip().split()[0]}'"""
        cursor.execute(query)
    except OperationalError as e:
        messagebox.showwarning(message=f"{e}")

    listaRegistro = cursor.fetchone()

    try:
        doc = canvas.Canvas(f"Alunos/Formulario_{id.strip().split()[1]}.pdf", pagesize=A4)
        doc.drawImage("Imagem_FORM/imgform.png", 0, 0, width=590, height=880)
        doc.drawString(160, 563, f"{listaRegistro[1]}")
        doc.drawString(190, 523, f"{listaRegistro[2][6:8]}/{listaRegistro[2][4:6]}/{listaRegistro[2][0:4]}")
        doc.drawString(160, 483, f"{listaRegistro[3]}")
        doc.drawString(160, 443, f"{listaRegistro[4]}")
        doc.drawString(160, 403, f"{listaRegistro[5]}")
        doc.drawString(160, 363, f"{listaRegistro[6]}")
        doc.drawString(160, 323, f"{listaRegistro[7][6:8]}/{listaRegistro[7][4:6]}/{listaRegistro[7][0:4]}")
        doc.save()
        messagebox.showinfo(message="Formulario Criado com Sucesso")
    except OperationalError as e:
        messagebox.showwarning(message=f"{e}")

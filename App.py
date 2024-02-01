from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import ttkbootstrap as tb
import psycopg2 as conector
from psycopg2 import OperationalError
from datetime import date

from PIL import Image, ImageTk
#Aqui são importações de outros arquivos,
#tentei manter neste arquivo (AppACCEB.py) somente a parte de
#interassão com janelas tkinter, ja os outros arquivos fazem funções
#mais especificas.
import gerarPdf_e_Excel as gerarFile
import buscarAlunos
import cadastraAluno
import alteraEexcluiAluno

import incluirImagem


# Mostrar the window
def show(janela):
    janela.deiconify()


# Sumir com the window
def hide(janela):
    janela.withdraw()

def centralizarJanela(janela):
    janela.update_idletasks()

    width = janela.winfo_width()
    frm_width = janela.winfo_rootx() - janela.winfo_x()
    win_width = width + 2 * frm_width

    height = janela.winfo_height()
    titlebar_height = janela.winfo_rooty() - janela.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = janela.winfo_screenwidth() // 2 - win_width // 2
    y = janela.winfo_screenheight() // 2 - win_height // 2

    janela.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    janela.deiconify()

def areaAluno(nome, conexao, janela):
    hide(janela)

    janelaAreaAluno = Toplevel()
    janelaAreaAluno["bg"] = "#87CEEB"
    janelaAreaAluno.geometry("910x580")
    centralizarJanela(janelaAreaAluno)

    cursor = conexao.cursor()
    try:
        query = f"""select * from public.alunos where id_aluno = '{nome.strip().split()[0]}'"""
        cursor.execute(query)
    except OperationalError as e:
        messagebox.showwarning(message=f"{e}")

    #Apos a execução do comando query, é feito um fetchone para pegar o registro
    #de acordo com o id que foi passado na variavel nome
    listaRegistro = cursor.fetchone()

    title_l = Label(janelaAreaAluno, text="ACCEB | ESCRAVOS BRANCOS", font=("calibri 35 bold"), background="#87CEEB")
    title_l.place(x=160, y=30)

    demarc_l = Label(janelaAreaAluno, text="************************************************************",
                     foreground="#008000", background="#87CEEB",
                     font=("times 15"))
    demarc_l.place(x=160, y=title_l.winfo_reqheight() + 37)

    #Esse formulario abaixo sera preenchido automaticamento com os dados do registro
    #do id passado pela variavel nome, podendo ser alterados os dados manualmente e salvando
    #ao clicar no botão alterar.
    Nome_completo_lbl = Label(janelaAreaAluno, text="Nome Completo", font=("calibri 15"), background="#87CEEB")
    Nome_completo_lbl.place(x=50, y=title_l.winfo_reqheight() + 95)

    Data_nasc_lbl = Label(janelaAreaAluno, text="Data de Nascimento", font=("calibri 15"), background="#87CEEB")
    Data_nasc_lbl.place(x=50, y=title_l.winfo_reqheight() + 140)

    Nome_pai_lbl = Label(janelaAreaAluno, text="Nome do Pai", font=("calibri 15"), background="#87CEEB")
    Nome_pai_lbl.place(x=50, y=title_l.winfo_reqheight() + 188)

    Nome_mae_lbl = Label(janelaAreaAluno, text="Nome da Mãe", font=("calibri 15"), background="#87CEEB")
    Nome_mae_lbl.place(x=50, y=title_l.winfo_reqheight() + 240)

    Endereco_lbl = Label(janelaAreaAluno, text="Endereço", font=("calibri 15"), background="#87CEEB")
    Endereco_lbl.place(x=50, y=title_l.winfo_reqheight() + 284)

    Bairro_lbl = Label(janelaAreaAluno, text="BAIRRO", font=("calibri 15"), background="#87CEEB")
    Bairro_lbl.place(x=50, y=title_l.winfo_reqheight() + 330)

    Data_inicio_lbl = Label(janelaAreaAluno, text="Data de Inicio", font=("calibri 15"), background="#87CEEB")
    Data_inicio_lbl.place(x=50, y=title_l.winfo_reqheight() + 370)

    Nome_completo_btn = Entry(janelaAreaAluno, font=("calibri 15"), width=35)
    Nome_completo_btn.insert(0, f"{listaRegistro[1]}")
    Nome_completo_btn.place(x=230, y=title_l.winfo_reqheight() + 92)

    janelaAreaAluno.title(f"{listaRegistro[1]}")

    #Quando o valor de variaveis com datas são pegos, os dados estão em ordem diferente,
    #e tambem por virem de um DateList a forma como são tratados é diferente para funcionar.
    dataNascAno = int(listaRegistro[2][0:4])
    dataNascMes = int(listaRegistro[2][4:6])
    dataNascDia = int(listaRegistro[2][6:8])

    Data_nasc_btn = tb.DateEntry(janelaAreaAluno, bootstyle="danger",
                                 startdate=date(dataNascAno, dataNascMes, dataNascDia))
    Data_nasc_btn.place(x=230, y=title_l.winfo_reqheight() + 138)

    Nome_pai_btn = Entry(janelaAreaAluno, font=("calibri 15"), width=35)
    Nome_pai_btn.insert(0, f"{listaRegistro[3]}")
    Nome_pai_btn.place(x=230, y=title_l.winfo_reqheight() + 185)

    Nome_mae_btn = Entry(janelaAreaAluno, font=("calibri 15"), width=35)
    Nome_mae_btn.insert(0, f"{listaRegistro[4]}")
    Nome_mae_btn.place(x=230, y=title_l.winfo_reqheight() + 235)

    Endereco_btn = Entry(janelaAreaAluno, font=("calibri 15"), width=35)
    Endereco_btn.insert(0, f"{listaRegistro[5]}")
    Endereco_btn.place(x=230, y=title_l.winfo_reqheight() + 280)

    Bairro_btn = Entry(janelaAreaAluno, font=("calibri 15"), width=35)
    Bairro_btn.insert(0, f"{listaRegistro[6]}")
    Bairro_btn.place(x=230, y=title_l.winfo_reqheight() + 325)

    dataInicAno = int(listaRegistro[7][0:4])
    dataInicMes = int(listaRegistro[7][4:6])
    dataInicDia = int(listaRegistro[7][6:8])

    Data_inicio_btn = tb.DateEntry(janelaAreaAluno, bootstyle="danger",
                                   startdate=date(dataInicAno, dataInicMes, dataInicDia))
    Data_inicio_btn.place(x=230, y=title_l.winfo_reqheight() + 370)

    if listaRegistro[8] != " ":
        imagem = Image.open(r"{}".format(listaRegistro[8]))
    else:
        caminho = r"C:\Users\lembr\OneDrive\Imagens\9-94702_user-outline-icon-clipart-png-download-profile-icon.png"
        imagem = Image.open(r"{}".format(caminho))
    resizeimg = imagem.resize((130, 180))
    img = ImageTk.PhotoImage(resizeimg)
    LabelImg = Label(janelaAreaAluno, image = img)
    LabelImg.image = img
    LabelImg.place(x=680, y=title_l.winfo_reqheight() + 108)

    Altera_img = Button(janelaAreaAluno, text=("ALTERAR"), width=15, command=lambda : incluirImagem.alteraIMG(conexao, listaRegistro[0]))
    Altera_img.place(x=690, y=title_l.winfo_reqheight() + 295)

    def janelaExcluirAluno():
        janelaExcluir = Tk()
        janelaExcluir["bg"] = "sky blue"
        janelaExcluir.geometry("360x120")
        janelaExcluir.title("EXCLUIR")
        centralizarJanela(janelaExcluir)

        lbl_pergunta = Label(janelaExcluir, text="TEM CERTEZA QUE QUE DESEJA EXCLUIR ESTE CADASTRO",
                             font=("calibri 10 bold"), background="sky blue")
        lbl_pergunta.place(x=25, y=20)
        btn_sim = Button(janelaExcluir, text="SIM", command=lambda: [alteraEexcluiAluno.excluir(conexao, nome.strip().split()[0]), janelaExcluir.destroy(), janelaAreaAluno.destroy(), show(janela)])
        btn_nao = Button(janelaExcluir, text="NÃO", command=lambda: janelaExcluir.destroy())
        btn_sim.place(x=25, y=60)
        btn_nao.place(x=260, y=60)
        janelaExcluir.mainloop()

    Button_cad = Button(janelaAreaAluno, text="ALTERAR", width=27, command=lambda: alteraEexcluiAluno.alterarAluno(conexao,
                                                                                                Nome_completo_btn.get(),
                                                                                                Data_nasc_btn.entry.get(),
                                                                                                Nome_pai_btn.get(),
                                                                                                Nome_mae_btn.get(),
                                                                                                Endereco_btn.get(),
                                                                                                Bairro_btn.get(),
                                                                                                Data_inicio_btn.entry.get(), nome.strip().split()[0]))
    Button_cad.place(x=130, y=title_l.winfo_reqheight() + 430)

    Button_sair = Button(janelaAreaAluno, text="SAIR", width=27, command=lambda: [janelaAreaAluno.destroy(), show(janela)])
    Button_sair.place(x=360, y=title_l.winfo_reqheight() + 430)

    Button_delete = Button(janelaAreaAluno, text="EXCLUIR CADASTRO", width=27, command=lambda: janelaExcluirAluno())
    Button_delete.place(x=130, y=title_l.winfo_reqheight() + 470)

    Button_pdf = Button(janelaAreaAluno, text="GERAR FORMULARIO PDF", width=27,
                        command=lambda: gerarFile.gerarFormularioPDF(nome, conexao))
    Button_pdf.place(x=360, y=title_l.winfo_reqheight() + 470)

    janelaAreaAluno.mainloop()


def cadastrarAluno(conexao, janela):
    hide(janela)

    janelaCadastro = Toplevel()
    janelaCadastro["bg"] = "#87CEEB"
    janelaCadastro.geometry("680x580")
    janelaCadastro.title("CADASTRAR ALUNO")
    centralizarJanela(janelaCadastro)

    title_l = Label(janelaCadastro, text="ACCEB | ESCRAVOS BRANCOS", font=("calibri 35 bold"), background="#87CEEB")
    title_l.place(x=30, y=30)

    demarc_l = Label(janelaCadastro, text="************************************************************",
                     foreground="#008000", background="#87CEEB",
                     font=("times 15"))
    demarc_l.place(x=50, y=title_l.winfo_reqheight() + 37)

    #O formulario abaixo realiza o cadastro do registro no banco de daos
    #ao clicar no botão cadastrar.
    Nome_completo_lbl = Label(janelaCadastro, text="Nome Completo", font=("calibri 15"), background="#87CEEB")
    Nome_completo_lbl.place(x=50, y=title_l.winfo_reqheight() + 95)

    Data_nasc_lbl = Label(janelaCadastro, text="Data de Nascimento", font=("calibri 15"), background="#87CEEB")
    Data_nasc_lbl.place(x=50, y=title_l.winfo_reqheight() + 140)

    Nome_pai_lbl = Label(janelaCadastro, text="Nome do Pai", font=("calibri 15"), background="#87CEEB")
    Nome_pai_lbl.place(x=50, y=title_l.winfo_reqheight() + 188)

    Nome_mae_lbl = Label(janelaCadastro, text="Nome da Mãe", font=("calibri 15"), background="#87CEEB")
    Nome_mae_lbl.place(x=50, y=title_l.winfo_reqheight() + 240)

    Endereco_lbl = Label(janelaCadastro, text="Endereço", font=("calibri 15"), background="#87CEEB")
    Endereco_lbl.place(x=50, y=title_l.winfo_reqheight() + 284)

    Bairro_lbl = Label(janelaCadastro, text="Bairro", font=("calibri 15"), background="#87CEEB")
    Bairro_lbl.place(x=50, y=title_l.winfo_reqheight() + 330)

    Data_inicio_lbl = Label(janelaCadastro, text="Data de Inicio", font=("calibri 15"), background="#87CEEB")
    Data_inicio_lbl.place(x=50, y=title_l.winfo_reqheight() + 370)

    Nome_completo_btn = Entry(janelaCadastro, font=("calibri 15"), width=35)
    Nome_completo_btn.place(x=230, y=title_l.winfo_reqheight() + 92)

    Data_nasc_btn = tb.DateEntry(janelaCadastro, bootstyle="danger")
    Data_nasc_btn.place(x=230, y=title_l.winfo_reqheight() + 138)

    Nome_pai_btn = Entry(janelaCadastro, font=("calibri 15"), width=35)
    Nome_pai_btn.place(x=230, y=title_l.winfo_reqheight() + 185)

    Nome_mae_btn = Entry(janelaCadastro, font=("calibri 15"), width=35)
    Nome_mae_btn.place(x=230, y=title_l.winfo_reqheight() + 235)

    Endereco_btn = Entry(janelaCadastro, font=("calibri 15"), width=35)
    Endereco_btn.place(x=230, y=title_l.winfo_reqheight() + 280)

    Bairro_btn = Entry(janelaCadastro, font=("calibri 15"), width=35)
    Bairro_btn.place(x=230, y=title_l.winfo_reqheight() + 325)

    Data_inicio_btn = tb.DateEntry(janelaCadastro, bootstyle="danger")
    Data_inicio_btn.place(x=230, y=title_l.winfo_reqheight() + 370)

    #Esta função limpa o formulario apagando o que foi digitado
    #apos ser cadastrado o aluno e é selecionado o Entry do Nome Completo.
    def limpaForm():
        Nome_completo_btn.delete(0, 'end')
        Nome_pai_btn.delete(0, 'end')
        Nome_mae_btn.delete(0, 'end')
        Endereco_btn.delete(0, 'end')
        Bairro_btn.delete(0, 'end')
        Nome_completo_btn.focus()

    def sendAlunoData():
        if (Nome_completo_btn.get() == '') or (Nome_pai_btn.get() == '') or (Nome_mae_btn.get() == '') or (
                Endereco_btn.get() == '') or (Bairro_btn.get() == ''):
            messagebox.showinfo(message="Campo(s) Sem Valor")
        else:
            cadastraAluno.cadastrar(conexao,
                                    Nome_completo_btn.get(),
                                    Data_nasc_btn.entry.get(),
                                    Nome_pai_btn.get(), Nome_mae_btn.get(),
                                    Endereco_btn.get(), Bairro_btn.get(),
                                    Data_inicio_btn.entry.get())
            limpaForm()

    Button_cad = Button(janelaCadastro, text="CADASTRAR", width=23, command=lambda: sendAlunoData())
    Button_cad.place(x=230, y=title_l.winfo_reqheight() + 430)

    Button_sair = Button(janelaCadastro, text="SAIR", width=17, command=lambda: [janelaCadastro.destroy(), show(janela)])
    Button_sair.place(x=475, y=title_l.winfo_reqheight() + 430)
    janelaCadastro.mainloop()


global conexao

#A parte abaixo é feito a conexão com o banco de dados do postgreslq,
#as tabelas ja foram criadas antes no caso deste prjeto.
try:
    conexao = conector.connect(
        database="BD_Capoeira",
        user="postgres",
        password="Ryuri22@33",
        host="localhost",
        port="5434")
except OperationalError as e:
    messagebox.showwarning(message=f"{e}")

janelaConsulta = Tk()
janelaConsulta.geometry("1250x580")
janelaConsulta.title("ACCEB | ESCRAVOS BRANCOS")
centralizarJanela(janelaConsulta)

cursor = conexao.cursor()

title_l = Label(janelaConsulta, text="ACCEB | ESCRAVOS BRANCOS", font=("calibri 20 bold"), background="#87CEEB")
title_l.place(x=900, y=30)

title_tb = Label(janelaConsulta, text=f"Id{'_' * 8}Nome | Endereço", font=("calibri 20 bold"), background="#708090",
                 width=59)
title_tb.place(x=13, y=30)

nome_aluno_lbl = Label(janelaConsulta, text="Nome Do Aluno", font=("calibri 15 bold"), background="#87CEEB")
nome_aluno_lbl.place(x=990, y=title_l.winfo_reqheight() + 70)

nome_aluno_btn = Entry(janelaConsulta, font=("times 15"), width=25)
nome_aluno_btn.place(x=930, y=title_l.winfo_reqheight() + 105)

lb_Lista = Listbox(janelaConsulta, width=83, height=20, font=("calibri 15 bold"))
lb_Lista.place(x=10, y=title_l.winfo_reqheight() + 25)

janelaConsulta["bg"] = "sky blue"

#Esta função auxilia o ListBox para que seja pego
#o dados do registro selecionado na lista

def chamaAreaAluno(event):
    areaAluno(lb_Lista.get(ACTIVE), conexao, janelaConsulta)

#Adiciona a função acima ao dar dois clicks.
lb_Lista.bind('<Double-1>', chamaAreaAluno)

btn_escolha = Button(janelaConsulta, text="BUSCAR", width=25, command=lambda: buscarAlunos.Buscar(cursor, nome_aluno_btn.get(), lb_Lista))
btn_escolha.place(x=980, y=title_l.winfo_reqheight() + 150)

btn_lista = Button(janelaConsulta, text="GERAR LISTA", width=15, command=lambda: gerarFile.gerarListaExcel(conexao))
btn_lista.place(x=1010, y=title_l.winfo_reqheight() + 460)

btn_cadastrar = Button(janelaConsulta, text="CADASTRAR", width=15, command=lambda: cadastrarAluno(conexao, janelaConsulta))
btn_cadastrar.place(x=930, y=title_l.winfo_reqheight() + 500)

btn_sair = Button(janelaConsulta, text="SAIR", width=15, command=lambda: janelaConsulta.destroy())
btn_sair.place(x=1090, y=title_l.winfo_reqheight() + 500)

janelaConsulta.mainloop()

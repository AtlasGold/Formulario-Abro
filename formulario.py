from logging import exception
from PIL import Image
from os import write
import streamlit as st
from streamlit.type_util import Key 
import os
#from conexão.conexao import cnxn,cursor



#trocar o nome da pagina e o icone
st.set_page_config(page_title = "Abro - Odontologia Especializada",
    page_icon=":smiley:")

#remover o botão de Menu

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



#conexão com o banco
#import mysql.connector
#cnxn = mysql.connector.connect(host=st.secrets["host"], user=st.secrets["user"], passwd= st.secrets["passwd"], db= st.secrets["db"])
#cursor = cnxn.cursor()

import mysql.connector
cnxn = mysql.connector.connect(host=os.environ['host'], user=os.environ['user'], passwd= os.environ['passwd'], db= os.environ['db'])
cursor = cnxn.cursor()

#enviar os dados
    
def inserir(Nome,Telefone,CPF):
    cursor.execute('INSERT INTO cadastro(Nome,Telefone,CPF) VALUES (%s, %s, %s)',(Nome,Telefone,CPF))
    cnxn.commit()


def inserir_an(motivo,tratamento,medicamento,qmedicamentos,alergia,qalergias,anestesia,ultimo,canal,gengiva,fuma,sangra,dor,desmaio,gravida,procedimento,cpf,nome):
    cursor.execute("INSERT INTO anamnese1(`Qual O Motivo Da Consulta`,`Tratamento ou Problema de Saude`,`Está Tomando Algum Medicamento`,`Quais Medicamentos`,`Tem alergia a algum medicamento`,`Apresenta Alergia a Quais Medicamentos`,`Teve Alguma Reação a Anestesia Local`,`Quando Foi o Seu Ultimo Tratamento Odontologico`,`Tratamento de Canal Protese Implante Perdeu um Dente`,`Sua Gengiva Sangra Com Frequência`,`Voce Fuma`,`Quando Você se Corta Sangra Muito`,`Dores de Dente Cabeça Face Ouvido Articulações`,`Teve Algum Desmaio Ataques Nervoso Epilepsia ou Convulsoes`,`Pode Estar Gravida`,`Procedimento Facial Botox Preenchimento Hialurônico PMA`,`CPF`,`Nome`) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)",(motivo,tratamento,medicamento,qmedicamentos,alergia,qalergias,anestesia,ultimo,canal,gengiva,fuma,sangra,dor,desmaio,gravida,procedimento,cpf,nome))
    cnxn.commit()

def inserir_so(profissão,time,qtime,animal,qanimal,filho,nfilho,medo,sorriso,facebook,instagram,qinstagram,hobby,qhobby,ambiente,generom,programação, generof,cpf,nome):
    cursor.execute("INSERT INTO sociais(`Qual sua profissão ?`,`Gosta de Futebol ?`,`Times que torce`,`Tem algum animal de estimação`,`Qual animal?`,`Tem filhos ?`,`Como se chamam ?`,`Tem medo de dentista ?`,`Esta Satisfeito Com Sua Estética Facil e de Sorriso ?`,`Tem Facebook`,`Tem Instagram ?`,`Qual instagram ?`,`Tem algum Hobby ?`,`Quais hobbies?`,`Gosta de música ambiente ?`,`Qual Gênero/Ritmo Gosta de Ouvir ?`,`Qual Tipo De Programa De Televisão Gosta De Assistir ?`,`Qual Gênero De Filme Gosta ?`,`CPF`,`Nome`) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(profissão,time,qtime,animal,qanimal,filho,nfilho,medo,sorriso,facebook,instagram,qinstagram,hobby,qhobby,ambiente,generom,programação, generof,cpf,nome))
    cnxn.commit()



#receber os dados

st.title("Cadastro")
input_nome = st.text_input("Digite Seu Nome Completo")
input_telefone = st.text_input("Telefone Para Contato")
input_CPF = st.text_input("CPF")

   
col1, col2, col3 = st.columns(3)
image = Image.open('abbro.png')
col2.image(image, use_column_width=True)

st.title("Anamnese")
input_01 = st.text_input("Qual O Motivo Da Consulta ? ") 

input_02 = st.selectbox("Está Fazendo Algum Tratamento Médico ou Tem Algum Problema de Saúde ? ",["","Sim","Não"])

input_03 = st.selectbox("Está Tomando Algum Medicamento?",["","Sim","Não"])

if input_03 ==("Sim"):
     input_003 =st.text_input("Quais Medicamentos ?")
input_04 = st.selectbox("Tem Alergia a Algum Medicamento ?",["","Sim","Não"])
if input_04 ==("Sim"):
     input_004 = st.text_input("Apresenta Alergia a Quais Medicamentos ?")
input_05 = st.selectbox("Teve Alguma Reação a Anestesia Local ?",["","Sim","Não"])
input_06 = st.text_input("Quando Foi o Seu Ultimo Tratamento Odontológico ?")
input_006 = st.selectbox ("Já Realizou Tratamento de Canal ? Prótese ? Implante ? Perdeu Algum Dente ?",["","Sim","Não"])
input_07 = st.selectbox("Sua Gengiva Sangra Com Frequência ?",["","Sim","Não"])
input_08 = st.selectbox("Você Fuma ?",["","Sim","Não"])
input_09 = st.selectbox("Quando Você se Corta, Sangra Muito ?",["","Sim","Não"])
input_10 = st.selectbox("Sente Dores de Dente ? Cabeça ? Dores na Face ? Ouvido ou Articulações ?",["","Sim","Não"])
input_11 = st.selectbox("Teve Algum Desmaio, Ataques Nervoso, Epilepsia ou Convulsões ? ",["","Sim","Não"])
input_12 = st.selectbox("Pode Estar Gravida ?",["","Sim","Não"])
input_25 = st.selectbox("Já Realizou Algum Procedimento Estético Facial ? Botox? Preenchimento com Ac. Hialurônico ou PMA ?",["","Sim","Não"])


st.title("Sobre Você")
st.warning("Perguntas Opcionais")

input_13 = st.text_input("Qual Sua Profissão ?")
if input_13=="":
 input_13=("Não Informou")
input_14 = st.selectbox("Gosta de Futebol ?",["","Sim","Não"])
if input_14 == ("Sim") :
    input_014 = st.text_input("Para Quais Times Você Torce ?")
input_15 = st.selectbox("Tem Algum Animal De Estimação ?",["","Sim","Não"])
if input_15 == ("Sim"):
    input_015 = st.text_input("Qual ?")


input_16 = st.selectbox("Tem Filhos ?",["","Sim","Não"])
if input_16 == ("Sim"):
    input_0016 = st.text_input("Como se Chamam ?")


input_17 = st.selectbox("Tem Medo De Dentista ?",["","Sim","Não"])
if input_17=="":
 input_17=("Não Informou")

input_18 = st.selectbox("Esta Satisfeito Com Sua Estética Facil e de Sorriso ? ",["","Sim","Não"])
if input_18=="":
 input_18=("Não Informou")

input_19 = st.selectbox("Tem Facebook? ",["","Sim","Não"])
if input_19=="":
 input_19=("Não Informou")
input_20 = st.selectbox("Tem Instagram ?",["","Sim","Não"])

if input_20 == ("Sim"):
    input_020 = st.text_input("Qual?",key='chave')


input_21 = st.selectbox("Tem Algum Hobby ?",["","Sim","Não"])
if input_21 == ("Sim"):
    input_021 = st.text_input("Quais ?")

input_22 = st.selectbox ("Gosta De Musica Ambiente ? ",["","Sim","Não"])
if input_22 == ("Sim"):
    input_022 = st.text_input("Qual Gênero/Ritmo Gosta de Ouvir ?")

input_23 = st.text_input ("Qual Tipo De Programa De Televisão Gosta De Assistir ?")
if input_23=="":
 input_23=("Não Informou")

input_24 = st.text_input ("Qual Gênero De Filme Gosta ?")

#tirar a obrigatoriedade de responder os dados pessoais

if input_24=="":
 input_24=("")
if input_03 == 'Não':
        input_003 = 'Não'
if input_04 == 'Não':
        input_004 = 'Não'
if input_14 == 'Não':
        input_014 = 'Nenhum'
if input_14 == "":
    input_014=("Não Informou")
if input_15 == 'Não':
        input_015 = 'Nenhum'
if input_15 == "":
        input_015=("Não informou")
if input_16 == 'Não':
        input_0016 = 'Não tenho'
if input_16 == "":
        input_0016=("Não informou")
if input_20 == 'Não':
        input_020 = 'Não tenho'
if input_20 == "":
         input_020=("Não informou")
if input_21 == 'Não':
        input_021 = 'Não tenho'
if input_21 == "":
         input_021=("Não informou")
if input_22 == 'Não':
        input_022 = 'Não gosto'   
if input_22 == "":
        input_022=("Não informou")  




 

#botão de enviar    
try:                                               
 if st.button("Enviar"):
  inserir(input_nome,input_telefone,input_CPF)
  inserir_an(input_01,input_02,input_03,input_003,input_04,input_004,input_05,input_06,input_006,input_07,input_08,input_09,input_10,input_11,input_12,input_25,input_CPF,input_nome )
  inserir_so(input_13,input_14,input_014,input_15,input_015,input_16,input_0016,input_17,input_18,input_19,input_20,input_020,input_21,input_021,input_22,input_022,input_23,input_24,input_CPF,input_nome)
  if st.button == 0 : st.error("Certifique-se que enviou tudo!") 
  else: st.success('Tudo Certo !')
except:
    st.error("Algumas Informações Importantes Estão Faltando")

  


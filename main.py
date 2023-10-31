#!/usr/bin/python3
import requests                 #pip install requests
from bs4 import BeautifulSoup   #pip install bs4
import os
import datetime
import PySimpleGUIQt as sg # pip install PySimpleGUIQt

sg.theme("DarkGreen5")

layout = [[sg.Text("Suas informações nunca serão reutilizadas com este script, elas não serão salvas en nenhum banco de dados ou afins.", font=("Helvetica", 12, "italic"))],
    [sg.Text("Número do WhatsApp"),sg.InputText(key="phoneNumber")],
    [sg.Text("Número da API"),sg.InputText(key="apiKey")],
    [sg.Ok(), sg.Cancel()]
]

window = sg.Window("Bot WhatsApp News",layout)


while True:
    event, value = window.read()
    if event in (sg.WIN_CLOSED, "Cancel"):
        break
    else:
        PHONE_NUMBER = value["phoneNumber"]
        API_KEY = value["apiKey"]
        window.close()
def getNoticiasLog():
    if (os.path.exists('noticias.log.txt')):
        pass
    else:
        with open('noticias.log.txt', 'w') as arquivo:
            arquivo.write('Arquivo Criado\n')
            arquivo.close()
    
    with open('noticias.log.txt','r') as arquivo:
        ultimaLinha = arquivo.readlines()[-1]
        arquivo.close()
        return ultimaLinha



def getNoticia():
    reponse = requests.get("https://g1.globo.com/")

    pagina = BeautifulSoup(reponse.text,'html.parser')
    tituloNoticia = pagina.find('div',attrs={'class':'feed-post-header with-post-chapeu'})
    subtituloNoticia = pagina.find('div',attrs={'class':'feed-post-body-title gui-color-primary gui-color-hover'})
    linkHTML = pagina.find('a',attrs={'class':'feed-post-link gui-color-primary gui-color-hover'})
    link = linkHTML['href']
    horario = datetime.datetime.now().strftime("%H:%M:%S")
    noticia = {'titulo':tituloNoticia.text, 'subTitulo': subtituloNoticia.text, 'link': link, "Horario": horario}

    return noticia


def getUltimaNoticia(ultimaNoticiaLog, ultimaNoticia):
    if (ultimaNoticiaLog == ultimaNoticia):
        return False
    else:
        return True
def sendNoticia(noticia):
    if (noticia['subTitulo'] != ""):
        mensagem = f"*{noticia['titulo']}*\n_{noticia['subTitulo']}_\n\n{noticia['link']}"
    else:
        mensagem = f"*{noticia['titulo']}*\n\n{noticia['link']}"

    url=f"https://api.callmebot.com/whatsapp.php?phone={PHONE_NUMBER}&text={mensagem}&apikey={API_KEY}"

    try:
        requests.get(url)
        with open('noticias.log.txt','w') as arquivo:
            arquivo.write(f"{noticia['titulo']}")
            arquivo.close()
    except:
        with open('noticiasBot.log.txt','w') as arquivo:
            arquivo.write("Erro ao enviar Notícia.")
            arquivo.close


if (__name__ == "__main__"):
    ultimaNoticia = getNoticia()
    ultimaNoticiaLog = getNoticiasLog()
    flag = getUltimaNoticia(ultimaNoticiaLog,ultimaNoticia['titulo'])

    if(flag):
        sendNoticia(ultimaNoticia)

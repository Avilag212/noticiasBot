import requests                 #pip install requests
from bs4 import BeautifulSoup   #pip install bs4
import os

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
    
    noticia = {'titulo':tituloNoticia.text, 'subTitulo': subtituloNoticia.text, 'link': link}

    return noticia

def getUltimaNoticia(ultimaNoticiaLog, ultimaNoticia):
    if (ultimaNoticiaLog == ultimaNoticia):
        return True
    else:
        return False
    
def sendNoticia(noticia):
    PHONE_NUMBER = '' #Set your WhatsApp number / Coloque o seu número de WhatsApp aqui
    API_KEY = '' #Set your APIKEY of CallmeBot / Coloque o seu API Key do CallmeBot aqui
    
    if (noticia['subTitulo'] != ""):
        mensagem = f"*{noticia['titulo']}*\n_{noticia['subTitulo']}_\n\n{noticia['link']}"
    else:
        mensagem = f"*{noticia['titulo']}*\n\n{noticia['link']}"

    url=f"https://api.callmebot.com/whatsapp.php?phone={PHONE_NUMBER}&text={mensagem}&apikey={API_KEY}"

    try:
        requests.get(url)
        with open('noticias.log.txt','w') as arquivo:
            arquivo.write(f"{noticia['titulo']}\n")
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

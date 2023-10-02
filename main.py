#! /usr/bin/python3
import requests
from bs4 import BeautifulSoup
import os

def getNoticiasLog():
    noticiasLog = "noticias.log.txt"
    if os.path.exists(noticiasLog):
        return True
    else:
        return False

def createNoticiasLog():
    with open('noticias.log.txt', 'w') as arquivo:
        arquivo.write(f'Arquivo criado\n')
        arquivo.close()

def getUltimaNoticiaLog():
    with open('noticias.log.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()

        if conteudo:
            ultimaLinha = conteudo[-1]
            arquivo.close()
            return ultimaLinha
        else:
            ultimaLinha = "False-flag"
            arquivo.close()
            return ultimaLinha

def getUltimaNoticia(): #Retona string com a título da última noticia da home do G1
    response = requests.get("https://g1.globo.com/")
    pagina = BeautifulSoup(response.text, 'html.parser')
    post = pagina.find('div', attrs={'class': 'feed-post-body'})
    tituloNoticia = post.find('span',attrs={'class':'feed-post-header-chapeu'})
    
    return tituloNoticia.text
    
def getUltimaNoticiaContent(): #Retorna Dicionário com Título, sub-título(se houver) e link da noticia nova, pronta para o sendNoticia.
    conteudos = {}
    
    #Pega a página e transforma em objeto BeautifulSoup
    response = requests.get("https://g1.globo.com/")
    pagina = BeautifulSoup(response.text, 'html.parser')

    #Pega o post da primeira noticia
    post = pagina.find('div', attrs={'class': 'feed-post-body'})
    #Titulo da Noticia
    tituloNoticia = post.find('span',attrs={'class':'feed-post-header-chapeu'})
    conteudos['tituloNoticia'] = tituloNoticia.text
    #Subtitulo da Noticia
    subtituloNoticia = post.find('div', attrs={'class': 'feed-post-body-title gui-color-primary gui-color-hover' })
    if(subtituloNoticia): #Se tiver subtitulo adiciona no array de conteudo
        conteudos['subtituloNoticia'] = subtituloNoticia.text
    
    #Obtendo link da noticia
    textoLink = post.find('a', attrs={'class':'feed-post-link gui-color-primary gui-color-hover'})
    link = textoLink['href']
    conteudos['link'] = link
    #Formata conteúdo em string Unica
    # noticia = "".join(f'{conteudos}\n')
    
    return conteudos


def setNoticiasLog(tituloUltimaNoticia, tituloUltimaNoticiaLog):
    if(tituloUltimaNoticia == tituloUltimaNoticiaLog):
        return False
    else:
        with open('noticias.log.txt', 'a') as arquivo:
            arquivo.write(f'\n{tituloUltimaNoticia}')
            arquivo.close()
            return True

def sendNoticia(mensagem):
    try:
        PHONE_NUMBER = ''
        API_KEY=''
        response =requests.get(
            url=f'https://api.callmebot.com/whatsapp.php?phone={PHONE_NUMBER}&text={mensagem}&apikey={API_KEY}'
    
        )
        response.raise_for_status()
        #Se bem sucedida, continar aqui

    except requests.exceptions.RequestException as erro:
        with open('botNoticias.log.txt', 'w') as arquivo:
            arquivo.write(f'Erro no envio:{erro}\n')
            arquivo.write(f'String mensagem:"{mensagem}"')
            arquivo.close()

# ------- MAIN ----------
if _name_ == "_main_":

    log = getNoticiasLog() #Verifica se o log de noticias existe
    if(log):
        tituloUltimaNoticiaLog = getUltimaNoticiaLog() #Pega a última linha(Título de notícia) do log de notícias
        tituloUltimaNoticia = getUltimaNoticia() #Pega a última notícia da home do G1
        noticiaNova = setNoticiasLog(tituloUltimaNoticia,tituloUltimaNoticiaLog) #Compara a ultima noticia do log com da page; Adiciona nova noticia na última linha do log de notícias (Se houver) ;Retorna True se tiver noticia nova.
        
        if(noticiaNova):
            conteudos = getUltimaNoticiaContent()
            mensagem = f"{conteudos['tituloNoticia']}\n_{conteudos['subtituloNoticia']}_\n\n{conteudos['link']}"
            sendNoticia(mensagem)
            print(mensagem)
    
    else:
        print(os.getcwd())
        print("Não tem arquivo log")
        #createNoticiasLog()

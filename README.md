# noticiasBot
Developed By Avilag
Desenvolvido por Avilag
Linkedin: https://www.linkedin.com/in/gabriel-de-avila-farias/

Bot que verifica a cada 1min se foi postada nova noticia na home do G1 e envia as novas notícias pelo whatsApp com a API do callmebot

How to use the noticiasBot:
1 - Send Messege for CallmeBot https://www.callmebot.com/blog/free-api-whatsapp-messages/
2 - Instal with pip Install, requests and BeautifulSoup
3 - Set the params of the callme API on sendNoticia() function, set the PHONE_NUMBER = '' and API_KEY='' with your phone and API Key.
3.1-The fone number need's follow this format: <country_code><area_code><number> Exemple: 34123123123
4 - Set the cron of the linux to execute noticiasBot.


Como usar o noticiasBot:
1 - Envie uma mensagem para o CallmeBot https://www.callmebot.com/blog/free-api-whatsapp-messages/
2 - Instale com o pip install o requests e o BeautifulSoup
3 - Set os parâmetros da API do callMe na função sendNoticia(), para que o bot possa enviar as notícias para o seu WhatsApp(Para maiores detalhes consulte a documentação da API CallMe)
3.1-O número de telefone deve seguir esse formato: <Código do país><Código de área(DDD)><numero> Exemplo: 5521999999999
4 - Programe o cron do linux (ou semelhante no Windows) para executar o bot a cada 1min, ou o tempo que desejar. (Aconselho 1min, tenho testado este tempo e se mostrado satisfatório).

[ATENÇÃO] ao diretório em que o BOT será executado, ele lê, cria e modifica arquivos (noticias.log.txt) <-log para verificar qual a última noticia e compararar com o último titulo disponível na home do G1.


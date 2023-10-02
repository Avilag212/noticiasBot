# noticiasBot
Bot que verifica a cada 1min se foi postada nova noticia na home do G1 e envia as novas notícias pelo whatsApp com a API do callmebot

How to use the noticiasBot:
1 - Set the params of the callme API on sendNoticia() function, set the 
Para que o princípío de periodicidade do bot funcione é necessário agendar sua execução com o cron do linux, ou semelhante no Windows.

[ATENÇÃO] ao diretório em que o BOT será executado, ele lê, cria e modifica arquivos (noticias.log.txt) <-log para verificar qual a última noticia e compararar com o último titulo disponível na home do G1.


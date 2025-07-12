### COMANDO COM APENAS FUNÇÕES NECESSÁRIAS PARA O BOT FUNCIONAR!

import discord # Importa a biblioteca que nos permite usar recursos do Discord, como criar eventos, e usar discord.Client.

intents = discord.Intents.default() # Declara os recursos que o bot pode acessar (como membros de um servidor, id de canais...). É como dizer 'os recursos (intents) dos recursos do Discord (discord.Intents) que o bot pode acessar, é igual a x (default())'.

client = discord.Client(intents=intents) #Isso cria nosso bot. É como dizer 'o bot (client), cadastrado como cliente do Discord (discord.Client), pode acessar os recursos definidos acima (intents=intents)'

client.run('TOKEN DO BOT') # Coloca o bot para iniciar

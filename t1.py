#importa a API do discord
import discord

# Cria uma nova classe, que herda discord.Client (assim fazendo conexão com o discord). E é uma classe personalizada de cliente de discord.
class MyClient(discord.Client): 

    #função assíncrona de quando o bot fica online
    async def on_ready(self):

        #sempre que o bot estiver online, ele irá exibir a seguinte mensagem
        print(f'Logged on as {self.user}!')

# função assíncrona que executa quando uma mensagem é executada em um canal onde o bot tem acesso
    async def on_message(self, message):

        #o bot irá mostrar no terminal a cada mensagem recebida, o respectivo autor e seu conteúdo
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.all() #Cria um objeto intents com todas as permissões ativas.
intents.message_content = True #Garante que o bot possa ler o conteúdo das mensagens (message.content). A opção message_content vem desativada por padrão, mesmo que todas as permissões estejam ativas.

client = MyClient(intents=intents) #Você está criando uma instância do seu bot personalizado. Uma forma de  chamar a classe e todas as suas permissões

client.run("MTM4OTgxODE0MTU5MjI1NjYwMw.G-N5n3.4_SAMf1tMUdMnDAW9PiP6WxMSsPhvlVMtiPjBA") #inicia o seu bot, usando um token de autenticação (verificação da identidade do bot)
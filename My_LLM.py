from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()
# Substituir pela sua chave de API válida
OPEN_AI_KEY = 'ChaveDaAPI_IA'

chave_api = OPEN_AI_KEY

# Verificar se a chave foi carregada corretamente
if chave_api is None:
    raise ValueError("Chave API da OpenAI não encontrada")

# Definir as mensagens do sistema e do usuário
mensagens = [
    SystemMessage(content="Traduza o texto a seguir para o Inglês"),  # O 'content' é o atributo correto
    HumanMessage(content="Hello World")
]

# Inicializar o modelo com a chave da API
modelo = ChatOpenAI(api_key=chave_api, model="gpt-3.5-turbo-0125")

# Invocar o modelo e obter a resposta
resposta = modelo(messages=mensagens)

# Exibir a resposta
print(resposta)

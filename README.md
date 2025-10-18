# 🤖 Chatbot IA em Python

Um chatbot simples e eficiente usando OpenAI GPT, desenvolvido em Python com interface de linha de comando.

## ✨ Funcionalidades

- 💬 Conversação natural com IA
- 📝 Histórico de conversa
- 💾 Salvar/carregar conversas
- 🎨 Interface colorida no terminal
- ⚙️ Configurações personalizáveis

## 🚀 Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/antonio338854/python-ai-chatbot-2024.git
cd python-ai-chatbot-2024
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Configure sua chave da API OpenAI:**
```bash
cp .env.example .env
# Edite o arquivo .env e adicione sua chave da OpenAI
```

## 🔑 Configuração da API

1. Acesse [OpenAI API](https://platform.openai.com/api-keys)
2. Crie uma nova chave de API
3. Adicione no arquivo `.env`:
```
OPENAI_API_KEY=sua-chave-aqui
```

## 📖 Como Usar

### Execução básica:
```bash
python chatbot.py
```

### Comandos disponíveis:
- `sair` - Encerra o chatbot
- `limpar` - Limpa o histórico da conversa
- `salvar` - Salva a conversa atual

## 📁 Estrutura do Projeto

```
python-ai-chatbot-2024/
├── chatbot.py          # Arquivo principal
├── chatbot_colorido.py # Versão com interface colorida
├── requirements.txt    # Dependências
├── .env.example       # Exemplo de configuração
└── README.md          # Este arquivo
```

## ⚙️ Configurações

Você pode personalizar o comportamento do chatbot editando as variáveis no arquivo `.env`:

- `MAX_HISTORY`: Número máximo de mensagens no histórico (padrão: 10)
- `DEFAULT_MODEL`: Modelo da OpenAI a usar (padrão: gpt-3.5-turbo)
- `MAX_TOKENS`: Máximo de tokens por resposta (padrão: 500)
- `TEMPERATURE`: Criatividade das respostas (0.0-1.0, padrão: 0.7)

## 🛠️ Exemplo de Uso

```python
from chatbot import ChatbotIA

# Inicializar o chatbot
bot = ChatbotIA(api_key="sua-chave-aqui")

# Enviar mensagem
resposta = bot.get_response("Olá! Como você está?")
print(resposta)

# Salvar conversa
bot.save_conversation("minha_conversa.json")
```

## 📋 Requisitos

- Python 3.7+
- Chave da API OpenAI
- Conexão com internet

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature
3. Fazer commit das mudanças
4. Fazer push para a branch
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🆘 Suporte

Se encontrar algum problema:

1. Verifique se sua chave da API está configurada corretamente
2. Confirme que tem créditos na sua conta OpenAI
3. Verifique sua conexão com internet

## 🔄 Atualizações

- v1.0.0 - Versão inicial com funcionalidades básicas
- Interface colorida e melhorias na experiência do usuário

---

Desenvolvido com ❤️ por Pedro Carlos
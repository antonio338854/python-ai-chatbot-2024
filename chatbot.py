#!/usr/bin/env python3
"""
Chatbot IA simples usando OpenAI GPT
Autor: Pedro Carlos
"""

import openai
import os
import json
from datetime import datetime
from typing import List, Dict

class ChatbotIA:
    def __init__(self, api_key: str = None):
        """
        Inicializa o chatbot com a chave da API OpenAI
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("Chave da API OpenAI não encontrada. Configure OPENAI_API_KEY ou passe como parâmetro.")
        
        openai.api_key = self.api_key
        self.conversation_history: List[Dict] = []
        self.max_history = 10  # Limita o histórico para controlar custos
        
    def add_to_history(self, role: str, content: str):
        """Adiciona mensagem ao histórico da conversa"""
        self.conversation_history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
        
        # Mantém apenas as últimas mensagens
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]
    
    def get_response(self, user_message: str, model: str = "gpt-3.5-turbo") -> str:
        """
        Obtém resposta do chatbot para a mensagem do usuário
        """
        try:
            # Adiciona mensagem do usuário ao histórico
            self.add_to_history("user", user_message)
            
            # Prepara mensagens para a API
            messages = [
                {"role": "system", "content": "Você é um assistente IA útil e amigável. Responda de forma clara e concisa."}
            ]
            
            # Adiciona histórico da conversa
            for msg in self.conversation_history:
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
            
            # Chama a API OpenAI
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            bot_response = response.choices[0].message.content.strip()
            
            # Adiciona resposta do bot ao histórico
            self.add_to_history("assistant", bot_response)
            
            return bot_response
            
        except Exception as e:
            return f"Erro ao processar sua mensagem: {str(e)}"
    
    def clear_history(self):
        """Limpa o histórico da conversa"""
        self.conversation_history = []
        print("Histórico da conversa limpo!")
    
    def save_conversation(self, filename: str = None):
        """Salva a conversa em um arquivo JSON"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"conversa_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
            print(f"Conversa salva em: {filename}")
        except Exception as e:
            print(f"Erro ao salvar conversa: {e}")
    
    def load_conversation(self, filename: str):
        """Carrega uma conversa de um arquivo JSON"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.conversation_history = json.load(f)
            print(f"Conversa carregada de: {filename}")
        except Exception as e:
            print(f"Erro ao carregar conversa: {e}")

def main():
    """Função principal do chatbot"""
    print("🤖 Chatbot IA - Python")
    print("=" * 40)
    print("Digite 'sair' para encerrar")
    print("Digite 'limpar' para limpar histórico")
    print("Digite 'salvar' para salvar conversa")
    print("=" * 40)
    
    try:
        # Inicializa o chatbot
        bot = ChatbotIA()
        
        while True:
            # Recebe input do usuário
            user_input = input("\n👤 Você: ").strip()
            
            # Comandos especiais
            if user_input.lower() in ['sair', 'exit', 'quit']:
                print("\n👋 Até logo!")
                break
            elif user_input.lower() == 'limpar':
                bot.clear_history()
                continue
            elif user_input.lower() == 'salvar':
                bot.save_conversation()
                continue
            elif not user_input:
                continue
            
            # Obtém e exibe resposta do bot
            print("\n🤖 Bot: ", end="")
            response = bot.get_response(user_input)
            print(response)
            
    except KeyboardInterrupt:
        print("\n\n👋 Chatbot encerrado pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        print("\nVerifique se você configurou sua chave da API OpenAI:")
        print("export OPENAI_API_KEY='sua-chave-aqui'")

if __name__ == "__main__":
    main()
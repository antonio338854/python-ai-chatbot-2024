#!/usr/bin/env python3
"""
Chatbot IA com interface colorida
Versão melhorada com cores e melhor UX
"""

import openai
import os
import json
from datetime import datetime
from typing import List, Dict
from colorama import init, Fore, Back, Style

# Inicializa colorama
init(autoreset=True)

class ChatbotColorido:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("Configure OPENAI_API_KEY")
        
        openai.api_key = self.api_key
        self.conversation_history: List[Dict] = []
        self.max_history = 10
        
    def print_banner(self):
        print(Fore.CYAN + Style.BRIGHT + "🤖 CHATBOT IA - PYTHON")
        print(Fore.CYAN + "=" * 50)
        print(Fore.YELLOW + "Comandos:")
        print(Fore.GREEN + "  • 'sair' - Encerrar")
        print(Fore.GREEN + "  • 'limpar' - Limpar histórico") 
        print(Fore.GREEN + "  • 'salvar' - Salvar conversa")
        print(Fore.CYAN + "=" * 50)
        
    def add_to_history(self, role: str, content: str):
        self.conversation_history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
        
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]
    
    def get_response(self, user_message: str) -> str:
        try:
            self.add_to_history("user", user_message)
            
            messages = [
                {"role": "system", "content": "Você é um assistente IA útil e amigável."}
            ]
            
            for msg in self.conversation_history:
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            bot_response = response.choices[0].message.content.strip()
            self.add_to_history("assistant", bot_response)
            
            return bot_response
            
        except Exception as e:
            return f"Erro: {str(e)}"
    
    def clear_history(self):
        self.conversation_history = []
        print(Fore.GREEN + "✅ Histórico limpo!")
    
    def save_conversation(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversa_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
            print(Fore.GREEN + f"✅ Conversa salva: {filename}")
        except Exception as e:
            print(Fore.RED + f"❌ Erro ao salvar: {e}")

def main():
    try:
        bot = ChatbotColorido()
        bot.print_banner()
        
        while True:
            user_input = input(f"\n{Fore.BLUE}👤 Você: {Style.RESET_ALL}").strip()
            
            if user_input.lower() in ['sair', 'exit', 'quit']:
                print(f"\n{Fore.YELLOW}👋 Até logo!")
                break
            elif user_input.lower() == 'limpar':
                bot.clear_history()
                continue
            elif user_input.lower() == 'salvar':
                bot.save_conversation()
                continue
            elif not user_input:
                continue
            
            print(f"\n{Fore.GREEN}🤖 Bot: {Style.RESET_ALL}", end="")
            response = bot.get_response(user_input)
            print(response)
            
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}👋 Chatbot encerrado.")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Erro: {e}")

if __name__ == "__main__":
    main()
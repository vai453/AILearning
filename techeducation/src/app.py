import json
from xmlrpc import client
import os
from chatbot.chatboat import ChatBot
from chatbot.fewshotchatbot import FewChatBot
from chatbot.text_generation import TextGeneration
from chatbot.oneshotchatbot import OneChatBot
from chatbot.wheatherchatbot import WheaterChatbot
from chatbot.zero_gemini_chatbot import ZeroChatBot
from chatbot.wheather_function_chatboat import WheatherFunctionChatbot
from tool.finance_chatbot import FinanceChatbot
from tool.multitools import MultiTools


def chat():
    
    bot = ChatBot("Maths Mentor")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        response = bot.send_message(user_input)
        print(f"{bot.name}: {response}")
        
def text_generation():
    
    text_gen = TextGeneration("gpt-5.4")
    # prompt = "What is the capital of France?"
    prompt=input("You: ")
    response = text_gen.generate_text(prompt)
    print(f"Generated Text: {response}")
    
def text_generation_with_instructions():
    
    text_gen = TextGeneration("gpt-5")
    prompt = input("You: ")
    response = text_gen.generate_text_with_instructions(prompt)
    print(f"Generated Text with Instructions: {response}")
    
def one_shot_chatbot():
    
    
    bot = OneChatBot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        response = bot.generate_response(user_input)
        print(f"Medical Assistant: {response}")
        
def few_shot_chatbot():
    
    bot = FewChatBot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        response = bot.generate_response(user_input)
        print(f"Medical Assistant: {response}")
def zero_gemini_chatbot():
    
    bot = ZeroChatBot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        response = bot.generate_response(user_input)
        print(f"Medical Assistant: {response}")
def get_wheather_detail():
    bot = WheaterChatbot()
    while True:
        location = input("Enter location (e.g. 'London, UK') or press Enter for default: ").strip() or "London, UK"
        if location.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        result = bot.get_wheather_detail(location)

        print("\nWeather result:\n")
        if isinstance(result, dict):
            print(json.dumps(result, indent=2))
        else:
            print(result)
def wheather_function_chatboat():
    
    bot = WheatherFunctionChatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        response = bot.get_wheather_detail(user_input)
        print(f"Weather Info: {response}")

def get_employee_salary():
     fin_bot= FinanceChatbot()
     while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        response = fin_bot.get_employee_salary(user_input)
        print(f"Employee Salary: {response}")
        
def get_salary_by_query():
    fin_bot= FinanceChatbot()
    while True:        
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        response = fin_bot.get_employee_details(user_input)
        print(f"Query Result: {response}")
def multi_tools():
    multi_tool = MultiTools()
    while True:       
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        result = multi_tool.call_tool(prompt=user_input)
        print(f"Final Result: {result}") 

if __name__ == "__main__":   
         chat()
        # text_generation()
        # text_generation_with_instructions()
        # one_shot_chatbot()
        # few_shot_chatbot()
        # zero_gemini_chatbot()
        # get_wheather_detail()
        # wheather_function_chatboat()
        # get_employee_salary()
        # get_salary_by_query()
        # multi_tools()



import logging
from models import Role, Message, AnalysisResult
def dict_output(result: dict):
    try:
        for key,value in result.items():
            print(f"{key}: {value}")
    except Exception as e:
        logging.warning(f"发生错误：{e}")
    print()

def list_output(result: list):
    try:
        for i in range(len(result)):
            print(f"{i+1}. {result[i]}")
    except Exception as e:
        logging.warning(f"发生错误：{e}")
    print()

def format_result(result: AnalysisResult):
    print("========== Conversation ==========")
    print(f"Message count: {result.message_count}")
    print(f"user: {result.user_count}")
    print(f"assistant: {result.assistant_count}\n")
    list_output(result.user_message)
    list_output(result.assistant_message)
    print(f"total characters: {result.total_characters}\n")
    print("word count: ")
    dict_output(result.word_count)
    print("message length: ")
    list_output(result.message_length)
    print("average message length: ")
    dict_output(result.average_message_length)
    print(f"longest message: {result.longest_message}")
    print("==================================")
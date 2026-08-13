import logging
def dict_output(result):
    try:
        for key,value in result.items():
            print(f"{key}: {value}")
    except Exception as e:
        logging.warning(f"发生错误：{e}")
    print()

def list_output(result):
    try:
        for i in range(len(result)):
            print(f"{i+1}. {result[i]}")
    except Exception as e:
        logging.warning(f"发生错误：{e}")
    print()
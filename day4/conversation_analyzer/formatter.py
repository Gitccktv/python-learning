def dict_output(result):
    for key,value in result.items():
        print(f"{key}: {value}")
    print()

def list_output(result):
    for i in range(len(result)):
        print(f"{i+1}. {result[i]}")
    print()
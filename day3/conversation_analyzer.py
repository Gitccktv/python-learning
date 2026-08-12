
def count_messages(messages):
    count=0
    for message in messages:
        count+=1
    print(f"Messages: {count}\n")


def count_by_role(messages):
    count={}
    for message in messages:
        if count.get(message["role"])==None:
            count[message["role"]]=1
        else:
            count[message["role"]]+=1
    for key,value in count.items():
        print(f"{key}: {value}")
    print()
        

def get_user_messages(messages):
    print("User messages:")
    count=0
    for message in messages:
        if message["role"]=="user":
            count+=1
            print(f"{count}. {message['content']}")
    print()


def get_assistant_messages(messages):
    print("Assistant messages:")
    count=0
    for message in messages:
        if message["role"]=="assistant":
            count+=1
            print(f"{count}. {message['content']}")
    print()


def get_all_text(messages):
    sum=0
    for message in messages:
        sum+=len(message["content"])
    print(f"Total characters: {sum}\n")


def get_message_lengths(messages):
    print("每个Message长度：")
    lengths={
        x+1 : len(messages[x]["content"]) for x in range(len(messages))
    }
    for key,value in lengths.items():
        print(f"{key}: {value}")
    print()


def word_count(messages):
    words={"Python":0,"AI":0,"RAG":0,"Agent":0}
    for message in messages:
        for word in words.keys():
            words[word]+=message["content"].count(word)
    print("各单词在messages出现次数：")
    for key,value in words.items():
        print(f"{key}: {value}")
    print()


def longest_message(messages):
    max_length=0
    string=""
    for message in messages:
        if len(message["content"]) > max_length:
            max_length=len(message["content"])
            string=message["content"]
    print(f"Longest message:\n{string}\n")


def average_message_length(messages):
    roles=set()
    for message in messages:
        roles.add(message["role"])
    count={}
    total_len={}
    for message in messages:
        count[message["role"]]=count.get(message["role"],0)+1
        total_len[message["role"]]=total_len.get(message["role"],0)+len(message["content"])
    for role in roles:
        print(f"平均{role} message长度：{total_len[role]/count[role]}")
    

def main():
    messages = [
    {
        "role": "user",
        "content": "什么是 RAG？"
    },
    {
        "role": "assistant",
        "content": "RAG 是 Retrieval Augmented Generation..."
    },
    {
        "role": "user",
        "content": "那 Agent 呢？"
    },
    {
        "role": "assistant",
        "content": "Agent 是能够调用工具..."
    }
    ]
    print("========== Conversation ==========")
    count_messages(messages)
    count_by_role(messages)
    get_user_messages(messages)
    get_assistant_messages(messages)
    get_all_text(messages)
    get_message_lengths(messages)
    word_count(messages)
    longest_message(messages)
    average_message_length(messages)
    print("==================================")

if __name__ == "__main__":
    main()


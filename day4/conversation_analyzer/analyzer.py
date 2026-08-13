def count_messages(messages):
    return len(messages)

def count_by_role(messages):
    count={}
    for message in messages:
        count[message["role"]]=count.get(message["role"],0)+1
    return count
        

def get_user_messages(messages):
    result=[
        message["content"] for message in messages
        if message["role"]=="user"
    ]
    return result
    

def get_assistant_messages(messages):
    result=[
        message["content"] for message in messages
        if message["role"]=="assistant"
    ]
    return result


def get_all_text(messages):
    total_chr=0
    for message in messages:
        total_chr+=len(message["content"])
    return total_chr


def get_message_lengths(messages):
    lengths={
        x+1 : len(messages[x]["content"]) for x in range(len(messages))
    }
    return lengths


def word_count(messages):
    words={"Python":0,"AI":0,"RAG":0,"Agent":0}
    for message in messages:
        for word in words.keys():
            words[word]+=message["content"].lower().count(word.lower())
    return words


def longest_message(messages):
    max_length=0
    string=""
    for message in messages:
        if len(message["content"]) > max_length:
            max_length=len(message["content"])
            string=message["content"]
    return string


def average_message_length(messages):
    count={}
    total_len={}
    for message in messages:
        count[message["role"]]=count.get(message["role"],0)+1
        total_len[message["role"]]=total_len.get(message["role"],0)+len(message["content"])
    result={
        role : total_len[role]/count[role] for role in count.keys()
    }
    return result


from models import Message, Role, AnalysisResult

def count_messages(messages: list[Message]) -> int:
    return len(messages)

def count_by_role(messages: list[Message]) -> dict[Role,int]:
    count={}
    for message in messages:
        count[message.role]=count.get(message.role,0)+1
    return count
        

def get_user_messages(messages: list[Message]) -> list[str]:
    result=[
        message.content for message in messages
        if message.role==Role.USER
    ]
    return result
    

def get_assistant_messages(messages: list[Message]) -> list[str]:
    result=[
        message.content for message in messages
        if message.role==Role.ASSISTANT
    ]
    return result


def get_all_text(messages: list[Message]) -> int:
    total_chr=0
    for message in messages:
        total_chr+=len(message.content)
    return total_chr


def get_message_lengths(messages: list[Message])-> list[int]:
    lengths=[
        len(messages[x].content) for x in range(len(messages))
    ]
    return lengths


def word_count(messages:list[Message])->dict[str,int]:
    words={"Python":0,"AI":0,"RAG":0,"Agent":0}
    for message in messages:
        for word in words.keys():
            words[word]+=message.content.lower().count(word.lower())
    return words


def longest_message(messages: list[Message])->str:
    max_length=0
    string=""
    for message in messages:
        if len(message.content) > max_length:
            max_length=len(message.content)
            string=message.content
    return string


def average_message_length(messages:list[Message])->dict[Role,float]:
    count={}
    total_len={}
    for message in messages:
        count[message.role]=count.get(message.role,0)+1
        total_len[message.role]=total_len.get(message.role,0)+len(message.content)
    result={
        role : total_len[role]/count[role] for role in count.keys()
    }
    return result

def analyze(messages: list[Message]) -> AnalysisResult:
    result=AnalysisResult(
        message_count=count_messages(messages),
        user_count=count_by_role(messages)[Role.USER],
        assistant_count=count_by_role(messages)[Role.ASSISTANT],
        total_characters=get_all_text(messages),
        average_message_length=average_message_length(messages),
        longest_message=longest_message(messages),
        user_message=get_user_messages(messages),
        assistant_message=get_assistant_messages(messages),
        message_length=get_message_lengths(messages),
        word_count=word_count(messages)
    )
    return result
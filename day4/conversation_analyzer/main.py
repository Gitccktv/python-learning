import analyzer as an
import formatter as fm

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
    print(f"Message: {an.count_messages(messages)}")
    fm.dict_output(an.count_by_role(messages))
    print("User messages:")
    fm.list_output(an.get_user_messages(messages))
    print("Assistant messages:")
    fm.list_output(an.get_assistant_messages(messages))
    print(f"Total characters: {an.get_all_text(messages)}\n")
    print("每个Message长度：")
    fm.dict_output(an.get_message_lengths(messages))
    print("各单词在messages出现次数:")
    fm.dict_output(an.word_count(messages))
    print(f"Longest message:\n{an.longest_message(messages)}\n")
    print("各类message平均长度：")
    fm.dict_output(an.average_message_length(messages))
    print("==================================")


if __name__ == "__main__":
    main()
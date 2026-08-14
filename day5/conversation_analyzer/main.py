from analyzer import analyze
from  result_formatter import format_result
from models import Role,Message
def main():
    messages = [
        Message(
            role=Role.USER,
            content="什么是 RAG？"
        ),
        Message(
            role=Role.ASSISTANT,
            content="RAG 是检索增强生成..."
        ),
        Message(
            role=Role.USER,
            content="那 Agent 呢？"
        ),
        Message(
            role=Role.ASSISTANT,
            content="Agent 可以调用工具..."
        ),
    ]
    result=analyze(messages)
    format_result(result)


if __name__ == "__main__":
    main()
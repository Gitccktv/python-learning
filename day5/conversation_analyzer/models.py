from dataclasses import dataclass
from enum import Enum

class Role(Enum):
    USER="user"
    ASSISTANT="assistant"

@dataclass
class Message:
    role: Role
    content: str

@dataclass
class AnalysisResult:
    message_count: int
    user_count: int
    assistant_count: int
    user_message: list[str]
    assistant_message: list[str]
    total_characters: int
    word_count: dict[str,int]
    message_length: list[int]
    average_message_length: dict[Role, float]
    longest_message: str

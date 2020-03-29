import enum


class BaseEnum(enum.Enum):
    @classmethod
    def to_choice(cls):
        return [(tag.value, tag) for tag in cls]


class AgentLanguage(BaseEnum):
    ENGLISH = "en"
    KOREAN = "ko"
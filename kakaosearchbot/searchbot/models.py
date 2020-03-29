import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models import UUIDField, DateTimeField, CharField, CASCADE, ForeignKey

from .const import AgentLanguage


class BaseModel(models.Model):
    u_id = UUIDField(editable=False, unique=True, null=False, default=uuid.uuid4)
    created_at = DateTimeField(auto_now_add=True)


class Agent(User, models.Model):
    agent_name = CharField(max_length=30, default='KakaoUser')
    lang = CharField(max_length=2, choices=AgentLanguage.to_choice())

    def __str__(self):
        return self.agent_name


class TextFile(BaseModel):
    agent = ForeignKey(Agent, related_name='texts', on_delete=CASCADE)
    title = CharField(max_length=50)
    category = CharField(max_length=50)


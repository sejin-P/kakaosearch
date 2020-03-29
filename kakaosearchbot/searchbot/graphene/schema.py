import graphene
from graphene_django.types import DjangoObjectType
from searchbot.models import Agent, TextFile
from graphene_file_upload.scalars import Upload
import django_rq
from graphene_django.forms.mutation import DjangoFormMutation


class AgentType(DjangoObjectType):
    class Meta:
        model = Agent


class TextFileType(DjangoObjectType):
    class Meta:
        model = TextFile


class TextFileUpload(graphene.ClientIDMutation):
    ok = graphene.Boolean()

    class Input:
        file_in = Upload(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        return TextFileUpload(ok=True)


class Query(object):
    all_agents = graphene.List(AgentType)
    all_text_files = graphene.List(TextFileType)

    def resolve_all_agents(self, info, **kwargs):
        return Agent.objects.all()

    def resolve_all_text_files(self, info, **kwargs):
        return TextFile.objects.all()


class Mutation()
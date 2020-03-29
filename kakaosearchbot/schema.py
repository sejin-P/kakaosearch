import graphene
import searchbot.graphene.schema


class Query(Query, graphene.ObjectType):
    pass


class Mutation(TextFileUpload):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)


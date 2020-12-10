import graphene

import guesser.schema


class Query(guesser.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

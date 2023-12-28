from graphene import ObjectType, String

class TodoType(ObjectType):
    title = String()
    description = String()
    time = String()
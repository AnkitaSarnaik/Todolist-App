from ariadne import ObjectType
from graphene import List
from todo_type import TodoType

class Query(ObjectType):
    todos = List(TodoType)
   
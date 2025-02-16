from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def createTask(request):
    return Response('Task created')


@api_view(['GET'])
def getTask(request):
    return Response('Task fetched')


@api_view(['PUT'])
def updateTask(request):
    return Response('Task updated')


@api_view(['DELETE'])
def deleteTask(request):
    return Response('Task deleted')

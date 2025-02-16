from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer


@api_view(['POST'])
def createTask(request):
    return Response('Task created')


@api_view(['GET'])
def getTask(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateTask(request):
    return Response('Task updated')


@api_view(['DELETE'])
def deleteTask(request):
    return Response('Task deleted')

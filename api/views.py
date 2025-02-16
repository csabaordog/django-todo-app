from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer


@api_view(['POST'])
def createTask(request):

    serializer = TaskSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def getTask(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)
       
        return Response(serializer.data)
    
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAllTasks(request):
    tasks = Task.objects.all()

    status = request.query_params.get('status')
    if status:
        tasks = tasks.filter(status=status)

    due_date = request.query_params.get('due_date')
    if due_date:
        tasks = tasks.filter(due_date=due_date)

    sort_by = request.query_params.get('sort_by')
    order = request.query_params.get('order', 'asc')
    if sort_by in ['created_at', 'due_date']:
        if order == 'desc':
            sort_by = f'-{sort_by}'
        tasks = tasks.order_by(sort_by)

    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def updateTask(request, pk):
    
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteTask(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.views import APIView
from app.models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response

# Create your views here.
class GetRoutes(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"tasks/","task/:task.id"})

class TaskList(APIView):
    serializer_class = TaskSerializer
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(owner=self.request.user)
        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        task = Task.objects.create(
            title = request.data['title'],
            description = request.data['description'],
            owner = self.request.user,
        )
        serializer = self.serializer_class(task, many=False)
        return Response(serializer.data)

class TaskDetails(APIView):
    serializer_class = TaskSerializer
    def get(self, request, pk):
        try:
            task = Task.objects.get(id=pk, owner=self.request.user)
        except:
            return Response('Couldn\'t Find this task', status=404)
        serializer = self.serializer_class(task, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            task = Task.objects.get(id=pk, owner=self.request.user)
            task.title = request.data['title']
            task.description = request.data['description']
            task.save()
        except:
            return Response('Couldn\'t Update this task You Don\'t own it!', status=404)
        serializer = self.serializer_class(task, many=False)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            task = Task.objects.get(id=pk, owner=self.request.user)
        except:
            return Response('Couldn\'t Delete this task You don\'t own it!', status=404)
        task.delete()
        return Response('Task Was Deleted!')


from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from todo import models, serializers
from todo.models import Todo
from user_auth.permissions import IsOwnerOrAdmin


class TodoListView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get(self, request):
        data = models.Todo.objects.filter(owner=request.user)
        serializer = serializers.TodoSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = serializers.TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
    permission_classes = [IsOwnerOrAdmin]

    def get(self, request, pk):
        try:
            data = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.TodoSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            data = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

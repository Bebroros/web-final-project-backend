from rest_framework.response import Response
from rest_framework.views import APIView
from events.models import Event
from events.serializers import EventSerializer
from rest_framework import status
from user_auth.permissions import IsOwnerOrAdmin

class EventList(APIView):
    permission_classes = [IsOwnerOrAdmin]

    def get(self, request):
        if request.user.is_staff:
            events = Event.objects.all()
        else:
            events = Event.objects.filter(owner=request.user)
        serializer = EventSerializer(events, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       


class EventDetail(APIView):
    permission_classes = [IsOwnerOrAdmin]

    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(request, event)
            serializer = EventSerializer(event)
        except Event.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(request, event)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(request, event)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

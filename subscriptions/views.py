from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from subscriptions.models import Subs
from subscriptions.serializers import SubsSerializer
from rest_framework import status
from user_auth.permissions import IsOwnerOrAdmin


class SubsList(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get(self, request):
        if request.user.is_staff:
            subs = Subs.objects.all()
        else:
            subs = Subs.objects.filter(owner=request.user)
        serializer = SubsSerializer(subs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SubsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubsDetails(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get(self, request, pk):
        try:
            subs = Subs.objects.get(pk=pk)
            self.check_object_permissions(request, subs)
            serializer = SubsSerializer(subs)
        except Subs.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    def patch(self, request, pk):
        try:
            subs = Subs.objects.get(pk=pk)
            self.check_object_permissions(request, subs)
        except Subs.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SubsSerializer(subs, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            subs = Subs.objects.get(pk=pk)
            self.check_object_permissions(request, subs)
        except Subs.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        subs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
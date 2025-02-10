from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import FormRecordsSerializer
from .models import CustomMember  # Ensure this is the correct model name

class FormRecordsAPIView(APIView):
    """
    API endpoint to retrieve all form records or create a new record.
    """

    def get(self, request):
        print("Fetching all users...")  # Debugging
        users = CustomMember.objects.all()
        serializer = FormRecordsSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print("Received POST request with data:", request.data)  # Debugging
        serializer = FormRecordsSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            print(f"New user created with ID: {instance.id}")  # Debugging
            return Response({"id": instance.id}, status=status.HTTP_201_CREATED)
        print("Validation errors:", serializer.errors)  # Debugging
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FormRecordDetailAPIView(APIView):
    """
    API endpoint to retrieve a single form record by ID.
    """

    def get_object(self, pk):
        try:
            print(f"Fetching user with ID: {pk}")  # Debugging
            return CustomMember.objects.get(pk=pk)
        except CustomMember.DoesNotExist:
            print(f"User with ID {pk} not found.")  # Debugging
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = FormRecordsSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import FormRecordsSerializer
from .models import CustomMember  # Ensure this is the correct model name

class FormRecordsAPIView(APIView):
    """
    API endpoint for handling form records.
    - Allows anyone to submit a form via POST.
    - GET request is restricted to logged-in admin users.
    """
    permission_classes = [AllowAny]  # Allow anyone to submit the form

    def post(self, request):
        print("Received POST request with data:", request.data)  # Debugging
        serializer = FormRecordsSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            print(f"New user created with ID: {instance.id}")  # Debugging
            return Response({"id": instance.id}, status=status.HTTP_201_CREATED)
        print("Validation errors:", serializer.errors)  # Debugging
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(login_required)
    def get(self, request):
        # Check if user is a staff/admin user
        if not request.user.is_staff:
            return Response({"error": "Admin access required"}, status=status.HTTP_403_FORBIDDEN)

        # Fetch all form records
        records = CustomMember.objects.all()
        serializer = FormRecordsSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FormRecordDetailAPIView(APIView):
    """
    API endpoint to retrieve a single form record by ID.
    - Allows unauthenticated access **only** when accessed via QR code (custom header check).
    - Requires authentication for all other actions.
    """
    permission_classes = [IsAuthenticated]  # Default: Authentication required

    def get_object(self, pk):
        try:
            print(f"Fetching user with ID: {pk}")  # Debugging
            return CustomMember.objects.get(pk=pk)
        except CustomMember.DoesNotExist:
            print(f"User with ID {pk} not found.")  # Debugging
            raise Http404

    def get(self, request, pk):
        # Check for the custom QR access header
        if request.headers.get("X-QR-Access") == "true":
            print("QR Access granted without authentication")  # Debugging
            user = self.get_object(pk)
            serializer = FormRecordsSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Otherwise, enforce authentication
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_403_FORBIDDEN)

        user = self.get_object(pk)
        serializer = FormRecordsSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

@login_required
def authenticated_user(request):
    """Returns the currently logged-in Django Admin user."""
    return JsonResponse({
        "username": request.user.username,
        "email": request.user.email,
        "is_superuser": request.user.is_superuser
    })

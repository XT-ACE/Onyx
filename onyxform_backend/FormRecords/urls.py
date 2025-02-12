from django.urls import path
from .views import FormRecordsAPIView, FormRecordDetailAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import authenticated_user

urlpatterns = [
    path('form-records/', FormRecordsAPIView.as_view(), name='form-records'),
    path('form-records/<int:pk>/', FormRecordDetailAPIView.as_view(), name='form-record-detail'),  # ✅ Get specific record by ID
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path("api/authenticated-user/", authenticated_user, name="authenticated-user"),
]

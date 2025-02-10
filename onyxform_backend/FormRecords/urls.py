from django.urls import path
from .views import FormRecordsAPIView, FormRecordDetailAPIView

urlpatterns = [
    path('form-records/', FormRecordsAPIView.as_view(), name='form-records'),
    path('form-records/<int:pk>/', FormRecordDetailAPIView.as_view(), name='form-record-detail'),  # ✅ Get specific record by ID
]

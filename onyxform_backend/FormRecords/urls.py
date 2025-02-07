from django.urls import path
from .views import FormRecordsAPIView
urlpatterns = [
    path('form-records/', FormRecordsAPIView.as_view(), name='form-records'),
]

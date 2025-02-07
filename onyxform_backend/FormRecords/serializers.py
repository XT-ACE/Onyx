from rest_framework import serializers
from .models import CustomUser

class FormRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id', 'title', 'last_name', 'first_name', 'age', 'date_of_birth', 'place_of_birth', 'gender', 'nationality', 'mobile_number', 
            'email_address', 'city_residence', 'state_residence', 'valid_id', 'valid_until', 
            'id_no', 'work_industry', 'role', 'income', 'same_address', 'street_address', 
            'permanent_street_address', 'permanent_city', 'permanent_state', 'id_front', 'id_back'  # Added id_front
        )

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

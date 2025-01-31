from rest_framework import serializers
from .models import CustomUser

class FormRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'title', 'last_name', 'first_name', 'age', 'citizenship', 'mobile_number', 
                  'email_address', 'country_residence', 'valid_id', 'id_no', 'work_industry', 
                  'role', 'income', 'present_address', 'permanent_address', 'street_address')  # Added street_address

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)



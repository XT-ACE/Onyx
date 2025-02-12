from rest_framework import serializers
from .models import CustomMember

class FormRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomMember
        fields = (
            'id', 'title', 'last_name', 'first_name', 'age', 'date_of_birth', 'place_of_birth', 'gender', 'nationality', 'mobile_number', 
            'email_address', 'city_residence', 'state_residence', 'valid_id', 'valid_until', 
            'id_no', 'work_industry', 'role', 'income', 'same_address', 'marketing_consent', 'privacy_consent','agreeToPrivacy','isOver21', 'street_address', 
            'permanent_street_address', 'permanent_city', 'permanent_state', 'id_front', 'id_back', 'signature'  # ✅ Added signature
        )

    def create(self, validated_data):
        return CustomMember.objects.create(**validated_data)

from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import UserForm

class UserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserForm
        fields = '__all__'

    def validate_date_of_birth(self, value):
        age = timezone.now().date().year - value.year - ((timezone.now().date().month, timezone.now().date().day) < (value.month, value.day))
        if age < 18:
            raise serializers.ValidationError("You must be at least 18 years old to submit the form.")
        
        return value

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Invalid phone number format.")
        
        return value
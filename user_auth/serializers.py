from rest_framework import serializers
from .models import CustomUser, UserProfile
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def validate(self, data):
        if 'role' in data and data['role'] != 'user':
            raise serializers.ValidationError("You can only register as a user.")
        validate_email(data['email'])
        return data

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            role='user'
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'age']

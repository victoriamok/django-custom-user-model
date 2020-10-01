from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import (
    CharField,
    EmailField,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = EmailField(label='E-mail')
    password = CharField(label='Password', style={'input_type': 'password'})
    password2 = CharField(label='Confirm password', style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'password2',
        ]
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def validate(self, data):
        if not data.get('password') or not data.get('password2'):
            raise serializers.ValidationError("You must confirm your password.")
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Passwords don't match.")
        return data

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.save()
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    email = EmailField(label='E-mail')
    password = CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        return data


# def validate_new_password(value):
#     validate_password(value)
#     return value


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)



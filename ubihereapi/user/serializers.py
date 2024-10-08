from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "id",
            "name",
            "email",
            "password",
            "is_staff",
            "is_superuser"
        ]

        # Makes sure password is write only and won't be listed on get

        extra_kwargs = {
            'password': {'write_only': True},
        }


    # Overriding the create method and also hashing the password before saving

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    # Overriding to hash the edited password before saving

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).update(instance, validated_data)
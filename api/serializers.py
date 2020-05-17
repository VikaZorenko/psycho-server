from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        if validated_data.get('email'):
            user.email = validated_data['email']
        user.save()

        return user

    class Meta:
        model = User
        fields = ("id", "username", "email", "password",)

from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', )

    def create(self, validated_data):
        user = UserModel.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('id', 'username', )
from rest_framework import serializers

from network.models import User, Following, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

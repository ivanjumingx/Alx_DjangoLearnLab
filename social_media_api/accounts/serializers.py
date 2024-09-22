from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Getting the custom user model
CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Using CharField for password with write-only access for security
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    bio = serializers.CharField(required=False, allow_blank=True)
    profile_picture = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers']
        extra_kwargs = {
            'followers': {'read_only': True},  # Make followers field read-only
        }

    # Override the create method to hash passwords and create the user properly
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(**validated_data)  # Create the user using the custom user model
        user.set_password(password)  # Hash the password
        user.save()
        Token.objects.create(user=user)  # Create a token for the user
        return user

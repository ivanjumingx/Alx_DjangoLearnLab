from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Fetching the custom user model
CustomUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # Use serializers.CharField() for password handling with write_only to ensure security
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    bio = serializers.CharField(required=False, allow_blank=True)
    profile_picture = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers']
        extra_kwargs = {
            'followers': {'read_only': True},  # Make followers read-only
        }

    # Override the create method to create a user using get_user_model().objects.create_user
    def create(self, validated_data):
        # Remove the password from validated_data to handle it separately
        password = validated_data.pop('password')

        # Use get_user_model().objects.create_user to create a new user
        user = CustomUser.objects.create_user(**validated_data)

        # Set the password using set_password for proper hashing
        user.set_password(password)
        user.save()

        # Create an auth token for the newly created user
        Token.objects.create(user=user)

        return user

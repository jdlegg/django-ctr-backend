from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers, status
from .models import CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['fav_color'] = user.fav_color
        token['username'] = user.username
        return token

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        lower_email = value.lower()
        if CustomUser.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Email Already Exists")
        return lower_email

    def validate_username(self, value):
        lower_username = value.lower()
        if CustomUser.objects.filter(username__iexact=lower_username).exists():
            raise serializers.ValidationError("Username Already Exists")
        return lower_username

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance
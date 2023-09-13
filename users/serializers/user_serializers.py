from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User

"""Add serializers for User views
(Добавлены сериализаторы для контроллеров User)"""


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserAuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

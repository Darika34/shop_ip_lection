from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)
                                                          # write_only dlya zapysy danny,kotorie nelza vivodyt

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation', 'first_name', 'last_name', 'username', 'avatar')


    def validate(self,attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError(
                'password must be the same'
            )
        if password.isdigit() or password.isalpha():
            raise serializers.ValidationError(
                'password should be with words and numbers'
            )
        return attrs


    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class ActivationSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)

    def validate(self, attrs):
        self.code = attrs['code']
        return attrs

    def save(self, **kwargs):
        try:
            user = User.objects.get(activation_code=self.code)
            user.is_active = True
            user.activation_code = ''
            user.save()
        except:
            self.fail('неверный код')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',) #skryt






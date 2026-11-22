from rest_framework import serializers
from accounts.models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True,style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['id','username','password','password2','role']

        def validate(self, data):
            if data['password'] != data['password2']:
                raise serializers.ValidationError('Пароли не совпадають!')
            return data

        def create(self, validated_data):
            validated_data.pop['password2']
            user = CustomUser.objects.create_user(**validated_data)
            return user
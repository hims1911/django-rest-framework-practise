from rest_framework import serializers
from .models import User
import re

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,validators=[])
    class Meta:
        model = User
        fields = ('name', 'email', 'mobile', 'password', 'city', 'pincode')

    def validate_password(self, data):
        password = data
        errors = dict() 
        rgx = re.compile(r'\d.*?[A-Z].*?[a-z]')

        if not (rgx.match(''.join(sorted(password))) and len(password) >= 8):
            errors['password'] = "Password should contain atleast 1 capital letter,1 small letter and length should be greater 7"
        
        if errors:
            raise serializers.ValidationError(errors['password'])
        
        return super(UserSerializer, self).validate(data)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
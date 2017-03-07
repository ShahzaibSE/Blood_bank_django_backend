from rest_framework import serializers

#Import Model
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
          model = User
          fields = ('id','firstname','lastname','email','password','createdAt')

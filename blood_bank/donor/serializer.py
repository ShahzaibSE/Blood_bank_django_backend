from rest_framework import serializers

#Import models
from donor.models import Donor

class donorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donor
        fields = ('id','firstname','lastname','bloodGroup','city','createdAt')
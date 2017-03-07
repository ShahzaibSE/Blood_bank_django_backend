from rest_framework import serializers

#Import models
from procurer.models import Procurer

class procurerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Procurer
        fields = ('id','firstname','lastname','numberOfDonors','city','createdAt')
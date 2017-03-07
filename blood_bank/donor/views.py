# Create your views here.
from django.conf.urls import *
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

#Models
from donor.models import Donor

#Serializer
from donor.serializer import donorSerializer

@api_view(['GET','POST'])
def donor_get_post(request):
    print(request);

    if(request.method == 'GET'):
        donorsList = Donor.objects.all();
        print("Donor's List");
        print(donorsList);

        #Serialize
        donorJSON = donorSerializer(donorsList,many=True)
        return Response(donorJSON.data);

    if(request.method == 'POST'):
        newDonor = donorSerializer(data = request.data);

        if(newDonor.is_valid()):
           newDonor.save();
           return Response(newDonor.data);

        return Response(newDonor.errors);




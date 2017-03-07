from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

#Import Serializer
from user.serializers import UserSerializer

#Import models
from user.models import User

# Create your views here.
@api_view(['GET','POST'])
def getallUsers(request):
    '''
     Get all users
    '''

    if request.method == 'GET':
        usersList = User.objects.all();
        # userList_JSON = JSONRenderer().render(usersList)
        userList_JSON = UserSerializer(usersList,many=True)
        return Response(userList_JSON.data)

    elif request.method == 'POST':
        # requestObj = JSONParser().parse(request)
        newUser = UserSerializer(data=request.data)

        if newUser.is_valid():
            newUser.save();
            return Response(newUser.data)
            # return Response({'status':True})

        return Response(newUser.errors)



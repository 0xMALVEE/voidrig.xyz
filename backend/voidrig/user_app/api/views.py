from django.shortcuts import render
from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer, InviteSerializer
from user_app.models import Invite
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
import secrets
import string

# Registration View
@api_view(['POST'])
def registration_view(request):
    
    if request.method == "POST":
        seriazlier = RegistrationSerializer(data=request.data)
        
        data = {}
        
        if seriazlier.is_valid():
            account = seriazlier.save()
            data['response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email
            
            # token = 
        else:
            data = seriazlier.errors
        
        return Response(data)

# GenerateInviteView
class GenerateInviteView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self,request):
        InviteCodeLength = 30
        code = str(''.join(secrets.choice(string.ascii_uppercase + string.digits)
              for i in range(InviteCodeLength)))
        
        serializer = InviteSerializer(data={ "invitecode": code })
        
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
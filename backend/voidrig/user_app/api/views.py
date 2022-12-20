from django.shortcuts import render
from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response

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

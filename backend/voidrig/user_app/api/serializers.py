from django.contrib.auth.models import User
from rest_framework import serializers
from user_app.models import Invite

# Registration Serialiser
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={ 'input-type':'password' },write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        
    # overiding save function
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        emailData = self.validated_data['email']
        usernameData = self.validated_data['username']
        
        if password != password2:
            raise serializers.ValidationError({"Error":"Password didn't match "})

        if User.objects.filter(email=emailData).exists():
            raise serializers.ValidationError({"Error":"Email already exist"})

        if User.objects.filter(username=usernameData).exists():
            raise serializers.ValidationError({"Error":"Username already exist"})
        
        account = User(email = emailData, username= usernameData)
        account.set_password(password)
        account.save()
        
        return account
    
# Invite Serializer
class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = "__all__"
        
    def save(self):
        code = self.validated_data["invitecode"]
        # check for existing codes
        if Invite.objects.filter(invitecode=code).exists():
            raise serializers.ValidationError({"Error":"Same Generated Invite Code Alrady Exist!"})
        else:
            d = Invite(invitecode= code)      
            d.save()
            
            return d;  
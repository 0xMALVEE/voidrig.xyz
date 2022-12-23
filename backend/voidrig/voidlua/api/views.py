from django.shortcuts import render
from rest_framework import generics
from voidlua.api.serializers import LuaSerializer
from voidlua.models import Lua
from rest_framework.permissions import IsAuthenticated
from voidlua.api.permissions import IsOwnerOfLua,IsOwnerOfLuas
from rest_framework.views import APIView
from rest_framework.response import Response

# Lua View (List All the luas)
class LuaListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Lua.objects.all()
    serializer_class = LuaSerializer
    

# Specific luas (CRUD)
class LuaView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOfLua]
    queryset = Lua.objects.all()
    serializer_class = LuaSerializer
        
    

# with APIView Class
# class LuaView(APIView):
#     permission_classes = [IsAuthenticated, IsOwnerOfLua]
    
#     def get(self,request,pk):
#         serializer = LuaSerializer(Lua.objects.get(pk=pk))
        
#         self.check_object_permissions(request,Lua.objects.get(pk=pk))
#         return Response(serializer.data)

# Get Lua By User ID <int:user>/luas (CRUB) (FOR USERS CLIENT PANEL)
class UserLuasView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOfLuas]
    serializer_class = LuaSerializer
    
    def get_queryset(self):
        userid = self.kwargs['user']
        
        return Lua.objects.filter(luaowner=userid)


from rest_framework import serializers
from voidlua.models import Lua  

# lua serializer
class LuaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lua
        fields = "__all__"
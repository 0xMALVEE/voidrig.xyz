from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOfLua(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        return obj.luaowner.id == request.user.id

class IsOwnerOfLuas(BasePermission):
    def has_permission(self, request, view):
        # kwargs array gets data from urls <int:data> 
        # view.kwargs['user'] get int from api/<int:user>/luas
        return request.user.id == view.kwargs['user']
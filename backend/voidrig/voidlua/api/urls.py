from django.urls import path, include
from voidlua.api.views import LuaListView, LuaView, UserLuasView

urlpatterns = [
    path('luas/',LuaListView.as_view(), name="lua-list"),
    path('lua/<int:pk>', LuaView.as_view(), name="lua-detail"),
    path('<int:user>/luas/', UserLuasView.as_view(), name="users-luas")
]

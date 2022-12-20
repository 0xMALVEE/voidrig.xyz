from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Lua Model
class Lua(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    lua = models.TextField(max_length=1000)
    luaowner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title;
from django.db import models

# Invite Model
class Invite(models.Model):
    invitecode = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invitecode

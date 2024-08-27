from django.db import models
from django.contrib.auth.models import User

class Visitor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    visit_time = models.DateTimeField(auto_now_add=True)
    checkout_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default='admin')

    def __str__(self):
        return self.user.username

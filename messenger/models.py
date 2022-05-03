from django.db import models
from user.models import Account
from django.utils import timezone
# Create your models here.
class ThreadModel(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='+')

class Messages(models.Model):
    thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='+')
    body = models.CharField(max_length=1000)
    date = models.DateTimeField(default = timezone.now)

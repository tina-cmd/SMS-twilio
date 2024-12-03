from django.db import models
from twilio.rest import Client

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.score >= 70:
            account_sid = 'ACc818ac8b0242aa4a0a14a661c044b1c6'
            auth_token = '95a80819a3914d934096ff68aafbd5b8'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body =f"Congratualations {self.name}, your score is {self.score}.",
                from_='+16413165940',
                to='+639463434042'
            )
        else:
            account_sid = 'ACc818ac8b0242aa4a0a14a661c044b1c6'
            auth_token = '95a80819a3914d934096ff68aafbd5b8'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body =f"Sorry {self.name}, your score is {self.score}. Try again",
                from_='+16413165940',
                to='+639463434042'
            )


        print(message.sid)
        return super().save(*args, **kwargs)

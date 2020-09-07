from django.db import models


class User(models.Model):
    userID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    contactNo = models.IntegerField()
    petName = models.CharField(max_length=50, blank=True)
    _created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName + ' - ' + self.lastName

from django.db import models


class Appointment(models.Model):
    appointmentID = models.AutoField(primary_key=True)
    userID = models.IntegerField()
    vetID = models.IntegerField()
    availabilityID = models.IntegerField()
    reason = models.CharField(max_length=100)
    petDetails = models.CharField(max_length=100)
    _created_at = models.DateTimeField(auto_now_add=True)

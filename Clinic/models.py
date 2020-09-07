from django.db import models


class ClinicBase(models.Model):
    clinicID = models.AutoField(primary_key=True)
    clinicName = models.CharField(max_length=100)
    _created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.clinicName


class Availability(models.Model):
    availabilityID = models.AutoField(primary_key=True)
    dateAndTime = models.DateTimeField(auto_now=False, auto_now_add=False)
    _created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dateAndTime.__str__()


class Vet(models.Model):
    vetID = models.AutoField(primary_key=True)
    vetName = models.CharField(max_length=100)
    _created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vetName


class TakenSlots(models.Model):
    class Meta:
        unique_together = (('vetID', 'availabilityID', 'clinicID'),)

    takenID = models.AutoField(primary_key=True)
    vetID = models.ForeignKey(Vet, on_delete=models.CASCADE)
    availabilityID = models.ForeignKey(Availability, on_delete=models.CASCADE)
    clinicID = models.ForeignKey(ClinicBase, on_delete=models.CASCADE)
    _created_at = models.DateTimeField(auto_now_add=True)

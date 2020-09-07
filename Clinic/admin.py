from django.contrib import admin
from .models import ClinicBase, TakenSlots, Availability, Vet

admin.site.register([ClinicBase, TakenSlots, Availability, Vet])

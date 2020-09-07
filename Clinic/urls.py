from django.urls import path
from Handlers.configHandler import *
from Clinic import views

configs = ConfigHandler.load_config('config.yaml')

API_PATH = configs['api']['title'] + '/' + configs['api']['version'] + '/' + configs['api']['backend']['clinicAPI']['name']

API_AVAILABILITY = API_PATH + '/' + configs['api']['backend']['clinicAPI']['sub']['availability']
API_VET = API_PATH + '/' + configs['api']['backend']['clinicAPI']['sub']['vet']
API_CLINIC = API_PATH + '/' + configs['api']['backend']['clinicAPI']['sub']['basic']

urlpatterns = [
    path(API_AVAILABILITY, views.AvailabilityList.as_view()),
    path(API_AVAILABILITY + '/<int:ID>', views.AvailabilityDetails.as_view()),

    path(API_VET, views.VetList.as_view()),
    path(API_VET + '/<int:ID>', views.VetDetails.as_view()),

    path(API_CLINIC, views.ClinicList.as_view()),
    path(API_CLINIC + '/<int:ID>', views.ClinicDetails.as_view()),
]



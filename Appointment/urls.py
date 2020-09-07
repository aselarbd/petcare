from django.urls import path
from Handlers.configHandler import *
from Appointment import views

configs = ConfigHandler.load_config('config.yaml')

API_PATH = configs['api']['title'] + '/' + configs['api']['version'] + '/' + configs['api']['backend']['appointmentAPI']['name']

urlpatterns = [
    path(API_PATH, views.AppointmentList.as_view()),
    path(API_PATH + '/<int:ID>', views.AppointmentDetails.as_view()),
]



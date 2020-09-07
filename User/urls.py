from django.urls import path
from Handlers.configHandler import *
from User import views

configs = ConfigHandler.load_config('config.yaml')

API_PATH = configs['api']['title'] + '/' + configs['api']['version'] + '/' + configs['api']['backend']['userAPI']['name']

urlpatterns = [
    path(API_PATH, views.UserList),
    path(API_PATH + '/<int:ID>', views.UserDetails.as_view()),
]



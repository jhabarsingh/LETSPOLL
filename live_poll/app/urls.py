from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.admin_login, name='login'),
    path('create_poll/', views.create_poll, name='create_poll'),
    path('show_polls/', views.show_polls, name='show_polls'),
    path('save_poll/', views.save_poll, name='save_poll'),
    path('polling/<uuid:id>/', views.polling, name='polling'),
    path('logout/', views.admin_logout, name='logout'),
    path('poll_result/<uuid:id>/', views.poll_result, name='poll_result'),
    path('get_data/<uuid:id>/', views.get_data, name='get_data'),
]

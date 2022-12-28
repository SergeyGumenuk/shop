from django.urls import path

from payment import views


app_name = 'payment'


urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('completed/', views.payment_completed, name='complete'),
    path('canceled/', views.payment_canceled, name='canceled'),
]
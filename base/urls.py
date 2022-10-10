from django.urls import path
from . import views

urlpatterns = [
    path('',views.train_no,name='train_no'),
    path('full_status',views.full_status,name='full_status')
]

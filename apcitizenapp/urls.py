from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepageview.as_view(), name='home'),
    path('aadharregister/', views.register, name='aadharregister'),
    path('voterregister/', views.voterregisterview, name='voterregister'),
    # path('login/', views.login, name='login'),
    # path('accounts/login/', views.login, name='login'),
    path('getaadhar/<int:aadhar_num>', views.getaadhar, name='getaadhar'),
    path('getaadhar/', views.getaadhar, name='getaadhar'),
    path('voteformla/', views.voteformla, name='voteformla'),
    path('voteformp/',views.voteformp, name='voteformp'),
]

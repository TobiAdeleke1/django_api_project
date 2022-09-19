from django.urls import path
from users_auth import views

urlpatterns =[

    path('signup/',views.CreateUserView.as_view(), name = 'sign_up'),
    
]
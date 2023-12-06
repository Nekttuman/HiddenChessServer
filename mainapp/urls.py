from django.urls import path, include
from . import views

urlpatterns = [

    path('login/', views.api_login_view),  # URL для входа
        path('register/', views.api_register_view),  # URL для входа

    path('gameroom/', include('gameroom.urls')),
    # path('', views.index),
    path('check-connection/', views.check_connection),
]

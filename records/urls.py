from django.urls import path
from records import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),   
    path('users', views.display, name="display"),
    path('more', views.more, name="more"),
    path('next', views.next, name="next"),
    path('previous', views.previous, name="previous"),

]
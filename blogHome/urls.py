from django.urls import path,include
from .import views
urlpatterns = [
   
    path('',views.home,name='home'),
    path('content/<pk>',views.content,name='content'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),

]

from django.urls import path,include
from .import views
urlpatterns = [
   
    path('',views.home,name='home'),
    path('content/<pk>',views.content,name='content'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('comment/',views.comment,name='comment'),
    path('replay/',views.replay,name='reply'),

]

from django.urls import path
from Base_App import views

# Template Defining (templates inside the folder)
app_name = 'basic_app'

urlpatterns = [
    #Templates In Other Folder
    path('',views.base_index,name="base_index"),
    path('base_other/',views.base_other,name="base_other"),
    path('base_relative/',views.base_relative,name="base_relative"),
    path('register/',views.register,name="register"),
    path('logout/',views.user_logout,name="logout"),
    path('special/',views.special,name='special'),
    path('user_login/',views.user_login,name='user_login'),
]

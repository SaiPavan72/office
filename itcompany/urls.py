from django.urls import path
from itcompany import views

urlpatterns = [
    path('',views.main,name='main'),
    path('apply/',views.apply,name='apply'),
    path('save_application/',views.save_application,name='save_application'),
    path('login/',views.login_request,name='login'),
    path('registration/',views.registration,name='registration'),
    path('details/',views.employee_details,name='details'),
    path('save_register/',views.save_register,name='save-register'),
    path('login_page/',views.login_user,name='save-login_page'),
    path('accept/',views.application_permission,name='application_accept'),
    path('<int:id>/applied/',views.applied_details,name='application_accept'),


]
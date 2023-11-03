from django.urls import path
from firstapp import views


app_name='firstapp'
urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('profile/',views.profile,name='profile'),
    path('student_details/<pk>/',views.StudentDetail.as_view(),name='student_details'),
   
]
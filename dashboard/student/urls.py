from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.student_login, name='student_login'),
    path('home/', views.home, name='home'),
    path('notices/', views.student_notice, name='student_notice'), 
    path('course_materials/', views.show_course_material, name='student_course_material'),
    path('view_marks/', views.view_marks, name='student_view_marks'),

]

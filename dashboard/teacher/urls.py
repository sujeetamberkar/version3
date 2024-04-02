from django.urls import path
from . import views
from .views import enter_update_marks


urlpatterns = [
    path('login/', views.teacher_login, name='teacher_login'),
    path('home/', views.home, name='teacher_home'),  # This line defines the 'teacher_home' URL name
    path('notice/', views.teacher_notice, name='teacher_notice'),
    path('add_course_material/', views.add_course_material, name='teacher_course_material'),
    path('enter_marks/', views.enter_update_marks, name='enter_update_marks'),



]

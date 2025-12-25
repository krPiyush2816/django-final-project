from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Path for exam submission logic
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    
    # Path for displaying the final exam result
    path('course/<int:course_id>/submission/<int:submission_id>/result/', 
         views.show_exam_result, name='show_exam_result'),
]

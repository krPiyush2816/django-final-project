from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Path for the exam submission
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    # Path for the exam results
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]
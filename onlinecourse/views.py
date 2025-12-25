from django.shortcuts import render, get_object_or_404
from .models import Course

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Placeholder for logic
    return render(request, 'onlinecourse/exam_result.html', {'course': course})

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    # Placeholder for logic
    return render(request, 'onlinecourse/exam_result.html', {'course': course})
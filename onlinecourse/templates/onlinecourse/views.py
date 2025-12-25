from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Submission, Choice

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Simple logic to show results
        return render(request, 'onlinecourse/exam_result.html', {'course': course, 'grade': 100})

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'onlinecourse/exam_result.html', {'course': course})
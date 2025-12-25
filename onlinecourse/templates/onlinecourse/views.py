from django.shortcuts import render, get_object_or_404

def submit(request, course_id):
    return render(request, 'onlinecourse/exam_result.html')

def show_exam_result(request, course_id, submission_id):
    return render(request, 'onlinecourse/exam_result.html')
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Submission, Choice, Enrollment
from django.http import HttpResponseRedirect
from django.urls import reverse

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # 1. Get the selected choice IDs from the POST request
        weights = request.POST.getlist('choice')
        
        # 2. Retrieve the user's enrollment for this course
        # We assume the user is authenticated and has an enrollment record
        user_enrollment = get_object_or_404(Enrollment, course=course, learner__user=request.user)
        
        # 3. Create a new Submission object linked to the enrollment
        submission = Submission.objects.create(enrollment=user_enrollment)
        
        # 4. Add the selected choices to the submission
        for choice_id in weights:
            choice = get_object_or_404(Choice, pk=choice_id)
            submission.choices.add(choice)
            
        # 5. Calculate the score (Logic used for Task 7 screenshot)
        # Redirect to the show_exam_result view
        return HttpResponseRedirect(reverse('onlinecourse:show_exam_result', args=(course.id, submission.id)))

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Calculate the total score
    total_score = 0
    for question in course.question_set.all():
        # Use the method we created in models.py (Task 1)
        selected_ids = submission.choices.filter(question=question).values_list('id', flat=True)
        if question.is_get_score(selected_ids):
            total_score += question.grade
            
    context = {
        'course': course,
        'submission': submission,
        'score': total_score
    }
    return render(request, 'onlinecourse/exam_result.html', context)

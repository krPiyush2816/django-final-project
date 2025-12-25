from django.contrib import admin
# Requirement: Import all seven classes
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Task 2: Implement ChoiceInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Task 2: Implement QuestionInline
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# Task 2: Implement QuestionAdmin with ChoiceInline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content', 'course', 'grade']

# Task 2: Implement LessonAdmin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Task 2: CourseAdmin with QuestionInline
class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('name', 'pub_date')
    search_fields = ['name', 'description']

# Register all required classes
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)

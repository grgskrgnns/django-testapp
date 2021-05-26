from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text']
    inlines = [ChoiceInline]

# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Instructor)
admin.site.register(Learner)

from django.contrib import admin
from .models import Exam ,Question

# Register your models here.


class ExamAdmin(admin.ModelAdmin):

    list_display = ["exam_course","exam_title", "publishing_date", "deadline_date", "start_date", "professor"]
    list_display_links = ["exam_title"]
    list_filter = ["publishing_date", "deadline_date"]
    search_fields = ["title", "content"]
    class Meta:
        model=Exam

admin.site.register(Exam,ExamAdmin)

class QuestionAdmin(admin.ModelAdmin):

    list_display = ["question_content", "belonged_exam"]
    list_display_links = ["belonged_exam"]
    search_fields = ["belonged_exam", "question_content"]
    class Meta:
        model=Question

admin.site.register(Question,QuestionAdmin)




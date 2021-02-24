from django import forms
from .models import Exam,Question

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class ExamCreateForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields=[
            "exam_course",
            "exam_title",
            "start_date",
            "deadline_date",
        ]
        widgets = {
            'start_date':DateInput(),
            'deadline_date': DateInput(),
        }

class ExamAssignStudentForm(forms.ModelForm):
    class Meta:
        model=Exam
        fields=[
            "assigned_students",
        ]

class ExamAssignQuestionForm(forms.ModelForm):
    class Meta:
        model=Exam
        fields=[
            "exam_title",
        ]

class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model=Question
        fields =[
            "question_content",
            "option_1",
            "option_2",
            "option_3",
            "option_4",
            "right_option"
        ]

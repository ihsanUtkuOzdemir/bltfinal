from django.urls import path
from .views import *

app_name='exam'

urlpatterns = [
    path('index', exam_index, name="index"),
    path('index2', exam_index2, name="index2"),
    path('<int:id>', exam_detail, name="detail"),
    path('<int:id>start', exam_start, name="start"),
    path('create', exam_create, name="create"),
    path('<int:id>/update', exam_update, name='update'),
    path('<int:id>/delete', exam_delete, name="delete"),
    path('<int:id>/assign_student', assign_student, name="assign_student"),
    path('<int:id>/assign_question', assign_question, name="assign_question"),
    path('question_create', question_create, name="create_question"),
]
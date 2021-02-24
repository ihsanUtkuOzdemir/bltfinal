from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Exam(models.Model):
    professor = models.ForeignKey('auth.User', verbose_name="Yayınlayan", on_delete=models.CASCADE ,related_name="exams")
    exam_course = models.CharField(max_length=120, verbose_name="Ders")
    exam_title = models.CharField(max_length=120, verbose_name="Başlık")
    publishing_date = models.DateTimeField(verbose_name="Yayınlanma Tarihi", auto_now_add=True)
    start_date = models.DateTimeField(verbose_name="Başlangıç Tarihi")
    deadline_date = models.DateTimeField(verbose_name="Bitiş Tarihi")
    assigned_students = models.ManyToManyField(User)

    def __str__(self):
        return self.exam_title

    def is_past_due(self):
        if self.deadline_date > self.start_date:
            return True
        return False

    def get_absolute_url(self):
        return  reverse('exam:detail',kwargs={'id':self.id})
    def get_start_url(self):
        return  reverse('exam:start',kwargs={'id':self.id})
    def get_update_url(self):
        return  reverse('exam:update',kwargs={'id':self.id})
    def get_delete_url(self):
        return  reverse('exam:delete',kwargs={'id':self.id})
    def get_assign_question_url(self):
        return  reverse('exam:assign_question',kwargs={'id':self.id})
    def get_assign_student_url(self):
        return  reverse('exam:assign_student',kwargs={'id':self.id})


    class Meta:
        ordering=["publishing_date","id"]


class Question(models.Model):
    belonged_exam = models.ForeignKey("exam.Exam",related_name="belonged_exam",on_delete=models.CASCADE)
    question_content = models.TextField(verbose_name="Soru İçeriği")
    option_1 = models.TextField(verbose_name="Soru Şıkkı 1")
    option_2 = models.TextField(verbose_name="Soru Şıkkı 2")
    option_3 = models.TextField(verbose_name="Soru Şıkkı 3")
    option_4 = models.TextField(verbose_name="Soru Şıkkı 4")
    right_option = models.IntegerField(verbose_name="Doğru Şık")

    def __str__(self):
        return self.question_content

    def get_absolute_url(self):
        return  reverse('exam:question_detail',kwargs={'id':self.id})
    def get_update_url(self):
        return  reverse('exam:question_update',kwargs={'id':self.id})
    def get_delete_url(self):
        return  reverse('exam:question_delete',kwargs={'id':self.id})


    class Meta:
        ordering=["belonged_exam","id"]



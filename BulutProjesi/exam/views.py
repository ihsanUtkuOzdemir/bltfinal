from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from django.utils import timezone

from exam.form import ExamCreateForm, QuestionCreateForm, ExamAssignStudentForm, ExamAssignQuestionForm
from exam.models import Exam


def exam_index (request):
    if not request.user.is_authenticated:
        raise Http404()
    #tasks_list= Task.objects.all()
    exam_list = Exam.objects.all().filter(assigned_students=request.user,start_date__lt=timezone.now(),deadline_date__gt=timezone.now())
    #tasks=request.user.tasks.all()
    query = request.GET.get("q")
    if query:
        exam_list = exam_list.filter(Q(exam_title__icontains=query) |
                                       Q(exam_course__icontains=query)
                                       ).distinct()

    paginator = Paginator(exam_list, 9)

    page_number = request.GET.get('page')
    exams = paginator.get_page(page_number)
    return render(request,"Exam/index.html",{"exams":exams})

def exam_index2 (request):
    if not request.user.is_authenticated:
        raise Http404()
    #tasks_list= Task.objects.all()
    exam_list = request.user.exams.all()
    #tasks=request.user.tasks.all()
    query = request.GET.get("q")
    if query:
        exam_list = exam_list.filter(Q(exam_title__icontains=query) |
                                       Q(exam_course__icontains=query)
                                       ).distinct()

    paginator = Paginator(exam_list, 9)

    page_number = request.GET.get('page')
    exams = paginator.get_page(page_number)
    return render(request,"Exam/index2.html",{"exams":exams})


def exam_detail (request,id):
    if not request.user.is_authenticated:
        raise Http404()
    exam=get_object_or_404(Exam,id=id)
    context= {
        'exam':exam,
    }
    return render(request,"Exam/detail.html",context)

def exam_start (request,id):
    if not request.user.is_authenticated:
        raise Http404()
    exam=get_object_or_404(Exam,id=id)
    context= {
        'exam':exam,
    }
    return render(request,"Exam/start.html",context)

def exam_create (request):
    if not request.user.is_authenticated:
        raise Http404()
    form = ExamCreateForm(request.POST or None)
    if form.is_valid():
        exam=form.save(commit=False)
        exam.professor=request.user
        exam.save()
        messages.success(request,"Exam Oluşturulmuştur!")
        return HttpResponseRedirect(exam.get_assign_question_url())
    context={
        "form":form,
    }
    return render(request,"Exam/form.html",context)

def exam_update (request, id):
    if not request.user.is_authenticated:
        raise Http404()
    exam = get_object_or_404(Exam, id=id)
    form = ExamCreateForm(request.POST or None,request.FILES or None, instance=exam)
    if form.is_valid():
        exam=form.save()
        messages.success(request, "Sınav Güncellenmiştir!!")
        return HttpResponseRedirect(exam.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request,"Exam/form.html",context)

def exam_delete (request,id):
    if not request.user.is_authenticated:
        raise Http404()
    exam = get_object_or_404(Exam, id=id)
    exam.delete()

    return redirect("exam:index")

def assign_question (request, id):
    if not request.user.is_authenticated:
        raise Http404()
    exam = get_object_or_404(Exam, id=id)
    form = QuestionCreateForm(request.POST or None)
    if form.is_valid():
        question = form.save(commit=False)
        question.belonged_exam=exam
        question.save()
        messages.success(request, "Sorular Eklendi!!")
        return HttpResponseRedirect(exam.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request,"Exam/form.html",context)

def assign_student (request, id):
    if not request.user.is_authenticated:
        raise Http404()
    exam = get_object_or_404(Exam, id=id)
    form = ExamAssignStudentForm(request.POST or None, instance=exam)
    if form.is_valid():
        exam=form.save()
        messages.success(request, "Öğrenciler Atandı!!")
        return HttpResponseRedirect(exam.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request,"Exam/form.html",context)

def question_create (request):
    if not request.user.is_authenticated:
        raise Http404()
    form = QuestionCreateForm(request.POST or None)
    if form.is_valid():
        question=form.save(commit=False)
        question.save()
        messages.success(request,"Question Oluşturulmuştur!")
        return HttpResponseRedirect(question.get_absolute_url())
    context={
        "form":form,
    }
    return render(request,"Exam/form.html",context)
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from .models import Question
from .forms import QuestionForm, AnswerForm
# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'board/question_list.html',context)

# 질문 상세
def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'board/question_detail.html',context)

# 답변 달기
def answer_create(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method=='POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('board:detail',question_id=question_id)
    else:
        return HttpResponseNotAllowed('Only POST is possible')
    context = {'question':question, 'form':form}
    return render(request,'board/question_detail.html',context)
# 질문 생성
def question_create(request):
    if request.method=='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'board/question_form.html',context)
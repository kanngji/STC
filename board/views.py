from django.shortcuts import render, get_object_or_404,redirect

from django.utils import timezone
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

last_page_num = 0

# Create your views here.

def index(request):
    page = request.GET.get('page','1') # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    max_index = len(paginator.page_range)
    page_obj = paginator.get_page(page)
    context = {'question_list':page_obj,'max_index':max_index}
    return render(request, 'board/question_list.html',context)

# 질문 상세
def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'board/question_detail.html',context)

# 답변 달기
@login_required(login_url='common:login')
def answer_create(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method=='POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('board:detail',question_id=question_id)
    else:
        form = AnswerForm()
    context = {'question':question, 'form':form}
    return render(request,'board/question_detail.html',context)
# 질문 생성
@login_required
def question_create(request):
    if request.method=='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'board/question_form.html',context)
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404,redirect

from ..models import Question
last_page_num = 0
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
from django.shortcuts import render, redirect


from .models import Topic
from .forms import TopicForm


# Create your views here.
def index(request):
    '''학습 로그의 홈 페이지'''
    return render(request, 'learning_logs/index.html')

def topics(request):
    '''모든 주제를 표시하는 페이지'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    '''특정 주제와 관련된 모든 항목을 표시하는 페이지'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    '''새로운 주제를 추가하는 페이지'''
    if request.method != 'POST':
        # 데이터가 제출되지 않은 경우, 빈 양식을 생성한다.
        form = TopicForm()
    else:
        # POST 데이터로 양식을 처리한다.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # 빈 양식 또는 잘못된 양식을 표시한다.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

# 소개글로 들어가는는
def about_me(request):
    return render(request, 'learning_logs/about_me.html')

# 관심사로 들어가는는
def interest_me(request):
    return render(request, 'learning_logs/interest_me.html')

from django.shortcuts import render
from django.http import HttpResponse

from .NLP import helloworld
from .NLP import predict

# database
from testpredict.models import Taskclassification as task_class
from .forms import TodoForm

# Create your views here.

def index(request):
    
    return PostTodo(request)
    #textpredict()
    #return HttpResponse("index page")

def todo(request):
    return HttpResponse("todo page")

def textpredict(todo_text):
    #print("test")
    #helloworld.helloworld()
    #entry = task_class.objects.get(pk=1)
    #entry = task_class.
    entry = task_class(todo_text=todo_text, todo_pred='other')
    pred = predict.predict(entry.todo_text)
    entry.todo_pred = pred
    entry.save()
    return pred

def PostTodo(request):
    #POST時処理
    if request.method == "POST":
        # Formのデータを用いTodoFormを再構築
        form = TodoForm(request.POST)
        # Formの値チェック
        if form.is_valid():
            return HttpResponse(textpredict(request.POST['todo_text']))
    # 初めてのアクセス
    else:
        print("!!!!!!!!!!!!!!!!!!!")
        # Formを新しくつくる
        form = TodoForm()

    return render(request, 'testpredict/todo.html', {'form': form})

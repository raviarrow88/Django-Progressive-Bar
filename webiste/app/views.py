from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
# Create your views here.
from .tasks import generate_users,task_status
from celery.result import AsyncResult
import time,json
from django.views.decorators.csrf import csrf_exempt
from celery.app.task import Task
from core.celery import app
# import tasks
def home(request):
    context={}
    return render(request,'form.html',context)

from .forms import CreateUserForm

@csrf_exempt
def create_user(request,*args,**kwargs):

    total=  request.POST.get('count')

    task = generate_users.delay(int(total))

    context = {"task_id":task.task_id }

    return JsonResponse(context)

# def get_id(task):



def getstate(self,task_id):
    result = AsyncResult(task_id)
    data= {
    'state':result.state,
    'meta_info':result.info
    }
    return HttpResponse(json.dumps(data),content_type='application/json')


def updatetask(self,task_id,status):
    # task_status.delay(task_id,status)
    result = AsyncResult(task_id)
    result.state='PAUSED'
    data= {
    'state':result.state,
    'meta_info':result.info
    }
    return HttpResponse(json.dumps(data),content_type='application/json')

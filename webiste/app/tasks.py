
from __future__ import absolute_import
from celery.decorators import task
from .emails import send_feedback_mail
from celery import shared_task
import time
import json
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
import string
from django.utils import timezone

@task
def generate_users(total):
    for i in range(total):
        username = "User_{}".format(get_random_string(6,string.ascii_letters))
        email = "{}@test.com".format(username)
        password = get_random_string(8)
        user = User.objects.create_user(username=username,email=email,password=password)


        c = User.objects.exclude(date_joined=timezone.now()).count()
        percent = int(100*c/total)

        

        generate_users.update_state(state='PROGRESS',meta={'total':total,'done':c,'percent':percent})
        time.sleep(2)

    return "Users Created"



@task
def task_status(status,task_id):
    if status == 'pause':
        task_status.update_state(state='PAUSED',task_id=task_id)
        time.sleep(100)
        # return HttpResponse(json.dumps(data),content_type='application/json')
    if status == 'resume':
        task_status.update_state(state='PROGRESS',task_id=task_id)

    return 'status changed'

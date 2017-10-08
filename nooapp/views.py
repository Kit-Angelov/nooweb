from django.shortcuts import render
from django.http import HttpResponse
from .telegram import send_telegram
from .models import Call
from datetime import datetime


def index(request):
    return render(request, 'nooapp/index.html')


def call(request):
    if request.method == 'GET':
        form = request.GET
        name = form.get('name')
        if name == '':
            name = 'нема имени'
        phone = form.get('phone')
        if phone == '':
            phone = 'нема телефона'
        message = form.get('message')
        if message == '':
            message = 'нема сообщения'
        print(form)
        call = Call(name=name, phone=phone, message=message)
        call.save()
        send_telegram(name=name,
                      phone=phone,
                      message=message,
                      date=datetime.now().strftime("%Y.%m.%d %H:%M"))
    return HttpResponse(content='ok', content_type="text/html")


def conf(request):
    return render(request, 'nooapp/conf.html')

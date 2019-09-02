from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from user.models import User
from . import models


# Create your views here.
def check_login(fn):
    def wrap(request, *args, **kwargs):
        if not hasattr(request, 'session'):
            return HttpResponseRedirect('/user/login')
        if 'user' not in request.session:
            return HttpResponseRedirect('/user/login')
        return fn(request, *args, **kwargs)

    return wrap


def list_view(request):
    if not hasattr(request, 'session'):
        return HttpResponseRedirect('/user/login')
    if 'user' not in request.session:
        return HttpResponseRedirect('/user/login')
    user_id = request.session['user']['id']
    auser = User.objects.get(id=user_id)
    notes = auser.note_set.all()
    return render(request, 'note/list_note.html', locals())


@check_login
def add_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        user_id = request.session['user']['id']
        auser = User.objects.get(id=user_id)
        anote = models.Note(user=auser)
        anote.title = title
        anote.content = content
        anote.save()
        return HttpResponseRedirect('/note/')


@check_login
def mod_view(request, id):
    user_id = request.session['user']['id']
    auser = User.objects.get(id=user_id)
    anote = models.Note.objects.get(user=auser, id=id)
    if request.method == 'GET':
        return render(request, 'note/mod_note.html', locals())
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        anote.title = title
        anote.content = content
        anote.save()
        return HttpResponseRedirect('/note')


@check_login
def del_view(request, id):
    user_id = request.session['user']['id']
    print(user_id)
    auser = User.objects.get(id=user_id)
    anote = models.Note.objects.get(user=auser, id=id)
    anote.delete()
    return HttpResponseRedirect('/note')

import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from tools.login_check import login_check
from topic.models import Topic


# http://127.0.0.1:5000/xixi/topic/release
@login_check("POST")
def topics(request, author_id):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        json_str = request.body
        if not json_str:
            result = {'code': 301, 'error': 'Please give me json!'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)

        title = json_obj.get('title')
        if not title:
            result = {'code': 302, 'error': 'Please give me title!'}
            return JsonResponse(result)

        content = json_obj.get('content')
        if not content:
            result = {'code': 303, 'error': 'Please give me content!'}
            return JsonResponse(result)

        content_text = json_obj.get('content_text')
        if not content_text:
            result = {'code': 304, 'error': 'Please give me content_text!'}
            return JsonResponse(result)
        introduce = content_text[:30]

        limit = json_obj.get('limit')
        if limit not in ['public', 'private']:
            result = {'code': 305, 'error': 'Please give me limit!'}
            return JsonResponse(result)

        category = json_obj.get('category')
        if category not in ['No-tec', 'tec']:
            result = {'code': 306, 'error': 'Please give me category!'}
            return JsonResponse(result)

        Topic.objects.create(title=title, category=category, limit=limit, content=content, introduce=introduce,
                             author=request.user)
        result = {'code': 200, 'username': request.user.username}
        return JsonResponse(result)

    return JsonResponse({'code': 200, 'error': 'This is test!'})

import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from message.models import Message
from tools.login_check import login_check
from topic.models import Topic


@login_check('POST')
def messages(request, topic_id):
    if request.method != 'POST':
        result = {'code': 401, 'error': 'Please use POST!'}
        return JsonResponse(result)
    user = request.user
    json_str = request.body
    json_obj = json.loads(json_str)
    # print(json_obj)
    content = json_obj.get('content')
    if not content:
        result = {'code': 402, 'error': 'Please give me content!'}
        return JsonResponse(result)
    parent_id = json_obj.get('parent_id','0')
    try:
        topic = Topic.objects.get(id=topic_id)
    except:
        # topic被删除 或者topic_id 不真实
        result = {'code': 403, 'error': 'The topic is not exist!'}
        return JsonResponse(result)
    if topic.limit == 'private':
        if user.username != topic.author.username:
            result = {'code': 404, 'error': 'Please GET OUT!'}
            return JsonResponse(result)
    Message.objects.create(content=content, publisher_id=user, topic_id=topic, parent_message=parent_id)
    return JsonResponse({'code': 200, 'data': {}})



def get_message(parent_message,l):
    '''
        messages = {
        "id": 1,
        "content": "<p>写得不错啊,大哥<br></p>",
        "publisher": "guoxiaonao",
        "publisher_avatar": "avatar/头像 2.png",
        "reply": [
            {
                "publisher": author_topic.author,
                "publisher_avatar": "avatar/头像 2.png",
                "created_time": "2019-06-03 07:52:16",
                "content": "谢谢您的赏识",
                "msg_id": 2
            }
        ],
        "created_time": "2019-06-03 07:52:02"
    }
    :param parent_message:
    :param l:
    :return:
    '''
    p_list=[]
    child_dict={}
    for i in l:
        if i.parent_message==0:
            p_list.append(i)
        else:
            if parent_message in child_dict:
                child_dict['parent_message'].append(i)
            else:
                child_dict['parent_message'] =[]
                child_dict['parent_message'].append(i)
            # 可以简写成
            child_dict.setdefault(parent_message,[])
            child_dict['parent_message'].append(i)
    for p in p_list:
        if p['id'] in child_dict:
            p['reply']=child_dict[p['id']]
    return messages



'''
    if parent_message in child_dict:
        child_dict['parent_message'].append(i)
    else:
        child_dict['parent_message'] =[]
        child_dict['parent_message'].append(i)
    可以简写成 
    child_dict.setdefault(parent_message,[])
    child_dict['parent_message'].append(i)
'''
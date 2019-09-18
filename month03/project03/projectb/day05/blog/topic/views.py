import json

from django.http import JsonResponse
from django.shortcuts import render

from message.models import Message
from tools.login_check import login_check, get_user_by_request
from topic.models import Topic
from user.models import UserProfile


# Create your views here.
# http://127.0.0.1:5000/xixi/topic/release

@login_check("POST", 'DELETE')
def topics(request, author_id):
    if request.method == "GET":
        # print(author_id)
        authors = UserProfile.objects.filter(username=author_id)
        if not authors:
            result = {'code': 308, 'error': 'There is no author!'}
            return JsonResponse(result)
        author = authors[0]
        visitor = get_user_by_request(request)
        visitor_name = None
        if visitor:
            visitor_name = visitor.username

        # http://127.0.0.1:8000/v1/topics/xixi?category=tec&t_id=18
        t_id = request.GET.get('t_id')
        if t_id:
            is_self = False  # #先默认false（为访客访问）
            # 获取详情
            t_id = int(t_id)
            if author_id == visitor_name:
                # 博主访问自己的博客
                is_self = True
                try:
                    author_topic = Topic.objects.get(id=t_id)
                    # print(author_topic)
                    # for i in author_topic:
                    #     print(i)
                except Exception as e:
                    result = {'code': 312, 'error': 'There is no topic!'}
                    return JsonResponse(result)
            else:
                try:
                    author_topic = Topic.objects.get(id=t_id, limit='public')
                except Exception as e:
                    result = {'code': 313, 'error': 'There is no topic!'}
                    return JsonResponse(result)
            result = make_topic_result(author, is_self, author_topic)
            return JsonResponse(result)

        else:
            # 部分数据 http://127.0.0.1: 8000/v1/topics/<author_id>?category=[tec|no-tec]
            # http://127.0.0.1:5000/xixi/topics/<author_id>?category=[tec|no-tec]
            category = request.GET.get('category')
            if category in ['tec', 'no-tec']:
                if author_id == visitor_name:
                    topics = Topic.objects.filter(author_id=author_id, category=category)
                else:
                    topics = Topic.objects.filter(author_id=author_id, limit='public', category=category)
            else:
                # 全量数据http://127.0.0.1:8000/v1/topics/<author_id>
                # http://127.0.0.1:5000/xixi/topics
                if author_id == visitor_name:
                    topics = Topic.objects.filter(author_id=author_id)
                else:
                    topics = Topic.objects.filter(author_id=author_id, limit='public')
            result = make_topics_result(author, topics)
            return JsonResponse(result)

    elif request.method == "POST":
        json_str = request.body
        if not json_str:
            result = {'code': 301, 'error': 'Please give me json!'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        title = json_obj.get('title')

        # # # xss注入
        import html
        # # # 进行转义
        title = html.escape(title)

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
        if category not in ['no-tec', 'tec']:
            result = {'code': 306, 'error': 'Please give me category!'}
            return JsonResponse(result)

        Topic.objects.create(title=title, category=category, limit=limit, content=content, introduce=introduce,
                             author=request.user)
        result = {'code': 200, 'username': request.user.username}
        return JsonResponse(result)

    # delete
    elif request.method == "DELETE":
        author = request.user
        token_author_id = author.username
        if author_id != token_author_id:
            result = {'code': 309, 'error': 'You don`t have privilege!'}
            return JsonResponse(result)
        topic_id = request.GET.get('topic_id')

        try:
            topic = Topic.objects.get(id=topic_id)
        except:  # #可能已经被删除
            result = {'code': 310, 'error': 'There is no topic!'}
            return JsonResponse(result)

        if topic.author.username != author_id:
            result = {'code': 311, 'error': 'You don`t have privilege!!!'}
            return JsonResponse(result)

        topic.delete()
        res = {'code': 200}
        return JsonResponse(res)

    return JsonResponse({'code': 200, 'error': 'This is test!'})


def make_topics_result(author, topics):
    result = {'code': 200, 'data': {}}
    data = {}
    data['nickname'] = author.nickname
    topics_list = []
    for topic in topics:
        d = {}
        d['id'] = topic.id
        d['category'] = topic.category
        d['title'] = topic.title
        d['introduce'] = topic.introduce
        d['author'] = author.nickname  # ##注意关键字
        d['created_time'] = topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
        topics_list.append(d)
    data['topics'] = topics_list
    result['data'] = data
    return result


# http://127.0.0.1:5000/xixi/topics/detail/1
def make_topic_result(author, is_self, author_topic):
    '''
    拼接详情页
    :param author_id:
    :param is_self:
    :param author_topic:
    :return:
    '''
    # print(author)
    # print(author_topic)
    # print(is_self)
    if is_self:
        next_topic = Topic.objects.filter(id__gt=author_topic.id, author=author).first()
        last_topic = Topic.objects.filter(id__lt=author_topic.id, author=author).last()
    else:
        next_topic = Topic.objects.filter(id__gt=author_topic.id, author=author, limit='public').first()
        last_topic = Topic.objects.filter(id__lt=author_topic.id, author=author, limit='public').last()

    if next_topic:
        next_id = next_topic.id
        next_title = next_topic.title
    else:
        next_id = None
        next_title = None

    if last_topic:
        last_id = last_topic.id
        last_title = last_topic.title
    else:
        last_id = None
        last_title = None

    all_messages = Message.objects.filter(topic_id=author_topic).order_by('-created_time')
    msg_list = []
    reply_dict = {}
    msg_count = 0
    for msg in all_messages:
        msg_count += 1
        if msg.parent_message == 0:
            msg_list.append({'id': msg.id,
                             'content': msg.content,
                             'publisher_id': msg.publisher_id.nickname,
                             'publisher_avatar': str(msg.publisher_id.avatar),
                             'created_time': msg.created_time.strftime('%Y-%m-%d'),
                             'reply': []
                             })
        else:
            reply_dict.setdefault(msg.parent_message, [])
            reply_dict[msg.parent_message].append({'msg_id': msg.id,
                                                   'content': msg.content,
                                                   'publisher_id': msg.publisher_id.nickname,
                                                   'publisher_avatar': str(msg.publisher_id.avatar),
                                                   'created_time': msg.created_time.strftime('%Y-%m-%d'),
                                                   })
    for _msg in msg_list:
        if _msg['id'] in reply_dict:
            _msg['reply'] = reply_dict[_msg['id']]

    result = {'code': 200, 'data': {}}
    data = result['data']
    data['nickname'] = author.nickname
    data["title"] = author_topic.title
    data["category"] = author_topic.category
    data["created_time"] = author_topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
    data["content"] = author_topic.content
    data["introduce"] = author_topic.introduce
    data["author"] = author.nickname
    data["next_id"] = next_id
    data["next_title"] = next_title
    data["last_id"] = last_id
    data["last_title"] = last_title
    data["messages"] = msg_list
    data["messages_count"] = msg_count
    return result

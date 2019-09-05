import redis
from django.http import JsonResponse

from user.models import UserProfile


def test_api(request):
    # r = redis.Redis('localhost', 6379, 0)
    # while True:
    #     try:
    #         with r.lock('xixi', blocking_timeout=3):
    #             u = UserProfile.objects.get(username='xixi')
    #             u.score += 1
    #             u.save()
    #         break
    #     except Exception as e:
    #         return JsonResponse({'code': 000, 'error': 'error!'})

    u = UserProfile.objects.get(username='xixi')
    u.score += 1
    u.save()
    return JsonResponse({'code': 200})

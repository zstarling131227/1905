import jwt
from django.http import JsonResponse
from user.models import UserProfile

key = '1234567'


# login_check('PUT','GET','POST')
def login_check(*methods):  # ()内为参数
    def _login_check(func):
        def wrapper(request, *args, **kwargs):
            # request.META.get()获取前端传来的token(也就是authorization)
            token = request.META.get('HTTP_AUTHORIZATION')
            if request.method not in methods:
                return func(request, *args, **kwargs)  # #返回常规视图函数
            if not token:
                result = {'code': 107, 'error': 'Please login/give me token!'}
                return JsonResponse(result)
            try:
                res = jwt.decode(token, key, algorithms="HS256")
            except jwt.ExpiredSignatureError:
                # token过期了
                result = {'code': 108, 'error': 'Please login！'}
                return JsonResponse(result)
            except Exception as e:  # 为了防止其他异常出现，再次抓取异常
                result = {'code': 109, 'error': 'Please login！'}
                return JsonResponse(result)
            username = res['username']
            try:
                user = UserProfile.objects.get(username=username)
            except:
                user = None
            if not user:
                result = {'code': 110, 'error': 'There is no user！'}
                return JsonResponse(result)
            request.user = user
            return func(request, *args, **kwargs)

        return wrapper

    return _login_check


def _login_check(func):
    def wrapper():
        return func()

    return wrapper

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.http import Http404
import re

class MyMV(MiddlewareMixin):
    def process_request(self, request):
        print('中间件 process_request方法被调用！')
        print('路由是', request.path)
        print('请求方式是', request.method)
        return HttpResponse('XXXXX')
        # if request.path == '/aaaa':
            # return HttpResponse('当前路由是：/aaaa')

class VisitLimit(MiddlewareMixin):
    '''此中间件限制一个IP地址对应的访问/user/login 的次数不能改过10次,超过后禁止使用'''
    visit_times = {}  # 此字典用于记录客户端IP地址有访问次数
    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']  # 得到IP地址
        if not re.match('^/test', request.path_info):
            return
        times = self.visit_times.get(ip_address, 0)
        print("IP:", ip_address, '已经访问过', times, '次!:', request.path_info)
        self.visit_times[ip_address] = times + 1
        if times < 5:
            return

        return HttpResponse('你已经访问过' + str(times) + '次，您被禁止了')
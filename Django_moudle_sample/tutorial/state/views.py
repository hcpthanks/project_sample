from django.http import HttpResponse
import datetime

# Create your views here.


def set_cookie(request):
    rsp = HttpResponse('写入cookie')
    rsp.set_cookie('came', '1', max_age=600)
    # rsp.set_cookie('language', value='zh-CN', expires=datetime.datetime(2017, 8, 1, 22, 33),
    #                path='product/', domain='blog.xuepy.com', secure=False, httponly=False)
    rsp.set_cookie('language', 'zh-CN', expires=datetime.datetime(2017, 8,25, 22, 44))

    return rsp


def get_cookie(request):
    lang = request.COOKIES.get('language', 'en-US')
    if 'came' in request.COOKIES:
        return HttpResponse(f'欢迎再次访问网站! 您设置的语言是:{lang}')
    return HttpResponse('欢迎第一次访问我们的网站, 您设置的语言是:{lang}')


def delete_cookie(request):
    if 'language' in request.COOKIES:
        rsp = HttpResponse()
        rsp.delete_cookie('language')
        return rsp


def set_session(request):
    """设置Session"""
    request.session['course'] = 'python web fullstack'
    request.session.set_expiry(300)                #设置过期时间
    return HttpResponse('写入session["course"]')


def get_session(request):
    """获取session"""
    course = None
    if 'course' in request.session:
        course = request.session.get('course', None)
    return HttpResponse(course if course else '未找到')


def clear_session(request):
    request.session.flush()
    return HttpResponse('session清楚完毕')




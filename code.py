from django.http import HTTPRespones

def index(request):
    return HTTPRespones('<h1>首页</h1>')

def index2(request):
    return HTTPRespones('<h1>首页22</h1>')

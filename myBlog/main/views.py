from django.shortcuts import render
from .models import Post

# index.html을 부르는 index함수
def index(request):
    return render(request,'main/index.html')

# blog.html 페이지를 부르는 blog함수
def bolg(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = Post.objects.all()
    #bolg.html페이지를 열때 모든 Post인 postlist도 같이 가져옴
    return render(request, 'main/bolg.html', {'postlist':postlist})
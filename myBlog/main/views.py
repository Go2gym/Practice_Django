from django.shortcuts import render
from .models import Post

# index.html을 부르는 index함수
def index(request):
    return render(request,'main/index.html')

# blog.html 페이지를 부르는 blog함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = Post.objects.all()
    #blog.html페이지를 열때 모든 Post인 postlist도 같이 가져옴
    return render(request, 'main/blog.html', {'postlist':postlist})

def posting(request, pk):
    #게시글 중 primary_key를 이용해 하나의 게시글을 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때 찾아낸 게시글을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post': post})
from django.urls import path

from django.contrib import admin
from main.views import index, blog, posting

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('blog/', blog, name='blog'),
    # blog뒤에 숫자가 온다면 그 값을 pk라고 할것이다. pk값도 같이 전달
    path('blog/<int:pk>', posting, name='posting'),
]
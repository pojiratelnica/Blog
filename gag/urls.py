"""gag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from apps.posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.posts_list, name='posts_list'),
    url(r'^index/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^like/(?P<post_id>[0-9]+)/$', views.likes, name='likes'),
    url(r'^dislike/(?P<post_id>[0-9]+)/$', views.dislikes, name='dislikes'),
    url(r'^by_likes_down/$', views.by_likes_down, name='by_likes_down'),
    url(r'^by_likes_up/$', views.by_likes_up, name='by_likes_up'),
    url(r'^by_dislikes_down/$', views.by_dislikes_down, name='by_dislikes_down'),
    url(r'^by_dislikes_up/$', views.by_dislikes_up, name='by_dislikes_up'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

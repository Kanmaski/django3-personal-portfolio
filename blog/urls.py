from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    re_path(r'^(?P<blog_id>[-@+()?%:,\s\w]+)/$', views.detail, name = 'detail')
]


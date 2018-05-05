from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'', views.PostListView.as_view(), name='posts'),
    # url(r'(?P<pk>[0-9]+)/^$', views.PostDetailView.as_view(), name='post_detail'),
]
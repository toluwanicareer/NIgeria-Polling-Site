from django.conf.urls import url

from . import views

app_name='poll_app'

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.PollDetailView.as_view(), name='detail'),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^api/vote/$', views.VoteView.as_view(), name='vote'),
    url(r'^api/login/$', views.loginView.as_view(), name='login'),
    url(r'^api/updatae_friend_count/$', views.updateFriendCount.as_view(), name='update_friend'),
    ]



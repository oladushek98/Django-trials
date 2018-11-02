from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from userpage.models import Articles

urlpatterns = [
   url(r'^$', 
   ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
   template_name="userpage/userpage.html")),
   url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Articles, template_name="userpage/news.html")),
]
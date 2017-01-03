from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token

from api import views


urlpatterns = [
    url(r'^register/$', views.Register.as_view()),
    url(r'^login/$', obtain_jwt_token),

    url(r'^skills/$', views.SkillList.as_view()),
    url(r'^skills/(?P<pk>[0-9]+)/$', views.SkillDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

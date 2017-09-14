from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^evaluator/', include('evaluator.urls')),
    url(r'^admin/', admin.site.urls),
]

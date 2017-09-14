from django.conf.urls import url
from .views import EvaluateView
urlpatterns = [
	url(r'^evaluate/', EvaluateView.as_view() ),
]

from .views import JobView,UpdateJob
from django.urls import path
from . import views

urlpatterns = [
	#localhost:8000/jobs/
    path('', JobView.as_view()),
    path('<int:j_id>/', UpdateJob.as_view()),
]
from django.urls import path
from app1 import views
from django.conf.urls.static import static
app_name = 'app1'
urlpatterns = [
    path('',view=views.home,name='home'),
    path('<int:pk>/',view=views.candidate_view,name='candidate')
]

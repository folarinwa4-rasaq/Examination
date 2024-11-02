from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('preview/<str:pk>', views.preview, name='preview'),
    path('preview/examination/<str:pk>', views.examination, name='examination'),
    path('preview/examination/result/<str:pk>', views.result, name='result'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
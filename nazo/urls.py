from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('<uuid:nazo_id>/', views.nazo, name='nazo'),
    path('answer/<uuid:answer_id>/', views.answer, name='answer'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
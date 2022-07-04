from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='home'),
    path('tournament/', views.tournament, name='tournament'),
    path('tournament_sorted/', views.tournament_sorted, name='tournament_sorted'),
    path('raiting/', views.raiting, name='raiting'),
    path('fighter/', views.fighter, name='fighter'),
    path('fighter/<int:pk>', views.Stats.as_view(), name='stats'),
    path('fight/', views.stats_fight, name='fight'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
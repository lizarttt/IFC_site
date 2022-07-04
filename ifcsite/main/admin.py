from django.contrib import admin
from .models import *

# регистрация в админку моделей
admin.site.register(TourPost)
admin.site.register(RaitingModel)
admin.site.register(FighterModel)
admin.site.register(StatisticsModel)


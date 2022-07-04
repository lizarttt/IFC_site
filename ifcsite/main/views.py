from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.core.paginator import Paginator


def index(request):
    return render(request, 'main/index.html')


def raiting(request):
    rait = RaitingModel.objects.all()
    return render(request, 'main/raiting.html', {'rait': rait})


def tournament(request): # пагинатор
    contact_list = TourPost.objects.order_by('data')
    paginator = Paginator(contact_list, 3) # количество постов для пагинатора

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/tournament.html', {'page_obj': page_obj})


"""сортировка для турниров внизу"""


def tournament_sorted(request): # пагинатор
    contact_list = TourPost.objects.order_by('-data')
    paginator = Paginator(contact_list, 3) # количество постов для пагинатора

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/tournament_sorted.html', {'page_obj': page_obj})


def fighter(request):  # классический пагинатор через функцию
    contact_list = FighterModel.objects.all()
    paginator = Paginator(contact_list, 4) # количество постов для пагинатора

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/fighter.html', {'page_obj': page_obj})


class Stats(DetailView):    # Наследуем класс ДетаилВью для создания уникального ID
    model = FighterModel
    template_name = 'main/stats.html'
    context_object_name = 'fighter'

    def get_success_url(self, **kwargs):  # Делаем get-request и получаем уникальный айди под каждый пост.
        return reverse_lazy('stats', kwargs={'pk': self.get_object().id})


def stats_fight(request):
    contact_list = StatisticsModel.objects.order_by('type_education')
    paginator = Paginator(contact_list, 25) # количество постов для пагинатора

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/stats_fight.html', {'page_obj': page_obj})


# <<<<<<< СОРТИРОВКА ПО КАТЕГОРИЯМ ВЕСОВЫМ
def stats_fight_sort_light(request):
    contact_list = StatisticsModel.objects.order_by('type_education')
    paginator = Paginator(contact_list, 25) # количество постов для пагинатора

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/stats_fight.html', {'page_obj': page_obj})


def stats_fight_sort_middle(request):
    contact_list = StatisticsModel.objects.order_by('-data')
    paginator = Paginator(contact_list, 25) # количество постов для пагинатора

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/stats_fight.html', {'page_obj': page_obj})


def stats_fight_sort_heavy(request):
    contact_list = StatisticsModel.objects.order_by('-data')
    paginator = Paginator(contact_list, 25) # количество постов для пагинатора

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/stats_fight.html', {'page_obj': page_obj})
# КОНЕЦ СОРТИРОВКА >>>>>>>>


def fighter_post(request):
    form = PostFighterForm # привязываем форму
    data = {
        'form': form
    }
    return render(request, 'main/fighter_post.html', data)


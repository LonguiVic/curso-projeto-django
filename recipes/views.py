from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Luiz Otávio',
        'recipes': [make_recipe() for _ in range(9)],
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Luiz Otávio',
        'recipe': make_recipe(),
    })

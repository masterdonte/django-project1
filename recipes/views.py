from django.contrib import messages
from django.http import Http404  # HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from recipes.models import Recipe
from django.db.models import Q
from utils.pagination import make_pagination
import os

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')  # recipes = Recipe.objects.all().order_by('-id')

    messages.success(request, 'Testando a flash message de sucesso')
    # messages.error(request, 'Testando a flash message de erro.')
    # messages.info(request, 'Testando a flash message de info.')
    # messages.warning(request, 'Testando a flash message de warning')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_obj,  # 'recipes': [make_recipe() for _ in range(10)],
        'pagination_range': pagination_range
    })


def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True,).order_by('-id'))
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'title': f'{recipes[0].category.name} - Category | '
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    # recipe = Recipe.objects.filter(pk=id, is_published=True,).order_by('-id').first() # noqa E501
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,  # 'recipe': make_recipe(),
        'is_detail_page': True,
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(Q(title__icontains=search_term) | Q(description__icontains=search_term)),
        is_published=True,
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })

# def category_old(request, category_id):
#     recipes = Recipe.objects.filter(category__id=category_id, is_published=True,).order_by('-id')
#     # if not recipes:
#     #     raise Http404('Not found 🥲')
#     if not recipes:
#         return HttpResponse(content='<h1>Pagina não encontrada 🥲<h1>',status = 404)
#     return render(request, 'recipes/pages/category.html', context={
#         'recipes': recipes,
#         'title': f'{recipes.first().category.name} - Category | '
#     })

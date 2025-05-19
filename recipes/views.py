from django.shortcuts import render, get_list_or_404, get_object_or_404
# from django.http import Http404, HttpResponse
from recipes.models import Recipe
# from utils.recipes.factory import make_recipe 

def home(request):
    # recipes = Recipe.objects.all().order_by('-id')
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        # 'recipes': [make_recipe() for _ in range(10)],
        'recipes': recipes,
    })

def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True,).order_by('-id'))
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    # recipe = Recipe.objects.filter(pk=id, is_published=True,).order_by('-id').first()
    return render(request, 'recipes/pages/recipe-view.html', context={
        # 'recipe': make_recipe(),
        'recipe': recipe,
        'is_detail_page': True,
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
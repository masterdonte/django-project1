from django.urls import reverse, resolve
from .test_recipe_base import RecipeBaseTest
from recipes import views


class RecipeSearchViewTest(RecipeBaseTest):

    def test_recipe_search_uses_correct_view_function(self):
        url = reverse("recipes:search")
        view = resolve(url)
        self.assertIs(view.func, views.search)

    def test_recipe_search_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=anytest')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse('recipes:search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
        )

    def test_recipe_search_can_find_recipe_by_title(self):
        title1 = 'title one'
        title2 = 'title two'
        recipe1 = self.make_recipe(
            slug='one', title=title1, author_data={'username': 'one'}
        )
        recipe2 = self.make_recipe(
            slug='two', title=title2, author_data={'username': 'two'}
        )

        url = reverse('recipes:search')
        response1 = self.client.get(f'{url}?q={title1}')
        response2 = self.client.get(f'{url}?q={title2}')
        response3 = self.client.get(f'{url}?q=title')

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])

        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response3.context['recipes'])
        self.assertIn(recipe2, response3.context['recipes'])

    def test_recipe_search_without_parameter_page(self):
        for i in range(1, 21):
            self.make_recipe(title=f'title-{i}', slug=f'slug-{i}', author_data={'username': f'user-{i}'})
        url = reverse('recipes:search')
        response = self.client.get(f'{url}?page=any&q=title')
        pagination_range = response.context['pagination_range']
        recipes = response.context['recipes']
        self.assertEqual(pagination_range['current_page'], 1)
        self.assertEqual(recipes.paginator.count, 20)
        # self.assertEqual(recipes.paginator.per_page, 9)

from django.core.exceptions import ValidationError
from .test_recipe_base import RecipeBaseTest


class CategoryModelTest(RecipeBaseTest):
    def setUp(self) -> None:
        self.category = self.make_category(name='Category Testing')
        return super().setUp()

    def test_recipe_category_model_string_representarion_is_name_field(self):
        self.assertEqual(
            str(self.category), self.category.name,
            msg=f'Recipe string representation must be "{self.category.name}" '
        )

    def test_recipe_category_model_name_max_length_is_65_chars(self):
        # self.category.name = 'A' * 66 # As duas formas funcionam
        setattr(self.category, 'name', 'A' * 66)
        with self.assertRaises(ValidationError):
            self.category.full_clean()

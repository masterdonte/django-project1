from unittest import TestCase
from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        result = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )
        self.assertEqual([1, 2, 3, 4], result['pagination'])

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):
        objects = list(range(1, 21))
        # Current page = 1 - Qty Page = 2 - Middle Page = 2
        result = make_pagination_range(objects, 4, 1)
        self.assertEqual([1, 2, 3, 4], result['pagination'])

        # Current page = 2 - Qty Page = 2 - Middle Page = 2
        result = make_pagination_range(objects, 4, 2)
        self.assertEqual([1, 2, 3, 4], result['pagination'])

        # Current page = 3 - Qty Page = 2 - Middle Page = 2 - HERE RANGE SHOULD CHANGE
        result = make_pagination_range(objects, 4, 3)
        self.assertEqual([2, 3, 4, 5], result['pagination'])

        # Current page = 4 - Qty Page = 2 - Middle Page = 2 - HERE RANGE SHOULD CHANGE
        result = make_pagination_range(objects, 4, 4)
        self.assertEqual([3, 4, 5, 6], result['pagination'])

    def test_make_sure_middle_ranges_are_correct(self):
        objects = list(range(1, 21))
        # Current page = 10 - Qty Page = 2 - Middle Page = 2 - HERE RANGE SHOULD CHANGE
        result = make_pagination_range(objects, 4, 10)
        self.assertEqual([9, 10, 11, 12], result['pagination'])

        # Current page = 12 - Qty Page = 2 - Middle Page = 2 - HERE RANGE SHOULD CHANGE
        result = make_pagination_range(objects, 4, 12)
        self.assertEqual([11, 12, 13, 14], result['pagination'])

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        objects = list(range(1, 21))
        # Current page = 18 - Qty Page = 2 - Middle Page = 2 - HERE RANGE SHOULD CHANGE
        result = make_pagination_range(objects, 4, 18)
        self.assertEqual([17, 18, 19, 20], result['pagination'])

        # Current page = 19 - Qty Page = 2 - Middle Page = 2 - HERE RANGE SHOULD CHANGE
        result = make_pagination_range(objects, 4, 19)
        self.assertEqual([17, 18, 19, 20], result['pagination'])

        # Current page = 20 - Qty Page = 2 - Middle Page = 2 - HERE RANGE SHOULD CHANGE
        result = make_pagination_range(objects, 4, 20)
        self.assertEqual([17, 18, 19, 20], result['pagination'])

        # Current page = 21 - Qty Page = 2 - Middle Page = 2 - HERE RANGE SHOULD CHANGE
        result = make_pagination_range(objects, 4, 21)
        self.assertEqual([17, 18, 19, 20], result['pagination'])

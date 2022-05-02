from http import HTTPStatus
from tests import TestCase


class TradingActivityTestCase(TestCase):

    def test_route_exists(self):
        self.assertTrue(self.get('/users'))

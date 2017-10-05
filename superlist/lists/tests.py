from django.template.loader import render_to_string
from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        fond = resolve('/')
        self.assertEqual(fond.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

    def test_home_page_can_save_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A New list item'

        response = home_page(request)
        self.assertIn('A New list item', response.content.decode('utf-8'))

        expected_html = render_to_string(
            'home_page.html', {'new_item_text': 'A New list item'}, request=request

        )
        print(expected_html)
        print(response.content.decode())
        self.assertEqual(response.content.decode(), expected_html)

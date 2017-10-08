from django.template.loader import render_to_string
from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item


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


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The First!'
        first_item.save()

        second_item = Item()
        second_item.text = 'The Second!'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)


class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post('/lists/new/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new/', data={'item_text': 'A new list item'})

        # self.assertEqual(response.status_code, 302)
        # self.assertRegex(response['location'], r'/lists/the_only_list/$')
        self.assertRedirects(response, '/lists/the_only_list/')


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get('/lists/the_only_list/')
        self.assertTemplateUsed(response, 'list.html')

    def test_display_all_lists(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the_only_list/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

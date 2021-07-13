from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

class SnakesTests(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='admin',
            email='admin@gmail.com',
            password='admin123'

        )
        self.snake=Snack.objects.create(
            name='Hummus',
            purchaser=self.user,
            description='afasgishjgoi hgoiseghiogsioogsegoi',

        )
    
    def test_list_page(self):
        url= reverse('snacks_list')
        self.assertTemplateUsed(self.client.get(url), 'snack_list.html')
        self.assertEqual(self.client.get(url).status_code,200)
    
    def test_detail_page(self):
        response= self.client.get(
            reverse('snack_detail',args='1') ,
            {'name':'Hummus', 'purchaser':self.user , 'description':'afasgishjgoi hgoiseghiogsioogsegoi'},
        )
        self.assertEqual(response.status_code, 200)

    def test_detail_page(self):
        response= self.client.get(
            reverse('snack_detail',args='1') ,
            {'name':'Hummus', 'purchaser':self.user , 'description':'afasgishjgoi hgoiseghiogsioogsegoi'},
        )
        self.assertEqual(response.status_code, 200)

    def test_create_page(self):
        response= self.client.get(
            reverse('snack_create') ,
            {'name':'Hummus', 'purchaser':self.user , 'description':'afasgishjgoi hgoiseghiogsioogsegoi'},
        )
        self.assertEqual(response.status_code, 200)
    
    def test_update_page(self):
        response= self.client.get(
            reverse('snack_update',args='1') ,
            {'name':'Hummus', 'purchaser':self.user , 'description':'afasgishjgoi hgoiseghiogsioogsegoi'},
        )
        self.assertEqual(response.status_code, 200)

    def test_update_page(self):
        response= self.client.get(
            reverse('snack_delete',args='1') ,
            {'name':'Hummus', 'purchaser':self.user , 'description':'afasgishjgoi hgoiseghiogsioogsegoi'},
        )
        self.assertEqual(response.status_code, 200)

from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from .models import New


# Create your tests here.
class NewTestCase(TestCase):
    def setUp(self):
        New.objects.create(title="It works", subtitle = "let's have fun", body="This proof is made to ensure that the app works properly")
        New.objects.create(title="Let's gonna make a proof")

    def test_list_news_function(self):
        url = reverse("new_list")
        list_new_get = self.client.get(url)
        self.assertEqual(list_new_get.status_code, 200)
        self.assertContains(list_new_get, 'It works')

    def test_detail_news_function(self):
        noticia= New.objects.get(title="It works")
        url = reverse("new_detail", args=(noticia.pk,))
        detail_new_get = self.client.get(url)
        self.assertEqual(detail_new_get.status_code, 200)
        self.assertContains(detail_new_get, 'It works')

    def test_create_news_function(self):
        num_news_bef = New.objects.count()
        upload_file = open(settings.MEDIA_ROOT + '/coche.jpg', 'rb')
        url = reverse("new_add")

        create_new_get = self.client.get(url)
        self.assertEqual(create_new_get.status_code, 200)
        num_news_aft = New.objects.count()
        self.assertEqual(num_news_aft, num_news_bef)

        data = {
            "title": "New test",
            "subtitle": "semana santa",
            "body": "lorem ipsum",
            "image": upload_file
        }

        create_new_post = self.client.post(url, data)
        self.assertEqual(create_new_post.status_code, 302)
        num_news_aft = New.objects.count()
        self.assertEqual(num_news_aft, num_news_bef + 1)

    def test_edit_news_function(self):
        upload_file = open(settings.MEDIA_ROOT + '/coche.jpg', 'rb')
        noticia= New.objects.get(title="It works")
        url = reverse("new_edit", args=(noticia.pk,))


        edit_new_get = self.client.get(url)
        self.assertEqual(edit_new_get.status_code, 200)

        data = {
            "title": "New modified test",
            "subtitle": "semana santa",
            "body": "lorem ipsum",
            "image": upload_file
        }

        edit_new_post = self.client.post(url, data)
        self.assertEqual(edit_new_post.status_code, 302)
        self.assertNotEqual(noticia.title,data['title'])

    def test_delete_news_function(self):
        noticia = New.objects.get(title="It works")
        num_news_bef = New.objects.count()
        url = reverse("new_delete", args=(noticia.pk,))

        delete_new_get = self.client.get(url)
        self.assertEqual(delete_new_get.status_code, 200)

        delete_new_post = self.client.post(url,{})
        self.assertEqual(delete_new_post.status_code, 302)
        num_news_aft = New.objects.count()
        self.assertEqual(num_news_aft, num_news_bef - 1)

    def test_list_news_class(self):
        url = reverse("new_list_class")
        list_new_get = self.client.get(url)
        self.assertEqual(list_new_get.status_code, 200)
        self.assertContains(list_new_get, 'It works')

    def test_detail_news_class(self):
        noticia= New.objects.get(title="It works")
        url = reverse("new_detail_class", args=(noticia.pk,))
        detail_new_get = self.client.get(url)
        self.assertEqual(detail_new_get.status_code, 200)
        self.assertContains(detail_new_get, 'It works')

    def test_create_news_class(self):
        num_news_bef = New.objects.count()
        upload_file = open(settings.MEDIA_ROOT + '/coche.jpg', 'rb')
        url = reverse("new_add_class")

        create_new_get = self.client.get(url)
        self.assertEqual(create_new_get.status_code, 200)
        num_news_aft = New.objects.count()
        self.assertEqual(num_news_aft, num_news_bef)

        data = {
            "title": "New test",
            "subtitle": "semana santa",
            "body": "lorem ipsum",
            "image": upload_file
        }

        create_new_post = self.client.post(url, data)
        self.assertEqual(create_new_post.status_code, 302)
        num_news_aft = New.objects.count()
        self.assertEqual(num_news_aft, num_news_bef + 1)

    def test_edit_news_class(self):
        upload_file = open(settings.MEDIA_ROOT + '/coche.jpg', 'rb')
        noticia= New.objects.get(title="It works")
        url = reverse("new_edit_class", args=(noticia.pk,))


        edit_new_get = self.client.get(url)
        self.assertEqual(edit_new_get.status_code, 200)

        data = {
            "title": "New modified test",
            "subtitle": "semana santa",
            "body": "lorem ipsum",
            "image": upload_file
        }

        edit_new_post = self.client.post(url, data)
        self.assertEqual(edit_new_post.status_code, 302)
        self.assertNotEqual(noticia.title,data['title'])

    def test_delete_news_class(self):
        noticia = New.objects.get(title="It works")
        num_news_bef = New.objects.count()
        url = reverse("new_delete_class", args=(noticia.pk,))

        delete_new_get = self.client.get(url)
        self.assertEqual(delete_new_get.status_code, 200)

        delete_new_post = self.client.post(url,{})
        self.assertEqual(delete_new_post.status_code, 302)
        num_news_aft = New.objects.count()
        self.assertEqual(num_news_aft, num_news_bef - 1)

    #Casos de error
    def test_new_title_left_class(self):
        num_news_bef = New.objects.count()
        upload_file = open(settings.MEDIA_ROOT + '/coche.jpg', 'rb')
        url = reverse("new_add_class")

        create_new_get = self.client.get(url)
        self.assertEqual(create_new_get.status_code, 200)
        num_news_aft = New.objects.count()
        self.assertEqual(num_news_aft, num_news_bef)

        data = {
            "subtitle": "semana santa",
            "body": "lorem ipsum",
            "image": upload_file
        }

        create_new_post = self.client.post(url, data)
        self.assertContains(create_new_post,'Este campo es obligatorio', status_code=200)
        num_news_aft = New.objects.count()
        self.assertEqual(num_news_aft, num_news_bef)

    def test_new_title_left_function(self):
        num_news_bef = New.objects.count()
        upload_file = open(settings.MEDIA_ROOT + '/coche.jpg', 'rb')
        url = reverse("new_add")

        create_new_get = self.client.get(url)
        self.assertEqual(create_new_get.status_code, 200)
        num_news_aft = New.objects.count()
        self.assertEqual(num_news_aft, num_news_bef)

        data = {
            "subtitle": "semana santa",
            "body": "lorem ipsum",
            "image": upload_file
        }

        create_new_post = self.client.post(url, data)
        self.assertContains(create_new_post,'Este campo es obligatorio', status_code=200)
        num_news_aft = New.objects.count()
        self.assertEqual(num_news_aft, num_news_bef)
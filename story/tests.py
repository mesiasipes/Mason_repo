# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from story.models import Post

from story.forms import AuthenticationForm

from django.contrib.auth.models import User


class TestStoryViews(TestCase):
    def setUp(self):
        post = Post(author='guy', title='my post', text='posty shit')
        post.save()

    def test_story_view(self):
        response = self.client.get('/story/')
        self.assertEqual(len(response.context[0]['posts']), Post.objects.count())

    def test_specific_view(self):
        post = Post.objects.first()
        response = self.client.get('/story/{}'.format(post.id))
        self.assertEqual(response.context[0]['post'], post)

    def test_login_view_empty(self):
        #response = self.client.get('/login/')
        #self.assertEqual(response.context[0]['form'], AuthenticationForm())

        #test that form handles empty data
        data = {}
        response = self.client.post('/login/', data)
        self.assertEqual(response.status_code, 200)

    def test_login_view_invalid(self):
        data = {
            'username': '',
            'password': '',
        }
        response = self.client.post('/login/', data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context[0]['user'].is_authenticated)

    def test_login_view_valid(self):
        user = User(username='mesia', email='your@momma.com')
        user.set_password('password')
        user.save()
        data = {
            'username': 'mesia',
            'password': 'password',
        }
        response = self.client.post('/login/', data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context[0]['user'].is_authenticated)
        self.assertEqual(response.context[0]['user'], user)

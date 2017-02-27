from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from kilonull.models import Post, Category, Tag, Menu, MenuItem
from kilonull import views

'''
IMPORTANT:
This tests both the views and their corresponding templates. Some tests try to
find content to verify that the template/view is correct. Changing content in
templates may require updates to tests.
'''


class TestIndex():
    # Should not display any posts.
    def test_empty_index(self):
        no_post_text = 'No posts found.'
        client = Client()
        response = client.get(reverse('kilonull:index'))
        assert response.status_code == 200
        assert str(response.content).find(no_post_text) != -1

    # Should not display any posts.
    def test_page_not_int(self):
        no_post_text = 'No posts found.'
        client = Client()
        response = client.get(reverse('kilonull:index'), {'page': 'df'})
        assert response.status_code == 200
        assert str(response.content).find(no_post_text) != -1

    # Should not display any posts.
    def test_page_bad_int(self):
        no_post_text = 'No posts found.'
        client = Client()
        response = client.get(reverse('kilonull:index'), {'page': -500})
        assert response.status_code == 200
        assert str(response.content).find(no_post_text) != -1

    def test_pagination(self):
        # Need a user for the author field
        user_args = {
            'username': 'test',
            'password': 'testpassword123',
        }
        user = User.objects.create(**user_args)
        user.save()

        # Generate posts.
        for i in range(20):
            Post.objects.create(**{
                'slug': 'test_slug' + str(i),
                'author': user,
            })
        client = Client()

        response = client.get(reverse('kilonull:index'), {'page': 2})
        assert response.status_code == 200
        assert str(response.content).find('next') != -1
        assert str(response.content).find('previous') != -1

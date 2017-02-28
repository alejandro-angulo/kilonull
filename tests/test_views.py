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


class TestBase(TestCase):
    def test_menu(self):
        main_menu = Menu.objects.create(**{
            'slug': 'primary',
        })
        menu_item_args = {
            'menu': main_menu,
            'order': 0,
            'link_url': 'https://google.com',
            'link_text': 'Menu Item',
        }
        menu_item = MenuItem.objects.create(**menu_item_args)

        client = Client()
        response = client.get(reverse('kilonull:index'))
        # expected_html = "<li><a href='{}'>{}</a></li>"
        expected_html = "<li><a href=\\'{}\\'>{}</a></li>".format(
            menu_item_args['link_url'], menu_item_args['link_text'])

        menu_item.delete()
        main_menu.delete()


class TestIndex(TestCase):
    # Should not display any posts.
    def test_empty_index(self):
        no_post_text = 'No posts found.'
        client = Client()
        response = client.get(reverse('kilonull:index'))
        assert response.status_code == 200
        assert no_post_text in str(response.content)

    # Should not display any posts.
    def test_page_not_int(self):
        no_post_text = 'No posts found.'
        client = Client()
        response = client.get(reverse('kilonull:index'), {'page': 'df'})
        assert response.status_code == 200
        assert no_post_text in str(response.content)

    # Should not display any posts.
    def test_page_bad_int(self):
        no_post_text = 'No posts found.'
        client = Client()
        response = client.get(reverse('kilonull:index'), {'page': -500})
        assert response.status_code == 200
        assert no_post_text in str(response.content)

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
        assert 'next' in str(response.content)
        assert 'previous' in str(response.content)


class TestPostView(TestCase):
    def setUp(self):
        # Need a user for the author field
        user_args = {
            'username': 'test',
            'password': 'testpassword123',
        }
        user = User.objects.create(**user_args)
        user.save()

        post_args = {
            'slug': 'test_slug',
            'author': user,
        }
        post = Post.objects.create(**post_args)
        post.save()

    def tearDown(self):
        Post.objects.get(slug='test_slug').delete()
        User.objects.get(username='test').delete()

    def test_render(self):
        client = Client()
        post = Post.objects.get(slug='test_slug')

        response = client.get(post.get_absolute_url())
        assert response.status_code == 200

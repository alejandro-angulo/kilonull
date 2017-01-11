from django.contrib.auth.models import User
from django.test import TestCase
from kilonull.models import Post, Category, Tag, Menu, MenuItem


class TestPostModel(TestCase):
    def setUp(self):
        # Need a user for the author field
        user_args = {
            'username': 'test',
            'password': 'testpassword123',
        }
        user = User.objects.create(**user_args)
        user.save()

    def tearDown(self):
        User.objects.get(username='test').delete()

    def test_representation(self):
        user = User.objects.get(username='test')
        post_args = {
            'slug': 'test_slug',
            'author': user,
        }
        post = Post.objects.create(**post_args)

        assert '{}'.format(post) == 'test_slug'

    def test_markdown_highlighting(self):
        user = User.objects.get(username='test')
        post_args = {
            'slug': 'test_slug',
            'author': user,
            'body': '```javascript\nalert(s);```',
        }
        post = Post.objects.create(**post_args)
        post.save()
        expected_html = '<div class="highlight"><pre><span></span>' \
            '<span class="nx">alert</span><span class="p">(' \
            '</span><span class="nx">s</span><span class="p">);' \
            '</span>\n</pre></div>\n'

        assert post.body_html == expected_html


class TestCategoryModel(TestCase):
    def test_string_representation(self):
        category = Category.objects.create(slug="test_slug")

        assert '{}'.format(category) == 'test_slug'


class TestTagModel(TestCase):
    def test_string_representation(self):
        tag = Tag.objects.create(slug="test_slug")

        assert '{}'.format(tag) == 'test_slug'


class TestMenuModel(TestCase):
    def test_string_representation(self):
        menu = Menu.objects.create(slug="test_slug")

        assert '{}'.format(menu) == 'test_slug'


class TestMenuItemModel(TestCase):
    def setUp(self):
        menu = Menu.objects.create(slug="test_slug")
        menu.save()

    def tearDown(self):
        Menu.objects.get(slug="test_slug").delete()

    def test_string_representation(self):
        menu = Menu.objects.get(slug="test_slug")
        menu_item = MenuItem.objects.create(
            link_text="test text",
            menu=menu,
            order=0,
        )

        assert '{}'.format(menu_item) == 'test text in test_slug'

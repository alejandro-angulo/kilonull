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

    def test_absolute_url(self):
        user = User.objects.get(username='test')
        post_args = {
            'slug': 'test_slug',
            'author': user,
        }
        post = Post.objects.create(**post_args)

        url = post.get_absolute_url()
        assert '{}'.format(url) == '/post/{}/'.format(post_args['slug'])

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
    def setUp(self):
        Category.objects.create(slug='test_slug')

    def tearDown(self):
        Category.objects.get(slug='test_slug').delete()

    def test_string_representation(self):
        slug = 'test_slug'
        category = Category.objects.get(slug=slug)

        assert '{}'.format(category) == slug

    def test_absolute_url(self):
        slug = 'test_slug'
        category = Category.objects.get(slug=slug)

        assert '{}'.format(category.get_absolute_url()) == \
            '/category/{}/'.format(slug)


class TestTagModel(TestCase):
    def setUp(self):
        Tag.objects.create(slug='test_slug')

    def tearDown(self):
        Tag.objects.get(slug='test_slug').delete()

    def test_string_representation(self):
        slug = 'test_slug'
        tag = Tag.objects.get(slug=slug)

        assert '{}'.format(tag) == slug

    def test_absolute_url(self):
        slug = 'test_slug'
        tag = Tag.objects.get(slug=slug)

        tag.get_absolute_url()
        assert '{}'.format(tag.get_absolute_url()) == '/tag/{}/'.format(slug)


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

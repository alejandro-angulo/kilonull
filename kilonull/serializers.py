from django.urls import reverse
from rest_framework import serializers
from kilonull.models import Category, Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="kilonull:view_blog_post",
        lookup_field="slug",
    )
    path = serializers.SerializerMethodField('find_path')
    read_only = True

    class Meta:
        model = Post
        fields = ('url', 'title', 'slug', 'published', 'body',
                  'hide_listing', 'path',)

    def find_path(self, obj):
        return reverse('kilonull:view_blog_post', kwargs={'slug': obj.slug})


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(queryset=Post.objects.all(),
                                                view_name='post-detail',
                                                many=True)

    class Meta:
        model = Category
        fields = ('url', 'title', 'posts',)

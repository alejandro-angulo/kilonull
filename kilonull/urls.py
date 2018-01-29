from django.urls import include, re_path
from rest_framework.routers import DefaultRouter
from kilonull.views import (
    index,
    view_category,
    view_post,
    view_tag,
    PostViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register(r'posts', PostViewSet)
# router.register(r'categories', CategoryViewSet)

app_name = 'kilonull'
urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^post/(?P<slug>[^\.]+)/$', view_post, name='view_blog_post'),
    re_path(r'^category/(?P<slug>[^\.]+)/$', view_category,
        name='view_blog_category'),
    re_path(r'^tag/(?P<slug>[^\.]+)/$', view_tag, name='view_blog_tag'),
    re_path(r'^api/', include(router.urls)),
]

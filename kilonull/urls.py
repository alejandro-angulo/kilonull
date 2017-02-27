from django.conf.urls import include, url
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

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^post/(?P<slug>[^\.]+)/$', view_post, name='view_blog_post'),
    url(r'^category/(?P<slug>[^\.]+)/$', view_category,
        name='view_blog_category'),
    url(r'^tag/(?P<slug>[^\.]+)/$', view_tag, name='view_blog_tag'),
    url(r'^api/', include(router.urls)),
]

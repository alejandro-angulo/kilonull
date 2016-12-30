from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from kilonull.views import index, view_post, PostViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
# router.register(r'categories', CategoryViewSet)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^post/(?P<slug>[^\.]+)/$', view_post, name='view_blog_post'),
    url(r'^api/', include(router.urls)),
]

from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('kilonull.urls', namespace='kilonull'))
]

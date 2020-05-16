from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)#no base_name required since we use queryset in UserProfileViewSet

urlpatterns=[
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls))
]
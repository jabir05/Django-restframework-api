from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from user_profile.views import ProfileViewSet
router=DefaultRouter()
router.register(r'users',UserViewSet,basename='users')
router.register(r'profiles',ProfileViewSet)
urlpatterns=router.urls
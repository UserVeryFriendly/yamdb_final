from rest_framework import routers
from django.urls import include, path

from users.views import UserViewSet, RegistrationViewSet, TokenViewSet
from .views import (CategoryViewSet, TitleViewSet, GenreViewSet,
                    ReviewViewSet, CommentViewSet)

app_name = 'api'

v1 = routers.DefaultRouter()

v1.register('titles', TitleViewSet, basename='titles')
v1.register('categories', CategoryViewSet, basename='categories')
v1.register('genres', GenreViewSet, basename='genres')
v1.register(r'titles/(?P<title_id>\d+)/reviews',
            ReviewViewSet, basename='reviews')
v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
v1.register('users', UserViewSet, basename='users')
v1.register('auth/signup', RegistrationViewSet, basename='sign-up')
v1.register('auth/token', TokenViewSet, basename='token')

urlpatterns = [
    path('v1/', include(v1.urls))
]

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet, GenreViewSet, TitleViewSet, CommentViewSet, ReviewViewSet
)
from users.views import UserViewSet, CreateTokenView, GetTokenView

auth_patern = [
    path('signup/', CreateTokenView.as_view()),
    path('token/', GetTokenView.as_view()),
]

router_v1 = DefaultRouter()
router_v1.register(r'users', UserViewSet, basename='users')
router_v1.register(r'categories', CategoryViewSet)
router_v1.register(r'genres', GenreViewSet)
router_v1.register(r'titles', TitleViewSet)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/auth/', include(auth_patern)),
    path('v1/', include(router_v1.urls)),
]

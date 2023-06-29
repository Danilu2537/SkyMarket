from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, UserAdsListView, CommentViewSet

ads_router = SimpleRouter()
ads_router.register('', AdViewSet)
comments_router = SimpleRouter()
comments_router.register('', CommentViewSet)

urlpatterns = [
    path('ads/me/', UserAdsListView.as_view(), name='user_ads'),
    path('ads/', include(ads_router.urls)),
    path('ads/<int:ad_pk>/comments/', include(comments_router.urls), name='comments'),
]
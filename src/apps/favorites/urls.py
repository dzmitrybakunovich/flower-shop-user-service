from django.urls import path

from .views import FavoriteCreateView, FavoriteUserListView

urlpatterns = [
    path('<int:item_id>/user-list/', FavoriteUserListView.as_view(), name='favorite'),
    path('<int:item_id>/', FavoriteCreateView.as_view(), name='favoritez'),
]

from django.urls import path

from .views import FavoriteCreateView, FavoriteNotifyView

urlpatterns = [
    path('<int:item_id>/notify/', FavoriteNotifyView.as_view(), name='favorite'),
    path('<int:item_id>/', FavoriteCreateView.as_view(), name='favoritez'),
]

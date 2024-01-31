from django.urls import path
from django.urls import reverse_lazy  # Import reverse_lazy

from . import views

app_name = 'ads'
urlpatterns = [
    path('', views.AdListView.as_view(), name='all'),  # Added name='all' for the default view
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create',
         views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_create'),  # Fixed success_url
    path('ad/<int:pk>/update',
         views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_update'),  # Fixed success_url
    path('ad/<int:pk>/delete',
         views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_delete'),  # Fixed success_url
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),
    path('ad/<int:pk>/comment',
         views.CommentCreateView.as_view(), name='ad_comment_create'),
    path('comment/<int:pk>/delete',
         views.CommentDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_comment_delete'),  # Fixed success_url
    path('ad/<int:pk>/favorite',
         views.AddFavoriteView.as_view(), name='ad_favorite'),
    path('ad/<int:pk>/unfavorite',
         views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
]

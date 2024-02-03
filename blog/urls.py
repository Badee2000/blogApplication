from django.urls import path
from .views import post_detail, post_share, post_comment, post_list, post_search
from .feeds import LatestPostFeed

# when you have multiple apps with similar URL patterns to ensure proper URL resolution and avoid conflicts.
app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('tag/<slug:tag_slug>/',
         post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>',
         post_detail, name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('<int:post_id>/comment/',
         post_comment, name='post_comment'),
    path('feed/', LatestPostFeed(), name='post_feed'),
    path('search/', post_search, name='post_search'),]

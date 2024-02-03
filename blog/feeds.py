from django.db.models.base import Model
import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatechars_html
from django.urls import reverse_lazy
from .models import Post


class LatestPostFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog'

    # The items() method retrieves the objects to be included in the feed. We retrieve the last five published posts to include them in the feed.
    def items(self):
        return Post.published.all()[:5]

    # The item_title(), item_description(), and item_pubdate() methods will receive each object returned by items() and return the title, description and publication date for each item.
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatechars_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        return item.publish

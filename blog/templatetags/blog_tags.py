from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

# Custom template tags can be generated to be used in the templates after loading them.

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()

# the function returns a dictionary of variables instead of a simple value.
# Inclusion tags have to return a dictionary of values (context).


@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

# Returns a queryset:
# We will store the result in a variable that can be reused, rather than outputting it directly


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments'))\
        .order_by('-total_comments')[:count]


# Django will not trust any HTML code and will escape it before placing it
# in the output. The only exceptions are variables that are marked as safe from escaping.

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

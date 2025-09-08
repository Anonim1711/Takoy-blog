from django.urls import path
from .views import add_blog, homepage, add_comment, filter_by_author

urlpatterns = [
    path('add_blog/', add_blog, name='add_blog'),
    path('', homepage, name='homepage'),
    path('comment/', add_comment, name='comment_view'),
    path('blogs/<int:author>/', filter_by_author, name='filter')
]
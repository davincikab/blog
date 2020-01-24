from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',PostListView.as_view(), name="list-view"),
    path('archives/', archives, name="archives"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/create/', PostCreateView.as_view(), name="post-create"),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name="post-update"),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name="post-delete"),
    path('post/reply/', render_reply_form, name="reply-form"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

from django.urls import path
from .views import (
    IndexView, PostListView, ComentarioListView, AvaliacaoListView,
    CriarPostView, CriarComentarioView, CriarAvaliacaoView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('comentarios/', ComentarioListView.as_view(), name='comentarios'),
    path('avaliacoes/', AvaliacaoListView.as_view(), name='avaliacoes'),
    path('posts/novo/', CriarPostView.as_view(), name='criar_post'),
    path('comentarios/novo/', CriarComentarioView.as_view(), name='criar_comentario'),
    path('avaliacoes/novo/', CriarAvaliacaoView.as_view(), name='criar_avaliacao'),
]

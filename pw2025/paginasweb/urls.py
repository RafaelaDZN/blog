from django.urls import path
from .views import (
    IndexView, PostListView, ComentarioListView, AvaliacaoListView,
    CriarPostView, CriarComentarioView, CriarAvaliacaoView,
    AtualizarAvaliacaoView,AtualizarPostView,DeletarComentarioView,AtualizarComentarioView,
    DeletarAvaliacaoView,DeletarPostView,LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('comentarios/', ComentarioListView.as_view(), name='comentarios'),
    path('avaliacoes/', AvaliacaoListView.as_view(), name='avaliacoes'),
    path('posts/novo/', CriarPostView.as_view(), name='criar_post'),
    path('comentarios/novo/', CriarComentarioView.as_view(), name='criar_comentario'),
    path('avaliacoes/novo/', CriarAvaliacaoView.as_view(), name='criar_avaliacao'),
    path('avaliacoes/atualizar/<int:pk>/', AtualizarAvaliacaoView.as_view(), name='atualizar_avaliacao'),
    path('comentarios/atualizar/<int:pk>/', AtualizarComentarioView.as_view(), name='atualizar_comentario'),
    path('posts/atualizar/<int:pk>/', AtualizarPostView.as_view(), name='atualizar_post'),
    path('avaliacoes/deletar/<int:pk>/', DeletarAvaliacaoView.as_view(), name='deletar_avaliacao'),
    path('comentarios/deletar/<int:pk>/', DeletarComentarioView.as_view(), name='deletar_comentario'),
    path('posts/deletar/<int:pk>/', DeletarPostView.as_view(), name='deletar_post'),
    path('login/', LoginView.as_view(template_name='paginasweb/login.html'), name='login'),
    # Custom logout view with next_page set to 'index'
    # Note: Ensure that 'index' is a valid URL name in your urlpatterns
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='paginasweb/password_change.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='paginasweb/password_change_done.html'), name='password_change_done'),



]

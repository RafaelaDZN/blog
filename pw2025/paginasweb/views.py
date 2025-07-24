from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comentario, Avaliacao
from .forms import PostForm, ComentarioForm, AvaliacaoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

# Página inicial
class IndexView(TemplateView):
    template_name = 'paginasweb/index.html'

# Listagens
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'paginasweb/posts.html'
    context_object_name = 'posts'

class ComentarioListView(LoginRequiredMixin, ListView):
    model = Comentario
    template_name = 'paginasweb/comentarios.html'
    context_object_name = 'comentarios'

class AvaliacaoListView(LoginRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'paginasweb/avaliacoes.html'
    context_object_name = 'avaliacoes'

################################ Criação (formulários)

class CriarPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'paginasweb/criar_post.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class CriarComentarioView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'paginasweb/criar_comentario.html'
    success_url = reverse_lazy('comentarios')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class CriarAvaliacaoView(LoginRequiredMixin, CreateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'paginasweb/criar_avaliacao.html'
    success_url = reverse_lazy('avaliacoes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


################################ Criação (formulários)


class AtualizarPostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'paginasweb/criar_post.html'
    success_url = reverse_lazy('posts')


class AtualizarComentarioView(LoginRequiredMixin, UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'paginasweb/criar_comentario.html'
    success_url = reverse_lazy('comentarios')


class AtualizarAvaliacaoView(LoginRequiredMixin, UpdateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'paginasweb/criar_avaliacao.html'
    success_url = reverse_lazy('avaliacoes')

################################ Criação (formulários)

class DeletarPostView(LoginRequiredMixin, DeleteView):
    model = Post
    form_class = PostForm
    template_name = 'paginasweb/criar_post.html'
    success_url = reverse_lazy('posts')


class DeletarComentarioView(LoginRequiredMixin,DeleteView ):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'paginasweb/criar_comentario.html'
    success_url = reverse_lazy('comentarios')


class DeletarAvaliacaoView(LoginRequiredMixin, DeleteView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'paginasweb/criar_avaliacao.html'
    success_url = reverse_lazy('avaliacoes')


class CustomLogoutView(LogoutView):
    next_page = 'index'

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'paginasweb/password_change.html'
    success_url = '/password_change/done/'

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'paginasweb/password_change_done.html'
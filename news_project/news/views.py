from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Article

class ArticleListView(ListView):
    """Список новостей с фильтрацией"""
    model = Article
    template_name = 'news/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        """
        Получение queryset с фильтрацией:
        - только опубликованные новости
        - фильтр по заголовку (если указан)
        """
        queryset = Article.objects.filter(is_published=True)
        
        # Поиск по заголовку
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(content__icontains=search_query)
            )
        
        return queryset

    def get_context_data(self, **kwargs):
        """Добавление поискового запроса в контекст"""
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context


class ArticleDetailView(DetailView):
    """Детальная страница новости"""
    model = Article
    template_name = 'news/article_detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        """Показываем только опубликованные новости"""
        return Article.objects.filter(is_published=True)


from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Настройка админ-панели для новостей"""
    list_display = ('title', 'author', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    raw_id_fields = ('author',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'content', 'author')
        }),
        ('Статус', {
            'fields': ('is_published',)
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')

from django.contrib import admin
from .models import Category,CryptoArticalModel,CreateNews

# admin.site.register(NewsPost)
admin.site.site_header = "Crypto News Admin Panel"
admin.site.site_title = "Crypto News Admin"
admin.site.index_title = "Welcome to the Crypto News Admin Panel"


@admin.register(CreateNews)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'author')

admin.site.register(Category)
admin.site.register(CryptoArticalModel)




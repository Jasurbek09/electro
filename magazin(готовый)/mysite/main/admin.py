from django.contrib import admin
from main.models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass
class SizeAdmin(admin.ModelAdmin):
    pass
class ColorAdmin(admin.ModelAdmin):
    pass
class ProductAdmin(admin.ModelAdmin):
    pass
class ProductImageAdmin(admin.ModelAdmin):
    pass
class CommentItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(CommentItem, CommentItemAdmin)






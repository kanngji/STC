from django.contrib import admin

# Register your models here.
from .models import Person

# 모델 검색하기
class PersonAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Person,PersonAdmin)
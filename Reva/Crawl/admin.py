from django.contrib import admin
from .models import First
from .Crawler import crawl_data
# Register your models here.
# @ = Decorators
@admin.register(First)
class Second(admin.ModelAdmin):
    list_display = ('name','page_no','data_count',) # in terms of model
    actions = ('run_crawl',)
    # def get_readonly_fields(self, request,  model_object):
    #     readonly_fields = self.readonly_fields
    #     if model_object:  # editing an existing object
    #         readonly_fields += ('data_count',)
    #     return readonly_fields
    def run_crawl(self,request,queryset):
        for i in queryset.iterator():

            print(i.url)
            count = crawl_data(i.url,i.page_no,i.name)
            i.data_count = count
            i.save()
    run_crawl.short_description = 'Run Crawl'         
        
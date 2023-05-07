from django.db import models

# Create your models here.
class First(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=2000)
    page_no = models.IntegerField()
    data_count = models.IntegerField(blank=True,null= True)

    class Meta:
        verbose_name_plural = 'Crawl Data'
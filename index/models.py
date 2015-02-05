from django.db import models

# Create your models here.

class Pages(models.Model):
    page_name = models.CharField(max_length=200)
    page_adress = models.CharField(max_length=200)
    page_ico = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
        
    def __str__(self):
        return self.page_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
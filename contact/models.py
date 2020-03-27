from django.db import models


class Contact(models.Model):
    SERVICE_CHOICES = {
        ('홈페이지', '홈페이지'),
        ('웹앱', '웹앱'),
        ('쇼핑몰', '쇼핑몰'),
        ('챗봇', '챗봇'),
        ('IT솔루션', 'IT솔루션'),
        ('크롤링', '크롤링'),
    }


    name = models.CharField(max_length=10)
    email = models.EmailField()
    phone_no = models.CharField(max_length=13)
    service = models.CharField(max_length=10, choices=SERVICE_CHOICES)
    url = models.URLField(blank=True)
    content = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed('contact:contact_list')

    class META:
        ordering = ['-created_at']

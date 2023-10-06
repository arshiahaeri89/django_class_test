from django.db import models


class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title')
    email = models.EmailField(max_length=300, verbose_name='Email')
    fullname = models.CharField(max_length=300, verbose_name='Fullname')
    message = models.TextField(verbose_name='Message')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    response = models.TextField(verbose_name='Response')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='Read')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Contact Form'
        verbose_name_plural = 'Contact Forms'

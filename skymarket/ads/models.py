from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Ad(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, default='')
    description = models.TextField(max_length=1000, null=False, blank=False, default='')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False, default=0.00
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ads',
        null=True,
        blank=True,
    )
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Ad')
        verbose_name_plural = _('Ads')
        ordering = ['-created_at']


class Comment(models.Model):
    text = models.TextField(max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments'
    )
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ['-created_at']

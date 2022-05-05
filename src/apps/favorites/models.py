from django.db import models

from django.utils.translation import gettext_lazy as _


class Favorite(models.Model):
    """Store information about user favorites item."""
    user = models.ForeignKey(
        'users.User',
        related_name='favorites',
        on_delete=models.CASCADE,
    )
    item_id = models.IntegerField(null=False)

    class Meta:
        verbose_name = _('Favorite')
        verbose_name_plural = _('Favorites')
        unique_together = ('user', 'item_id')

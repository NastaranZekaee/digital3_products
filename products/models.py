from django.db import models
#from django.db.models import DateTimeField
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('describtion'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('creat time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('update time'), auto_now=True)

    class Meta:
        db_table = 'categorys'
        verbose_name = _('category')
        verbose_name_plural = _('categorys')



    def __str__(self):
        return self.title


class Product(models.Model):
    #parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('describtion'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='product/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(_('creat time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('update time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')



class File(models.Model):
    #parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', verbose_name=_('product'), on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file = models.FileField(_('file'), upload_to='file/%Y/%m/%d/' )
    #avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories')
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('creat time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('update time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')

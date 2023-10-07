from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=30)
    slug = models.SlugField(verbose_name='Слаг категории', max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=30)
    description = models.TextField(verbose_name='Описание товара')
    quantity = models.PositiveIntegerField(verbose_name='Количество товара')
    price = models.DecimalField(verbose_name='Цена товара', max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name='Изображение товара', upload_to='product/%Y/%m/%d', blank=True)
    create = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    upload = models.DateTimeField(verbose_name='Дата и время обновления', auto_now=True)
    slug = models.SlugField(verbose_name='Слаг товара', max_length=40, unique=True)
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 related_name='products',
                                 on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name, self.quantity

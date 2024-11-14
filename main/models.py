from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    В модели Category определены следующие поля:

name: поле для хранения названия категории, ограниченное максимальной длиной
в 100 символов.

description: поле для хранения описания категории, которое может быть пустым.
    """
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    """
    В модели Product определены следующие поля:
name: поле для хранения названия продукта, ограниченное максимальной длиной
в 200 символов.

description: поле для хранения описания продукта, которое может быть пустым.

preview_image: поле для хранения изображения продукта, используя ImageField
с указанием директории для сохранения изображений (upload_to='products/').

category: поле для связи продукта с категорией, используя внешний ключ
(ForeignKey) с моделью Category. При удалении категории, все связанные с ней
продукты также будут удалены (on_delete=models.CASCADE).

purchase_price: поле для хранения цены продукта, ограниченное максимальным
количеством цифр в 10 и двумя десятичными знаками.

created_at: поле для хранения даты создания продукта, которое автоматически
устанавливается при создании записи в базе данных (auto_now_add=True).

updated_at: поле для хранения даты последнего изменения продукта, которое
автоматически обновляется при каждом сохранении записи в базе данных
(auto_now=True)
    """
    objects = None
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    preview_image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manufactured_at = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

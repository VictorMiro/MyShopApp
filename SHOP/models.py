from django.db import models


class TradeMark(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Торговая Марка'
        verbose_name_plural = 'Торговые Марки'

    def __str__(self):
        return self.name


class ModelType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Тип модели'
        verbose_name_plural = 'Типы моделей'

    def __str__(self):
        return self.name


class GadgetType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Тип Гаджета'
        verbose_name_plural = 'Типы Гаджетов'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    count = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products')
    discount = models.CharField(max_length=255, default=None)
    trade_mark = models.ForeignKey(TradeMark, on_delete=models.CASCADE)
    model_type = models.ForeignKey(ModelType, on_delete=models.CASCADE, default=None)
    gadget_type = models.ForeignKey(GadgetType, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = 'Гаджет'
        verbose_name_plural = 'Гаджеты'

    @property
    def total(self):
        return self.price * self.count

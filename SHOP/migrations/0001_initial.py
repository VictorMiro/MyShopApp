# Generated by Django 2.1.3 on 2018-11-15 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GadgetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Тип Гаджета',
                'verbose_name_plural': 'Типы Гаджетов',
            },
        ),
        migrations.CreateModel(
            name='ModelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Тип модели',
                'verbose_name_plural': 'Типы моделей',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('count', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='products')),
                ('discount', models.CharField(default=None, max_length=255)),
                ('gadget_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SHOP.GadgetType')),
                ('model_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SHOP.ModelType')),
            ],
            options={
                'verbose_name': 'Гаджет',
                'verbose_name_plural': 'Гаджеты',
            },
        ),
        migrations.CreateModel(
            name='TradeMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Торговая Марка',
                'verbose_name_plural': 'Торговые Марки',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='trade_mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SHOP.TradeMark'),
        ),
    ]

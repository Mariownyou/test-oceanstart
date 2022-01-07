# Generated by Django 4.0.1 on 2022-01-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('price_min', models.PositiveIntegerField()),
                ('price_max', models.PositiveIntegerField()),
                ('is_published', models.BooleanField(default=False)),
                ('is_removed', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(related_name='products', to='categories.Category')),
            ],
        ),
    ]
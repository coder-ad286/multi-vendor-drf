# Generated by Django 5.0.4 on 2024-04-21 23:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_customeraddress_default_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('reviews', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_ratings', to='main.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='main.product')),
            ],
        ),
    ]

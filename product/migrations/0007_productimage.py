# Generated by Django 5.0.7 on 2024-11-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_category_nested_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 3.2 on 2021-04-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog', '0002_alter_article_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='unique_id',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-29 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='comments',
            name='body',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]

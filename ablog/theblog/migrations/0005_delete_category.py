# Generated by Django 4.0.4 on 2022-04-24 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_category_post_catergory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]

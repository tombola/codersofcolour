# Generated by Django 3.0.7 on 2020-06-08 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('blog', '0003_blogindexpage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='image',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
        ),
    ]

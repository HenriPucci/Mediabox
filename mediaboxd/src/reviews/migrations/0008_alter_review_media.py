# Generated by Django 3.2.7 on 2021-10-26 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_alter_media_media_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='media',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reviews.media'),
            preserve_default=False,
        ),
    ]
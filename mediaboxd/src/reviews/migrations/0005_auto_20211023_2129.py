# Generated by Django 3.2.7 on 2021-10-23 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20211020_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_url', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('media_type', models.CharField(choices=[('book', 'Book'), ('movie', 'Movie'), ('music', 'Music'), ('game', 'Game'), ('other', 'Other')], default='other', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.media'),
        ),
    ]

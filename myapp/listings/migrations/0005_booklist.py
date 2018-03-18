# Generated by Django 2.0.2 on 2018-03-18 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0004_songlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.CharField(max_length=100)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('book_author', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

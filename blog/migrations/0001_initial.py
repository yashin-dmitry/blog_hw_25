# Generated by Django 5.1.2 on 2024-10-31 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('published', models.BooleanField(default=True)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'blog_post',
                'verbose_name_plural': 'blog_posts',
            },
        ),
    ]

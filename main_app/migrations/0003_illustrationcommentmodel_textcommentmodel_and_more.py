# Generated by Django 4.1.7 on 2023-02-27 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_dislike_commentmodel_ai_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IllustrationCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('human', models.PositiveSmallIntegerField(verbose_name='Human')),
                ('ai', models.PositiveSmallIntegerField(verbose_name='AI')),
                ('illustration', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.illustrationmodel', verbose_name='Illustration')),
            ],
        ),
        migrations.CreateModel(
            name='TextCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('human', models.PositiveSmallIntegerField(verbose_name='Human')),
                ('ai', models.PositiveSmallIntegerField(verbose_name='AI')),
                ('text', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.textmodel', verbose_name='Text')),
            ],
        ),
        migrations.DeleteModel(
            name='CommentModel',
        ),
    ]

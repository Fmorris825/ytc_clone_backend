# Generated by Django 4.0.4 on 2022-11-14 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comment_dislikes_alter_comment_likes'),
        ('replies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.comment'),
        ),
    ]

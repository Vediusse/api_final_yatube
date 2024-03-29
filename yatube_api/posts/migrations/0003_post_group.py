# Generated by Django 4.1.3 on 2022-12-03 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_group_follow"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="group",
            field=models.ForeignKey(
                blank=True,
                help_text="Выберите группу или оставьте пустым",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="posts",
                to="posts.group",
                verbose_name="select",
            ),
        ),
    ]

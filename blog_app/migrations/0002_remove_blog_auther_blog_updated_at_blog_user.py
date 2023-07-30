# Generated by Django 4.2.2 on 2023-07-29 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="blog", name="auther",),
        migrations.AddField(
            model_name="blog",
            name="updated_at",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="blog",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="blog",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]

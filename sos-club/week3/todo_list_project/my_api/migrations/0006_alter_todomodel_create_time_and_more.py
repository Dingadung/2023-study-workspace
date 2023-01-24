# Generated by Django 4.1.5 on 2023-01-24 09:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0005_todomodel_create_time_todomodel_modified_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='modified_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
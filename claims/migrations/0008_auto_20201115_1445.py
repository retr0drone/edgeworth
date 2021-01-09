# Generated by Django 3.1.3 on 2020-11-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0007_auto_20201115_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='claims',
            options={'verbose_name': 'claim', 'verbose_name_plural': 'claims'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='support_files',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]

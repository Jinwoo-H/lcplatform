# Generated by Django 4.2.9 on 2024-01-07 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_question_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.9 on 2024-01-06 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_question_belongs_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='belongs_to',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-22 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_auto_20210522_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='forQuestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='Quiz.questions'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='toQuiz',
            field=models.ManyToManyField(related_name='questions', to='Quiz.Quiz'),
        ),
    ]

# Generated by Django 3.2.5 on 2022-07-27 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_text', models.CharField(max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=100)),
                ('votes', models.IntegerField(default=0)),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.quote')),
            ],
        ),
    ]

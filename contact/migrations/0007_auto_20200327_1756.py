# Generated by Django 2.2.11 on 2020-03-27 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20200326_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='content',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='service',
            field=models.CharField(choices=[('쇼핑몰', '쇼핑몰'), ('챗봇', '챗봇'), ('IT솔루션', 'IT솔루션'), ('웹앱', '웹앱'), ('크롤링', '크롤링'), ('홈페이지', '홈페이지')], max_length=10),
        ),
    ]

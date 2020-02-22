# Generated by Django 3.0.2 on 2020-02-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20200120_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth',
            field=models.CharField(max_length=10, null=True, verbose_name='인증번호'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=5, null=True, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=17, unique=True, verbose_name='아이디'),
        ),
    ]
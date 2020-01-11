# Generated by Django 3.0.1 on 2020-01-11 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200112_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(choices=[('외부인', '학부생이 아님'), ('드론IOT시뮬레이션학부', '드론IOT시뮬레이션학부'), ('의과대학', '의과대학'), ('문리과대학', '문리과대학'), ('사회과학대학', '사회과학대학'), ('공과대학', '공과대학'), ('보건의료융합대학', '보건의료융합대학'), ('BNIT융합대학', 'BNIT융합대학'), ('약학대학', '약학대학')], max_length=24, null=True, verbose_name='학과'),
        ),
    ]
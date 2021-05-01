# Generated by Django 3.2 on 2021-05-01 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeerecipe', '0002_auto_20210501_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='size',
            field=models.CharField(choices=[('아리아나그란데', '아리아나그란데'), ('그란데말입니다', '그란데말입니다'), ('그란데밖에없는데', '그란데밖에없는데'), ('손에 담아마실게요', '손에 담아마실게요')], default='아리아나그란데', max_length=30),
        ),
        migrations.AlterField(
            model_name='content',
            name='taste',
            field=models.CharField(choices=[('인생의 쓴맛', '인생의 쓴맛'), ('어우달아!', '어우달아!'), ('밍밍한 한강물맛', '밍밍한 한강물맛'), ('마트..다녀오셨어요?', '마트..다녀오셨어요?'), ('매운맛', '매운맛')], default='인생의 쓴맛', max_length=30),
        ),
    ]

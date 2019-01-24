# Generated by Django 2.1.5 on 2019-01-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(default='', max_length=50, verbose_name='昵称')),
                ('username', models.CharField(default='', max_length=50, verbose_name='用户名')),
                ('password', models.CharField(default='', max_length=50, verbose_name='密码')),
                ('birthday', models.DateField(null=True, verbose_name='生日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=5)),
                ('address', models.CharField(default='', max_length=100)),
                ('mobile', models.CharField(blank=True, default='', max_length=11, null=True)),
                ('image', models.ImageField(default='/image/default.png', upload_to='image/%Y/%m')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]
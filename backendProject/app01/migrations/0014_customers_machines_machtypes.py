# Generated by Django 3.1.1 on 2020-10-10 16:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0013_auto_20201002_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('customerId', models.AutoField(primary_key=True, serialize=False, verbose_name='顾客id')),
                ('customerName', models.CharField(max_length=10, unique=True, verbose_name='顾客名')),
                ('customerType', models.CharField(max_length=30, verbose_name='顾客类型')),
                ('customerLevel', models.IntegerField(choices=[(1, 1), (1, 0)], verbose_name='顾客等级')),
                ('sponsor', models.CharField(max_length=6, verbose_name='赞助商')),
                ('phone', models.CharField(max_length=11, verbose_name='联系电话')),
                ('address', models.CharField(max_length=10, verbose_name='地址')),
                ('machCount', models.IntegerField(verbose_name='机器数目')),
                ('remark', models.CharField(max_length=10, verbose_name='remark')),
            ],
            options={
                'verbose_name': '客户',
                'verbose_name_plural': '客户',
                'db_table': '客户',
                'ordering': ['customerId'],
            },
        ),
        migrations.CreateModel(
            name='machTypes',
            fields=[
                ('machTypeId', models.AutoField(primary_key=True, serialize=False, verbose_name='机器类型id')),
                ('machTypeCode', models.CharField(default='defaultTypeCode', max_length=10, verbose_name='机器类型编号')),
                ('machTypeName', models.CharField(max_length=10, unique=True, verbose_name='机器类型名称')),
                ('machTypeDesc', models.CharField(max_length=30, verbose_name='机器类型描述')),
            ],
            options={
                'verbose_name': '机器类型',
                'verbose_name_plural': '机器类型',
                'db_table': '机器类型',
                'ordering': ['machTypeId'],
            },
        ),
        migrations.CreateModel(
            name='machines',
            fields=[
                ('machineId', models.AutoField(primary_key=True, serialize=False, verbose_name='机器id')),
                ('machineName', models.CharField(max_length=10, unique=True, verbose_name='机器名称')),
                ('machineDesc', models.TextField(max_length=30, verbose_name='机器描述')),
                ('dataOfProdect', models.DateTimeField(default=django.utils.timezone.now, verbose_name='生产日期')),
                ('office', models.CharField(max_length=10, verbose_name='办事处')),
                ('mwordId', models.IntegerField(default=1, verbose_name='mworkid')),
                ('customerName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers_customerName', to='app01.customers', verbose_name='客户')),
                ('machTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machine_machTypeId', to='app01.machtypes', verbose_name='机器类型id')),
            ],
            options={
                'verbose_name': '机器/设备',
                'verbose_name_plural': '机器/设备',
                'db_table': '设备',
                'ordering': ['machineId'],
            },
        ),
    ]
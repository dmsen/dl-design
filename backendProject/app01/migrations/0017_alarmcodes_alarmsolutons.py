# Generated by Django 3.1.1 on 2020-10-14 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_auto_20201012_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='alarmSolutons',
            fields=[
                ('alarmSolutonId', models.AutoField(primary_key=True, serialize=False, verbose_name='解决方案id')),
                ('alarmSolutonName', models.CharField(max_length=32, unique=True, verbose_name='解决方案名称')),
                ('alarmSolutonDetail', models.CharField(max_length=32, verbose_name='解决方案描述')),
                ('alarmCodeList', models.TextField(verbose_name='适用与异常码/组合码')),
            ],
            options={
                'verbose_name': '解决方案',
                'verbose_name_plural': '解决方案',
                'db_table': '解决方案',
                'ordering': ['alarmSolutonId'],
            },
        ),
        migrations.CreateModel(
            name='alarmCodes',
            fields=[
                ('alarmCodeId', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True, verbose_name='异常码id')),
                ('alarmCodeName', models.CharField(max_length=16, verbose_name='异常码名字')),
                ('minValue', models.IntegerField(default=0, verbose_name='最小值')),
                ('maxValue', models.IntegerField(verbose_name='最大值')),
                ('alarmMsg', models.CharField(blank=True, max_length=36, null=True, verbose_name='异常信息')),
                ('level', models.IntegerField(blank=True, default=1, null=True, verbose_name='异常级别')),
                ('timeLimit', models.IntegerField(blank=True, default=10, null=True, verbose_name='异常时延')),
                ('machineName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.machines', verbose_name='机器名')),
                ('physicalName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.iopoints', verbose_name='监控点物理量')),
            ],
            options={
                'verbose_name': '异常码',
                'verbose_name_plural': '异常码',
                'db_table': '异常码',
                'ordering': ['alarmCodeId'],
            },
        ),
    ]
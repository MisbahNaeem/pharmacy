# Generated by Django 3.1.4 on 2021-01-27 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_ssn', models.IntegerField(primary_key=True, serialize=False)),
                ('doctor_name', models.CharField(blank=True, max_length=30, null=True)),
                ('experience', models.IntegerField(blank=True, db_column='Experience', null=True)),
                ('specilization', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'doctor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('login_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=40, null=True)),
                ('password', models.CharField(blank=True, max_length=40, null=True)),
                ('userrole', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'manage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('m_id', models.IntegerField(primary_key=True, serialize=False)),
                ('manufacturer_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'manufacturer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manufactures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'manufactures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_ssn', models.IntegerField(primary_key=True, serialize=False)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('patient_name', models.CharField(blank=True, max_length=20, null=True)),
                ('patient_address', models.CharField(blank=True, max_length=70, null=True)),
                ('patient_phonenumber', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PrescribeSell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('date', models.CharField(blank=True, max_length=40, null=True)),
                ('bill', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'prescribe_sell',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Registeruser',
            fields=[
                ('login_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=40, null=True)),
                ('username', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('role', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'registeruser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tyype', models.CharField(blank=True, max_length=40, null=True)),
                ('stocknumber', models.IntegerField(blank=True, null=True)),
                ('sdescription', models.CharField(blank=True, max_length=50, null=True)),
                ('no_items', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'stock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'stock_supplier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.IntegerField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(blank=True, max_length=40, null=True)),
                ('supplier_type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'supplier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usert',
            fields=[
                ('user_ssn', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.CharField(blank=True, max_length=40, null=True)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('role', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'usert',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.TextField(blank=True, null=True)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('sales', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('drug_id', models.IntegerField(primary_key=True, serialize=False)),
                ('drugname', models.CharField(blank=True, max_length=40, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('manufacturing_date', models.DateField(blank=True, db_column='Manufacturing_date', null=True)),
                ('expiry_date', models.DateField(blank=True, db_column='Expiry_date', null=True)),
            ],
            options={
                'db_table': 'drugs',
                'managed': True,
            },
        ),
    ]

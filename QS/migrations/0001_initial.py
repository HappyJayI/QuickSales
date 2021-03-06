# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillD',
            fields=[
                ('InOutDSeq', models.AutoField(primary_key=True, serialize=False, verbose_name='입출고DSeq')),
                ('InOutSubSeq', models.IntegerField(verbose_name='입출고순번')),
                ('Qty', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True, verbose_name='수량')),
                ('InOutSubDivSeq', models.IntegerField(choices=[(1101, '내수구매'), (2101, '정상판매'), (2102, '판매반품'), (2201, '계산서'), (3101, '판촉사용'), (3102, '재고손실')], verbose_name='입출고구분항목')),
                ('Remark', models.CharField(blank=True, max_length=100, verbose_name='비고')),
                ('UnitSeq', models.IntegerField(blank=True, null=True, verbose_name='사원')),
                ('Price', models.FloatField(blank=True, null=True, verbose_name='외화단가')),
                ('Amt', models.FloatField(blank=True, null=True, verbose_name='외화금액')),
                ('BasePrice', models.FloatField(blank=True, null=True, verbose_name='단가')),
                ('BaseAmt', models.FloatField(blank=True, null=True, verbose_name='금액')),
            ],
            options={
                'verbose_name': '계산서품목',
                'verbose_name_plural': '계산서품목',
                'db_table': 'tinoutd',
            },
        ),
        migrations.CreateModel(
            name='BillM',
            fields=[
                ('InOutSeq', models.AutoField(db_column='InOutSeq', primary_key=True, serialize=False)),
                ('InOutDiv', models.IntegerField(choices=[(11, '구매입고'), (21, '거래명세'), (22, '계산서'), (31, '기타출고')], default=22, editable=False, verbose_name='입출고구분')),
                ('InOutNo', models.CharField(blank=True, max_length=100, verbose_name='계산서번호')),
                ('InOutDate', models.DateField(verbose_name='계산서일')),
                ('InOutName', models.CharField(blank=True, max_length=100, null=True, verbose_name='계산서명')),
                ('IsCfm', models.CharField(blank=True, choices=[('1', '확정')], max_length=1, null=True, verbose_name='확정여부')),
                ('Remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='비고')),
                ('EmpSeq', models.IntegerField(blank=True, null=True, verbose_name='사원')),
                ('ExSeq', models.IntegerField(blank=True, null=True, verbose_name='통화')),
                ('ExRatio', models.FloatField(blank=True, null=True, verbose_name='환율')),
            ],
            options={
                'verbose_name': '계산서',
                'verbose_name_plural': '계산서',
                'db_table': 'tinoutm',
            },
        ),
        migrations.CreateModel(
            name='CollectD',
            fields=[
                ('CollectDSeq', models.AutoField(primary_key=True, serialize=False, verbose_name='수금DSeq')),
                ('CollectSubSeq', models.IntegerField(verbose_name='수금순번')),
                ('CollectSubDivSeq', models.IntegerField(choices=[(1, '현금'), (2, '어음')], verbose_name='수금구분항목')),
                ('Remark', models.CharField(blank=True, max_length=100, verbose_name='비고')),
                ('Amt', models.FloatField(blank=True, null=True, verbose_name='외화금액')),
                ('BaseAmt', models.FloatField(blank=True, null=True, verbose_name='금액')),
            ],
            options={
                'verbose_name': '수금품목',
                'verbose_name_plural': '수금품목',
                'db_table': 'tcollectd',
            },
        ),
        migrations.CreateModel(
            name='CollectM',
            fields=[
                ('CollectSeq', models.AutoField(db_column='CollectSeq', primary_key=True, serialize=False)),
                ('CollectDiv', models.IntegerField(choices=[(1, '외상매출'), (2, '선수'), (3, '미수')], default=21, editable=False, verbose_name='수금구분')),
                ('CollectNo', models.CharField(blank=True, max_length=100, verbose_name='수금번호')),
                ('CollectDate', models.DateField(verbose_name='수금일')),
                ('CollectName', models.CharField(blank=True, max_length=100, null=True, verbose_name='수금명')),
                ('IsCfm', models.CharField(blank=True, choices=[('1', '확정')], max_length=1, verbose_name='확정여부')),
                ('Remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='비고')),
                ('EmpSeq', models.IntegerField(blank=True, null=True, verbose_name='사원')),
                ('ExSeq', models.IntegerField(blank=True, null=True, verbose_name='통화')),
                ('ExRatio', models.FloatField(blank=True, null=True, verbose_name='환율')),
            ],
            options={
                'verbose_name': '수금',
                'verbose_name_plural': '수금',
                'db_table': 'tcollectm',
            },
        ),
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('CustSeq', models.AutoField(primary_key=True, serialize=False)),
                ('CustNo', models.CharField(max_length=100, verbose_name='거래처번호')),
                ('CustName', models.CharField(max_length=100, verbose_name='거래처명')),
                ('Remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='비고')),
                ('BizNo', models.CharField(blank=True, max_length=30, null=True, verbose_name='사업자번호')),
                ('Addr', models.CharField(blank=True, max_length=100, null=True, verbose_name='주소')),
                ('Tel1', models.CharField(blank=True, max_length=30, null=True, verbose_name='전화1')),
                ('Tel2', models.CharField(blank=True, max_length=30, null=True, verbose_name='전화2')),
                ('TaxEmail', models.CharField(blank=True, max_length=100, null=True, verbose_name='전자세금계산서 emaiil')),
                ('TaxEmpName', models.CharField(blank=True, max_length=50, null=True, verbose_name='전자세금계산서 담당자')),
                ('USpec1', models.CharField(blank=True, max_length=100, null=True, verbose_name='사용자정의1')),
                ('USpec2', models.CharField(blank=True, max_length=100, null=True, verbose_name='사용자정의2')),
                ('USpec3', models.CharField(blank=True, max_length=100, null=True, verbose_name='사용자정의3')),
                ('USpec4', models.CharField(blank=True, max_length=100, null=True, verbose_name='사용자정의4')),
            ],
            options={
                'verbose_name': '거래처',
                'verbose_name_plural': '거래처',
                'db_table': 'tcust',
            },
        ),
        migrations.CreateModel(
            name='DCode',
            fields=[
                ('DCodeSeq', models.AutoField(primary_key=True, serialize=False)),
                ('DCodeName', models.CharField(max_length=100, verbose_name='D코드명')),
                ('DCodeValue', models.CharField(max_length=100, verbose_name='D코드값')),
                ('Remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='비고')),
            ],
            options={
                'verbose_name': 'D코드',
                'verbose_name_plural': 'D코드',
                'db_table': 'tdcode',
            },
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('EmpSeq', models.AutoField(primary_key=True, serialize=False)),
                ('EmpNo', models.CharField(max_length=10, verbose_name='사번')),
                ('EmpName', models.CharField(max_length=100, verbose_name='사원명')),
                ('Remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='비고')),
            ],
            options={
                'verbose_name': '사원',
                'verbose_name_plural': '사원',
                'db_table': 'temp',
            },
        ),
        migrations.CreateModel(
            name='InOutD',
            fields=[
                ('InOutDSeq', models.AutoField(primary_key=True, serialize=False, verbose_name='입출고DSeq')),
                ('InOutSubSeq', models.IntegerField(verbose_name='입출고순번')),
                ('Qty', models.DecimalField(blank=True, decimal_places=0, default=1, max_digits=20, null=True, verbose_name='수량')),
                ('InOutSubDivSeq', models.IntegerField(choices=[(1101, '내수구매'), (2101, '정상판매'), (2102, '판매반품'), (2201, '계산서'), (3101, '판촉사용'), (3102, '재고손실')], verbose_name='입출고구분항목')),
                ('Remark', models.CharField(max_length=100, verbose_name='비고')),
                ('UnitSeq', models.IntegerField(blank=True, null=True, verbose_name='사원코드')),
                ('Price', models.FloatField(blank=True, null=True, verbose_name='외화단가')),
                ('Amt', models.FloatField(blank=True, null=True, verbose_name='외화금액')),
                ('BasePrice', models.FloatField(blank=True, null=True, verbose_name='단가')),
                ('BaseAmt', models.FloatField(blank=True, null=True, verbose_name='금액')),
            ],
            options={
                'verbose_name': '입출고품목',
                'verbose_name_plural': '입출고품목',
                'db_table': 'tinoutd',
            },
        ),
        migrations.CreateModel(
            name='InOutM',
            fields=[
                ('InOutSeq', models.AutoField(db_column='InOutSeq', primary_key=True, serialize=False)),
                ('InOutDiv', models.IntegerField(choices=[(11, '구매입고'), (21, '거래명세'), (22, '계산서'), (31, '기타출고')], verbose_name='입출고구분')),
                ('InOutNo', models.CharField(max_length=100, verbose_name='입출고번호')),
                ('InOutDate', models.DateField(verbose_name='입출고일')),
                ('InOutName', models.CharField(blank=True, max_length=100, null=True, verbose_name='입출고명')),
                ('IsCfm', models.CharField(choices=[('1', '확정')], max_length=1, verbose_name='확정여부')),
                ('Remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='비고')),
                ('EmpSeq', models.IntegerField(blank=True, null=True, verbose_name='사원코드')),
                ('ExSeq', models.IntegerField(blank=True, null=True, verbose_name='통화')),
                ('ExRatio', models.FloatField(blank=True, null=True, verbose_name='환율')),
                ('USpec1', models.CharField(blank=True, max_length=100, null=True, verbose_name='사용자정의1')),
                ('USpec2', models.CharField(blank=True, max_length=100, null=True, verbose_name='사용자정의2')),
                ('USpec3', models.CharField(blank=True, max_length=100, null=True, verbose_name='사용자정의3')),
                ('USpec4', models.CharField(blank=True, max_length=100, null=True, verbose_name='사용자정의4')),
                ('CustSeq', models.ForeignKey(db_column='CustSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.Cust', verbose_name='거래처')),
            ],
            options={
                'verbose_name': '입출고',
                'verbose_name_plural': '입출고',
                'db_table': 'tinoutm',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('InventorySeq', models.IntegerField(primary_key=True, serialize=False)),
                ('InQty', models.FloatField(verbose_name='입고수량')),
                ('OutQty', models.FloatField(verbose_name='출고수량')),
                ('StockQty', models.FloatField(verbose_name='재고수량')),
            ],
            options={
                'verbose_name': '재고',
                'verbose_name_plural': '재고',
                'db_table': 'vinventory',
            },
        ),
        migrations.CreateModel(
            name='InvoiceD',
            fields=[
                ('InOutDSeq', models.AutoField(primary_key=True, serialize=False, verbose_name='입출고DSeq')),
                ('InOutSubSeq', models.IntegerField(verbose_name='입출고순번')),
                ('Qty', models.FloatField(blank=True, null=True, verbose_name='수량')),
                ('InOutSubDivSeq', models.IntegerField(choices=[(1101, '내수구매'), (2101, '정상판매'), (2102, '판매반품'), (2201, '계산서'), (3101, '판촉사용'), (3102, '재고손실')], verbose_name='입출고구분항목')),
                ('Remark', models.CharField(blank=True, max_length=100, verbose_name='비고')),
                ('UnitSeq', models.IntegerField(blank=True, null=True, verbose_name='사원')),
                ('Price', models.FloatField(blank=True, null=True, verbose_name='단가')),
                ('Amt', models.FloatField(blank=True, verbose_name='금액')),
                ('BasePrice', models.FloatField(blank=True, verbose_name='기준단가')),
                ('BaseAmt', models.FloatField(blank=True, null=True, verbose_name='기준금액')),
            ],
            options={
                'verbose_name': '거래명세품목',
                'verbose_name_plural': '거래명세품목',
                'db_table': 'tinoutd',
            },
        ),
        migrations.CreateModel(
            name='InvoiceM',
            fields=[
                ('InOutSeq', models.AutoField(db_column='InOutSeq', primary_key=True, serialize=False)),
                ('InOutDiv', models.IntegerField(choices=[(11, '구매입고'), (21, '거래명세'), (22, '계산서'), (31, '기타출고')], default=21, editable=False, verbose_name='입출고구분')),
                ('InOutNo', models.CharField(blank=True, max_length=100, verbose_name='거래명세번호')),
                ('InOutDate', models.DateField(verbose_name='거래명세일')),
                ('InOutName', models.CharField(blank=True, max_length=100, null=True, verbose_name='거래명')),
                ('IsCfm', models.CharField(blank=True, choices=[('1', '확정')], max_length=1, null=True, verbose_name='확정여부')),
                ('Remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='비고')),
                ('EmpSeq', models.IntegerField(blank=True, null=True, verbose_name='사원')),
                ('ExSeq', models.IntegerField(blank=True, null=True, verbose_name='통화')),
                ('ExRatio', models.FloatField(blank=True, null=True, verbose_name='환율')),
                ('CustSeq', models.ForeignKey(db_column='CustSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.Cust', verbose_name='거래처')),
            ],
            options={
                'verbose_name': '거래명세',
                'verbose_name_plural': '거래명세',
                'db_table': 'tinoutm',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('ItemSeq', models.AutoField(primary_key=True, serialize=False)),
                ('ItemNo', models.CharField(max_length=100, verbose_name='품번')),
                ('ItemName', models.CharField(max_length=100, verbose_name='품명')),
                ('Spec', models.CharField(max_length=100, verbose_name='규격')),
                ('USpec1', models.CharField(blank=True, choices=[('01', '대형매장용'), ('02', '가정용'), ('03', '유흥음식점용'), ('04', '기타')], max_length=100, null=True, verbose_name='용도구분')),
                ('USpec2', models.CharField(blank=True, choices=[('01', '주정'), ('02', '탁주'), ('03', '약주'), ('04', '청주'), ('05', '맥주'), ('06', '과실주'), ('07', '증류식소주'), ('08', '희석식소주'), ('09', '위스키'), ('10', '브랜디'), ('11', '일반증류주'), ('12', '리큐르'), ('13', '기타추류')], max_length=100, null=True, verbose_name='주종구분')),
                ('Remark', models.CharField(max_length=100, verbose_name='비고')),
                ('Uptdate', models.DateTimeField(blank=True, editable=False, null=True)),
            ],
            options={
                'verbose_name': '품목',
                'verbose_name_plural': '품목',
                'db_table': 'titem',
            },
        ),
        migrations.CreateModel(
            name='MCode',
            fields=[
                ('MCodeSeq', models.AutoField(primary_key=True, serialize=False)),
                ('MCodeNo', models.CharField(max_length=10, primary_key=True, verbose_name='M코드번호')),
                ('MCodeName', models.CharField(max_length=100, verbose_name='M코드명')),
                ('Remark', models.CharField(max_length=100, verbose_name='비고')),
            ],
            options={
                'verbose_name': 'M코드',
                'verbose_name_plural': 'M코드',
                'db_table': 'tmcode',
            },
        ),
        migrations.CreateModel(
            name='PurchaseBillD',
            fields=[
                ('InOutDSeq', models.AutoField(primary_key=True, serialize=False, verbose_name='입출고DSeq')),
                ('InOutSubSeq', models.IntegerField(verbose_name='입출고순번')),
                ('Qty', models.DecimalField(blank=True, decimal_places=0, default=1, max_digits=20, null=True, verbose_name='수량')),
                ('InOutSubDivSeq', models.IntegerField(choices=[(1101, '내수구매'), (2101, '정상판매'), (2102, '판매반품'), (2201, '계산서'), (3101, '판촉사용'), (3102, '재고손실')], verbose_name='입출고구분항목')),
                ('Remark', models.CharField(max_length=100, verbose_name='비고')),
                ('UnitSeq', models.IntegerField(blank=True, null=True, verbose_name='사원코드')),
                ('Price', models.FloatField(blank=True, null=True, verbose_name='외화단가')),
                ('Amt', models.FloatField(blank=True, null=True, verbose_name='외화금액')),
                ('BasePrice', models.FloatField(blank=True, null=True, verbose_name='단가')),
                ('BaseAmt', models.FloatField(blank=True, null=True, verbose_name='금액')),
            ],
            options={
                'verbose_name': '계산서품목',
                'verbose_name_plural': '계산서품목',
                'db_table': 'tinoutd',
            },
        ),
        migrations.CreateModel(
            name='PurchaseBillM',
            fields=[
                ('InOutSeq', models.AutoField(db_column='InOutSeq', primary_key=True, serialize=False)),
                ('InOutDiv', models.IntegerField(choices=[(11, '구매입고'), (21, '거래명세'), (22, '계산서'), (31, '기타출고')], default=11, editable=False, verbose_name='입출고구분')),
                ('InOutNo', models.CharField(max_length=100, verbose_name='계산서번호')),
                ('InOutDate', models.DateField(verbose_name='계산서일')),
                ('InOutName', models.CharField(blank=True, max_length=100, null=True, verbose_name='계산서명')),
                ('IsCfm', models.CharField(choices=[('1', '확정')], max_length=1, verbose_name='확정여부')),
                ('Remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='비고')),
                ('EmpSeq', models.IntegerField(blank=True, null=True, verbose_name='사원코드')),
                ('ExSeq', models.IntegerField(blank=True, null=True, verbose_name='통화')),
                ('ExRatio', models.FloatField(blank=True, null=True, verbose_name='환율')),
                ('CustSeq', models.ForeignKey(db_column='CustSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.Cust', verbose_name='거래처')),
            ],
            options={
                'verbose_name': '계산서',
                'verbose_name_plural': '계산서',
                'db_table': 'tinoutm',
            },
        ),
        migrations.CreateModel(
            name='PurchaseD',
            fields=[
                ('InOutDSeq', models.AutoField(primary_key=True, serialize=False, verbose_name='입출고DSeq')),
                ('InOutSubSeq', models.IntegerField(verbose_name='입출고순번')),
                ('Qty', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True, verbose_name='수량')),
                ('InOutSubDivSeq', models.IntegerField(choices=[(1101, '내수구매'), (2101, '정상판매'), (2102, '판매반품'), (2201, '계산서'), (3101, '판촉사용'), (3102, '재고손실')], verbose_name='입출고구분항목')),
                ('Remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='비고')),
                ('UnitSeq', models.IntegerField(blank=True, null=True, verbose_name='사원코드')),
                ('Price', models.FloatField(blank=True, null=True, verbose_name='외화단가')),
                ('Amt', models.FloatField(blank=True, null=True, verbose_name='외화금액')),
                ('BasePrice', models.FloatField(blank=True, null=True, verbose_name='단가')),
                ('BaseAmt', models.FloatField(blank=True, null=True, verbose_name='금액')),
            ],
            options={
                'verbose_name': '구매입고품목',
                'verbose_name_plural': '구매입고품목',
                'db_table': 'tinoutd',
            },
        ),
        migrations.CreateModel(
            name='PurchaseM',
            fields=[
                ('InOutSeq', models.AutoField(db_column='InOutSeq', primary_key=True, serialize=False)),
                ('InOutDiv', models.IntegerField(choices=[(11, '구매입고'), (21, '거래명세'), (22, '계산서'), (31, '기타출고')], default=11, verbose_name='입출고구분')),
                ('InOutNo', models.CharField(blank=True, max_length=100, verbose_name='구매입고번호')),
                ('InOutDate', models.DateField(verbose_name='구매입고일')),
                ('InOutName', models.CharField(blank=True, max_length=100, null=True, verbose_name='거래명')),
                ('IsCfm', models.CharField(blank=True, choices=[('1', '확정')], max_length=1, null=True, verbose_name='확정여부')),
                ('Remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='비고')),
                ('EmpSeq', models.IntegerField(blank=True, null=True, verbose_name='사원코드')),
                ('ExSeq', models.IntegerField(blank=True, null=True, verbose_name='통화')),
                ('ExRatio', models.FloatField(blank=True, null=True, verbose_name='환율')),
                ('CustSeq', models.ForeignKey(db_column='CustSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.Cust', verbose_name='거래처')),
            ],
            options={
                'verbose_name': '구매입고',
                'verbose_name_plural': '구매입고',
                'db_table': 'tinoutm',
            },
        ),
        migrations.AddField(
            model_name='purchased',
            name='InOutSeq',
            field=models.ForeignKey(db_column='InOutSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.PurchaseM', verbose_name='입출고Seq'),
        ),
        migrations.AddField(
            model_name='purchased',
            name='ItemSeq',
            field=models.ForeignKey(db_column='ItemSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.Item', verbose_name='품목'),
        ),
        migrations.AddField(
            model_name='purchasebilld',
            name='InOutSeq',
            field=models.ForeignKey(db_column='InOutSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.PurchaseBillM', verbose_name='입출고Seq'),
        ),
        migrations.AddField(
            model_name='purchasebilld',
            name='ItemSeq',
            field=models.ForeignKey(db_column='ItemSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.Item', verbose_name='품목'),
        ),
        migrations.AddField(
            model_name='invoiced',
            name='InOutSeq',
            field=models.ForeignKey(db_column='InOutSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.InvoiceM', verbose_name='입출고Seq'),
        ),
        migrations.AddField(
            model_name='invoiced',
            name='ItemSeq',
            field=models.ForeignKey(db_column='ItemSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.Item', verbose_name='품목'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='ItemSeq',
            field=models.ForeignKey(db_column='ItemSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.Item', verbose_name='품목'),
        ),
        migrations.AddField(
            model_name='inoutd',
            name='InOutSeq',
            field=models.ForeignKey(db_column='InOutSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.InOutM', verbose_name='입출고Seq'),
        ),
        migrations.AddField(
            model_name='inoutd',
            name='ItemSeq',
            field=models.ForeignKey(db_column='ItemSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.Item', verbose_name='품목'),
        ),
        migrations.AddField(
            model_name='dcode',
            name='MCodeSeq',
            field=models.ForeignKey(db_column='MCodeSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.MCode', verbose_name='M코드'),
        ),
        migrations.AddField(
            model_name='collectm',
            name='CustSeq',
            field=models.ForeignKey(db_column='CustSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.Cust', verbose_name='거래처'),
        ),
        migrations.AddField(
            model_name='collectd',
            name='CollectSeq',
            field=models.ForeignKey(db_column='CollectSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.CollectM', verbose_name='수금Seq'),
        ),
        migrations.AddField(
            model_name='collectd',
            name='InOutDSeq',
            field=models.ForeignKey(blank=True, db_column='OriginInOutDSeq', null=True, on_delete=django.db.models.deletion.CASCADE, to='QS.BillD', verbose_name='계산서DSeq'),
        ),
        migrations.AddField(
            model_name='billm',
            name='CustSeq',
            field=models.ForeignKey(db_column='CustSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.Cust', verbose_name='거래처'),
        ),
        migrations.AddField(
            model_name='billd',
            name='InOutSeq',
            field=models.ForeignKey(db_column='InOutSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.BillM', verbose_name='입출고Seq'),
        ),
        migrations.AddField(
            model_name='billd',
            name='ItemSeq',
            field=models.ForeignKey(db_column='ItemSeq', on_delete=django.db.models.deletion.CASCADE, to='QS.Item', verbose_name='품목'),
        ),
        migrations.AlterUniqueTogether(
            name='purchased',
            unique_together=set([('InOutSeq', 'InOutSubSeq')]),
        ),
        migrations.AlterUniqueTogether(
            name='purchasebilld',
            unique_together=set([('InOutSeq', 'InOutSubSeq')]),
        ),
        migrations.AlterUniqueTogether(
            name='invoiced',
            unique_together=set([('InOutSeq', 'InOutSubSeq')]),
        ),
        migrations.AlterUniqueTogether(
            name='inoutm',
            unique_together=set([('InOutDiv', 'InOutNo')]),
        ),
        migrations.AlterUniqueTogether(
            name='inoutd',
            unique_together=set([('InOutSeq', 'InOutSubSeq')]),
        ),
        migrations.AlterUniqueTogether(
            name='collectd',
            unique_together=set([('CollectSeq', 'CollectSubSeq')]),
        ),
        migrations.AlterUniqueTogether(
            name='billd',
            unique_together=set([('InOutSeq', 'InOutSubSeq')]),
        ),
    ]

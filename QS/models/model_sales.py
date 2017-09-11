from django.db import models
from django.utils import timezone
from .model_common import *

#거래명세
class InvoiceM(models.Model):    
    InOutSeq = models.AutoField(db_column="InOutSeq",primary_key=True)
    InOutDiv = models.IntegerField(default=getChoicecode(InOutDiv_Code,"invoice"),editable=False, choices=InOutDiv_Choices,verbose_name="입출고구분") #/*11:구매입고,21:거래명세,22:계산서,31:기타출고*/
    InOutNo = models.CharField(max_length=100,blank=True,null=True,verbose_name="거래명세번호")
    InOutDate = models.DateField(verbose_name="거래명세일")
    InOutName = models.CharField(max_length=100,blank=True,null=True,verbose_name="거래명")
    IsCfm = models.CharField(max_length=1,choices=IsCfm_Choices,blank=True,null=True,verbose_name="확정여부")
    Remark = models.CharField(max_length=100,blank=True,null=True,verbose_name="비고")
    CustSeq = models.ForeignKey(Cust, db_column="CustSeq",verbose_name="거래처")
    EmpSeq = models.IntegerField(blank=True,null=True,verbose_name="사원코드")
    ExSeq = models.IntegerField(blank=True,null=True,verbose_name="통화")
    ExRatio = models.FloatField(blank=True,null=True,verbose_name="환율")

    def __str__(self):
        return "%s %s" %(self.InOutNo,self.InOutDate)

    class Meta:
        db_table = "tinoutm"
        verbose_name="거래명세"
        verbose_name_plural = "거래명세"        

class InvoiceD(models.Model):     
    InOutDSeq = models.AutoField(primary_key=True,verbose_name="입출고DSeq")   
    InOutSeq = models.ForeignKey(InvoiceM, db_column="InOutSeq",verbose_name="입출고Seq")
    InOutSubSeq = models.IntegerField(verbose_name="입출고순번")
    ItemSeq = models.ForeignKey(Item, db_column="ItemSeq",verbose_name="품목")
    Qty = models.DecimalField(decimal_places=0,max_digits=20,blank=True,null=True,verbose_name="수량")
    InOutSubDivSeq = models.IntegerField(choices=InOutSubDiv_Choices,verbose_name="입출고구분항목") 
    Remark = models.CharField(max_length=100,verbose_name="비고")
    UnitSeq = models.IntegerField(blank=True,null=True,verbose_name="사원코드")
    Price = models.FloatField(blank=True,null=True,verbose_name="외화단가")
    Amt = models.FloatField(blank=True,null=True,verbose_name="외화금액")
    BasePrice = models.FloatField(blank=True,null=True,verbose_name="단가")
    BaseAmt = models.FloatField(blank=True,null=True,verbose_name="금액")

    def __str__(self):
        return "%s %s" %(self.InOutSeq,self.InOutSubSeq)

    class Meta:
        db_table = "tinoutd"   
        verbose_name="거래명세품목"
        verbose_name_plural = "거래명세품목"  
        unique_together = (("InOutSeq", "InOutSubSeq"),)             

#계산서
class BillM(models.Model):    
    InOutSeq = models.AutoField(db_column="InOutSeq",primary_key=True)
    InOutDiv = models.IntegerField(default=getChoicecode(InOutDiv_Code,"bill"),editable=False, choices=InOutDiv_Choices,verbose_name="입출고구분") #/*11:구매입고,21:거래명세,22:계산서,31:기타출고*/
    InOutNo = models.CharField(max_length=100,blank=True,null=True,verbose_name="계산서번호")
    InOutDate = models.DateField(verbose_name="계산서일")
    InOutName = models.CharField(max_length=100,blank=True,null=True,verbose_name="계산서명")
    IsCfm = models.CharField(max_length=1,choices=IsCfm_Choices,blank=True,null=True,verbose_name="확정여부")
    Remark = models.CharField(max_length=100,blank=True,null=True,verbose_name="비고")
    CustSeq = models.ForeignKey(Cust, db_column="CustSeq",verbose_name="거래처")
    EmpSeq = models.IntegerField(blank=True,null=True,verbose_name="사원코드")
    ExSeq = models.IntegerField(blank=True,null=True,verbose_name="통화")
    ExRatio = models.FloatField(blank=True,null=True,verbose_name="환율")

    def __str__(self):
        return "%s %s" %(self.InOutNo,self.InOutDate)

    class Meta:
        db_table = "tinoutm"
        verbose_name="계산서"
        verbose_name_plural = "계산서"        

class BillD(models.Model):     
    InOutDSeq = models.AutoField(primary_key=True,verbose_name="입출고DSeq")   
    InOutSeq = models.ForeignKey(BillM, db_column="InOutSeq",verbose_name="입출고Seq")
    InOutSubSeq = models.IntegerField(verbose_name="입출고순번")
    ItemSeq = models.ForeignKey(Item, db_column="ItemSeq",verbose_name="품목")
    Qty = models.DecimalField(decimal_places=0,max_digits=20,blank=True,null=True,verbose_name="수량")
    InOutSubDivSeq = models.IntegerField(choices=InOutSubDiv_Choices,verbose_name="입출고구분항목") 
    Remark = models.CharField(max_length=100,verbose_name="비고")
    UnitSeq = models.IntegerField(blank=True,null=True,verbose_name="사원코드")
    Price = models.FloatField(blank=True,null=True,verbose_name="외화단가")
    Amt = models.FloatField(blank=True,null=True,verbose_name="외화금액")
    BasePrice = models.FloatField(blank=True,null=True,verbose_name="단가")
    BaseAmt = models.FloatField(blank=True,null=True,verbose_name="금액")

    def __str__(self):
        return "%s %s" %(self.InOutSeq,self.InOutSubSeq)

    class Meta:
        db_table = "tinoutd"   
        verbose_name="계산서품목"
        verbose_name_plural = "계산서품목"  
        unique_together = (("InOutSeq", "InOutSubSeq"),)                     


#수금
class CollectM(models.Model):    
    CollectSeq = models.AutoField(db_column="CollectSeq",primary_key=True)
    CollectDiv = models.IntegerField(default=21,editable=False, choices=CollectDiv_Choices,verbose_name="수금구분") #/*11:구매입고,21:거래명세,22:수금,31:기타출고*/
    CollectNo = models.CharField(max_length=100,verbose_name="수금번호")
    CollectDate = models.DateField(verbose_name="수금일")
    CollectName = models.CharField(max_length=100,blank=True,null=True,verbose_name="수금명")
    IsCfm = models.CharField(max_length=1,choices=IsCfm_Choices,verbose_name="확정여부")
    Remark = models.CharField(max_length=100,blank=True,null=True,verbose_name="비고")
    CustSeq = models.ForeignKey(Cust, db_column="CustSeq",verbose_name="거래처")
    EmpSeq = models.IntegerField(blank=True,null=True,verbose_name="사원코드")
    ExSeq = models.IntegerField(blank=True,null=True,verbose_name="통화")
    ExRatio = models.FloatField(blank=True,null=True,verbose_name="환율")

    def __str__(self):
        return "%s %s" %(self.CollectNo,self.CollectDate)

    class Meta:
        db_table = "tcollectm"
        verbose_name="수금"
        verbose_name_plural = "수금"        

class CollectD(models.Model):     
    CollectDSeq = models.AutoField(primary_key=True,verbose_name="수금DSeq")   
    CollectSeq = models.ForeignKey(CollectM, db_column="CollectSeq",verbose_name="수금Seq")
    CollectSubSeq = models.IntegerField(verbose_name="수금순번")
    CollectSubDivSeq = models.IntegerField(choices=CollectSubDiv_Choices,verbose_name="수금구분항목") 
    Remark = models.CharField(max_length=100,verbose_name="비고")
    Amt = models.FloatField(blank=True,null=True,verbose_name="외화금액")
    BaseAmt = models.FloatField(blank=True,null=True,verbose_name="금액")
    OriginInOutDSeq = models.ForeignKey(InOutD,blank=True,null=True,verbose_name="계산서DSeq")

    def __str__(self):
        return "%s %s" %(self.CollectSeq,self.CollectSubSeq)

    class Meta:
        db_table = "tcollectd"   
        verbose_name="수금품목"
        verbose_name_plural = "수금품목"  
        unique_together = (("CollectSeq", "CollectSubSeq"),)      
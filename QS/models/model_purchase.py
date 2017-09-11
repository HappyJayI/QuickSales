from django.db import models
from django.utils import timezone
from .model_common import *
from django.db import connection

class PurchaseM(models.Model):    
    InOutSeq = models.AutoField(db_column="InOutSeq",primary_key=True)
    InOutDiv = models.IntegerField(default=getChoicecode(InOutDiv_Code,"purchase"),choices=InOutDiv_Choices,verbose_name="입출고구분") #/*11:구매입고,21:구매입고,22:계산서,31:기타출고*/
    InOutNo = models.CharField(max_length=100,blank=True,verbose_name="구매입고번호")
    InOutDate = models.DateField(verbose_name="구매입고일")
    InOutName = models.CharField(max_length=100,blank=True,null=True,verbose_name="거래명")
    IsCfm = models.CharField(max_length=1,blank=True,null=True,choices=IsCfm_Choices,verbose_name="확정여부")
    Remark = models.CharField(max_length=100,blank=True,null=True,verbose_name="비고")
    CustSeq = models.ForeignKey(Cust, db_column="CustSeq",verbose_name="거래처")
    EmpSeq = models.IntegerField(blank=True,null=True,verbose_name="사원코드")
    ExSeq = models.IntegerField(blank=True,null=True,verbose_name="통화")
    ExRatio = models.FloatField(blank=True,null=True,verbose_name="환율")
    #UptDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s" %(self.InOutNo,self.InOutDate)

    def save(self, *args, **kwargs):
        strInOutDate = str(self.InOutDate).replace("-","")

        # if self.InOutSeq == None:
        #     if self.InOutNo == "" :
        #         #cursor 리턴값 확인...
        #         with connection.cursor() as cursor:
        #             cursor.execute( "SELECT max(InOutNo) as InOutNo FROM tinoutm where InOutDate='%s'"%str(self.InOutDate) )
        #             NewNo = cursor.fetchone()    

        #             if NewNo[0] != None:
        #                  self.InOutNo = getChoicecode(InOutDiv_Code,'purchase',2) + strInOutDate + str(int(NewNo[0][-3:]) + 1).rjust(3,'0')
        #             else:
        #                 self.InOutNo = getChoicecode(InOutDiv_Code,'purchase',2) + strInOutDate + '001'                    
        getNo(self)
        
        super(PurchaseM, self).save(*args, **kwargs)

    class Meta:
        db_table = "tinoutm"
        verbose_name="구매입고"
        verbose_name_plural = "구매입고"        

class PurchaseD(models.Model):     
    InOutDSeq = models.AutoField(primary_key=True,verbose_name="입출고DSeq")   
    InOutSeq = models.ForeignKey(PurchaseM, db_column="InOutSeq",verbose_name="입출고Seq")
    InOutSubSeq = models.IntegerField(verbose_name="입출고순번")
    ItemSeq = models.ForeignKey(Item, db_column="ItemSeq",verbose_name="품목")
    Qty = models.DecimalField(decimal_places=0,max_digits=20,blank=True,null=True,verbose_name="수량")
    InOutSubDivSeq = models.IntegerField(choices=InOutSubDiv_Choices,verbose_name="입출고구분항목") 
    Remark = models.CharField(max_length=100,blank=True,null=True,verbose_name="비고")
    UnitSeq = models.IntegerField(blank=True,null=True,verbose_name="사원코드")
    Price = models.FloatField(blank=True,null=True,verbose_name="외화단가")
    Amt = models.FloatField(blank=True,null=True,verbose_name="외화금액")
    BasePrice = models.FloatField(blank=True,null=True,verbose_name="단가")
    BaseAmt = models.FloatField(blank=True,null=True,verbose_name="금액")

    def __str__(self):
        return "%s %s" %(self.InOutSeq,self.InOutSubSeq)

    class Meta:
        db_table = "tinoutd"   
        verbose_name="구매입고품목"
        verbose_name_plural = "구매입고품목"  
        unique_together = (("InOutSeq", "InOutSubSeq"),)             


class PurchaseBillM(models.Model):    
    InOutSeq = models.AutoField(db_column="InOutSeq",primary_key=True)
    InOutDiv = models.IntegerField(default=getChoicecode(InOutDiv_Code,"purchase"),editable=False, choices=InOutDiv_Choices,verbose_name="입출고구분") #/*11:구매입고,21:구매입고,22:계산서,31:기타출고*/
    InOutNo = models.CharField(max_length=100,verbose_name="계산서번호")
    InOutDate = models.DateField(verbose_name="계산서일")
    InOutName = models.CharField(max_length=100,blank=True,null=True,verbose_name="계산서명")
    IsCfm = models.CharField(max_length=1,choices=IsCfm_Choices,verbose_name="확정여부")
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

class PurchaseBillD(models.Model):     
    InOutDSeq = models.AutoField(primary_key=True,verbose_name="입출고DSeq")   
    InOutSeq = models.ForeignKey(PurchaseBillM, db_column="InOutSeq",verbose_name="입출고Seq")
    InOutSubSeq = models.IntegerField(verbose_name="입출고순번")
    ItemSeq = models.ForeignKey(Item, db_column="ItemSeq",verbose_name="품목")
    Qty = models.DecimalField(default=1,decimal_places=0,max_digits=20,blank=True,null=True,verbose_name="수량")
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
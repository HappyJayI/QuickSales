from django.db import models
from django.utils import timezone

IsCfm_Choices = (
    ('1', '확정'),
)

InOutDiv_Choices = (
    (11, '구매입고'),
    (21, '거래명세'),
    (22, '계산서'),
    (31, '기타출고'),
)#입출고구분

USpec1_Choices = (
    ('01', '대형매장용'),
    ('02', '가정용'),
    ('03', '유흥음식점용'),
    ('04', '기타'),
)#주종구분

USpec2_Choices = (
    ('01', '주정'),
    ('02', '탁주'),
    ('03', '약주'),
    ('04', '청주'),
    ('05', '맥주'),
    ('06', '과실주'),
    ('07', '증류식소주'),
    ('08', '희석식소주'),
    ('09', '위스키'),
    ('10', '브랜디'),
    ('11', '일반증류주'),
    ('12', '리큐르'),
    ('13', '기타추류'),
)#용도구분

InOutSubDiv_Choices = (
    (1101, '내수구매'),
    (2101, '정상판매'),
    (2102, '판매반품'),        
    (2201, '계산서'),
    (3101, '판촉사용'),
    (3102, '재고손실'),        
)#입출고구분

class Item(models.Model):    
    ItemSeq = models.AutoField(primary_key=True)
    ItemNo = models.CharField(max_length=100,verbose_name="품번")
    ItemName = models.CharField(max_length=100,verbose_name="품명")
    Spec = models.CharField(max_length=100,verbose_name="규격")
    USpec1 = models.CharField(max_length=100,blank=True, null=True,choices=USpec1_Choices,verbose_name="용도구분")
    USpec2 = models.CharField(max_length=100,blank=True, null=True,choices=USpec2_Choices,verbose_name="주종구분")
    Remark = models.CharField(max_length=100,verbose_name="비고")
    Uptdate = models.DateTimeField(blank=True, null=True,editable=False)

    def publish(self):
        self.Uptdate = timezone.now()
        self.save()

    def __str__(self):
        return "%s %s %s" %(self.ItemName,self.Spec,self.USpec1)

    class Meta:
        db_table = "titem"
        verbose_name="품목"
        verbose_name_plural = "품목"

class Cust(models.Model):    
    CustSeq = models.AutoField(primary_key=True)
    CustNo = models.CharField(max_length=100,verbose_name="거래처번호")
    CustName = models.CharField(max_length=100,verbose_name="거래처명")
    Remark = models.CharField(max_length=100,blank=True,null=True,verbose_name="비고")
    BizNo = models.CharField(max_length=30,blank=True,null=True,verbose_name="사업자번호")
    Addr = models.CharField(max_length=100,blank=True,null=True,verbose_name="주소")
    Tel1 = models.CharField(max_length=30,blank=True,null=True,verbose_name="전화1")
    Tel2 = models.CharField(max_length=30,blank=True,null=True,verbose_name="전화2")
    TaxEmail = models.CharField(max_length=100,blank=True,null=True,verbose_name="전자세금계산서 emaiil")
    TaxEmpName = models.CharField(max_length=50,blank=True,null=True,verbose_name="전자세금계산서 담당자")
    USpec1 = models.CharField(max_length=100,blank=True,null=True,verbose_name="사용자정의1")
    USpec2 = models.CharField(max_length=100,blank=True,null=True,verbose_name="사용자정의2")
    USpec3 = models.CharField(max_length=100,blank=True,null=True,verbose_name="사용자정의3")
    USpec4 = models.CharField(max_length=100,blank=True,null=True,verbose_name="사용자정의4")
    
    def __str__(self):
        return "%s %s" %(self.CustName,self.Remark)

    class Meta:
        db_table = "tcust"
        verbose_name="거래처"
        verbose_name_plural  = "거래처"

class InOutM(models.Model):    
    InOutSeq = models.AutoField(db_column="InOutSeq",primary_key=True)
    InOutDiv = models.IntegerField(choices=InOutDiv_Choices,verbose_name="입출고구분") #/*11:구매입고,21:거래명세,22:계산서,31:기타출고*/
    InOutNo = models.CharField(max_length=100,verbose_name="입출고번호")
    InOutDate = models.DateField(verbose_name="입출고일")
    InOutName = models.CharField(max_length=100,blank=True,null=True,verbose_name="입출고명")
    IsCfm = models.CharField(max_length=1,choices=IsCfm_Choices,verbose_name="확정여부")
    Remark = models.CharField(max_length=100,blank=True,null=True,verbose_name="비고")
    CustSeq = models.ForeignKey(Cust, db_column="CustSeq",verbose_name="거래처")
    EmpSeq = models.IntegerField(blank=True,null=True,verbose_name="사원코드")
    ExSeq = models.IntegerField(blank=True,null=True,verbose_name="통화")
    ExRatio = models.FloatField(blank=True,null=True,verbose_name="환율")
    USpec1 = models.CharField(max_length=100,blank=True,null=True,verbose_name="사용자정의1")
    USpec2 = models.CharField(max_length=100,blank=True,null=True,verbose_name="사용자정의2")
    USpec3 = models.CharField(max_length=100,blank=True,null=True,verbose_name="사용자정의3")
    USpec4 = models.CharField(max_length=100,blank=True,null=True,verbose_name="사용자정의4")

    def __str__(self):
        return "%s %s" %(self.InOutNo,self.InOutDate)

    class Meta:
        db_table = "tinoutm"
        verbose_name="입출고"
        verbose_name_plural = "입출고"

class InOutD(models.Model):     
    InOutDSeq = models.AutoField(primary_key=True,verbose_name="입출고DSeq")   
    InOutSeq = models.ForeignKey(InOutM, db_column="InOutSeq",verbose_name="입출고Seq")
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
        verbose_name="입출고품목"
        verbose_name_plural = "입출고품목"  
        unique_together = (("InOutSeq", "InOutSubSeq"),)      

class MCode(models.Model):    
    MCodeSeq = models.AutoField(primary_key=True)
    MCodeNo = models.CharField(max_length=10,primary_key=True,verbose_name="M코드번호")
    MCodeName = models.CharField(max_length=100,verbose_name="M코드명")
    Remark = models.CharField(max_length=100,verbose_name="비고")

    def __str__(self):
        return "%s %s" %(self.MCodeSeq,self.MCodeName)

    class Meta:
        db_table = "tmcode"
        verbose_name="M코드"
        verbose_name_plural = "M코드"        

class DCode(models.Model):    
    DCodeSeq = models.AutoField(primary_key=True)
    MCodeSeq = models.ForeignKey(MCode, db_column="MCodeSeq",verbose_name="M코드")
    DCodeName = models.CharField(max_length=100,verbose_name="D코드명")
    DCodeValue = models.CharField(max_length=100,verbose_name="D코드값")    
    Remark = models.CharField(max_length=100,blank=True,null=True,verbose_name="비고")

    def __str__(self):
        return "%s %s" %(self.DCodeSeq,self.DCodeName)

    class Meta:
        db_table = "tdcode"
        verbose_name="D코드"
        verbose_name_plural = "D코드"

class Emp(models.Model):    
    EmpSeq = models.AutoField(primary_key=True)
    EmpNo = models.CharField(max_length=10,verbose_name="사번")
    EmpName = models.CharField(max_length=100,verbose_name="사원명")
    Remark = models.CharField(max_length=100,blank=True,null=True,verbose_name="비고")

    def __str__(self):
        return "%s %s" %(self.EmpSeq,self.EmpName)

    class Meta:
        db_table = "temp"
        verbose_name="사원"
        verbose_name_plural = "사원"        

class Inventory(models.Model):    
    InventorySeq = models.IntegerField(primary_key=True)
    ItemSeq = models.ForeignKey(Item, db_column="ItemSeq",verbose_name="품목")
    InQty = models.FloatField(verbose_name="입고수량")
    OutQty = models.FloatField(verbose_name="출고수량")
    StockQty = models.FloatField(verbose_name="재고수량")

    def __str__(self):
        return "%s %s" %(self.ItemSeq,self.StockQty)

    class Meta:
        db_table = "vinventory"
        verbose_name="재고"
        verbose_name_plural = "재고"           


class InvoiceM(models.Model):    
    InOutSeq = models.AutoField(db_column="InOutSeq",primary_key=True)
    InOutDiv = models.IntegerField(default=21,editable=False, choices=InOutDiv_Choices,verbose_name="입출고구분") #/*11:구매입고,21:거래명세,22:계산서,31:기타출고*/
    InOutNo = models.CharField(max_length=100,verbose_name="거래명세번호")
    InOutDate = models.DateField(verbose_name="거래명세일")
    InOutName = models.CharField(max_length=100,blank=True,null=True,verbose_name="거래명")
    IsCfm = models.CharField(max_length=1,choices=IsCfm_Choices,verbose_name="확정여부")
    Remark = models.CharField(max_length=100,blank=True,null=True,verbose_name="비고")
    CustSeq = models.ForeignKey(Cust, db_column="CustSeq",verbose_name="거래처")
    EmpSeq = models.IntegerField(blank=True,null=True,verbose_name="사원코드")
    ExSeq = models.IntegerField(blank=True,null=True,verbose_name="통화")
    ExRatio = models.FloatField(blank=True,null=True,verbose_name="환율")
    USpec1 = models.CharField(max_length=100,blank=True,null=True,verbose_name="사용자정의1")
    USpec2 = models.CharField(max_length=100,blank=True,null=True,verbose_name="사용자정의2")
    USpec3 = models.CharField(max_length=100,blank=True,null=True,verbose_name="사용자정의3")
    USpec4 = models.CharField(max_length=100,blank=True,null=True,verbose_name="사용자정의4")

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
        verbose_name="거래명세품목"
        verbose_name_plural = "거래명세품목"  
        unique_together = (("InOutSeq", "InOutSubSeq"),)             
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.db.models import Sum
from QS.models import *
from QS.admin import *
from QS.forms import *

#거래명세서 출력
def Print_Invoice(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)   
    masters = InvoiceM.objects.filter(InOutSeq__in=selected)
    details = InvoiceD.objects.filter(InOutSeq__in=selected)
    sumvals = InvoiceD.objects.filter(InOutSeq__in=selected).values('InOutSeq').annotate(Sum('Amt'))
    return render(request, 'QS/print_invoice.html',{'masters':masters, 'details':details, 'sumvals':sumvals})
    # selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    # ct = ContentType.objects.get_for_model(queryset.model)
    # return HttpResponseRedirect("/print/invoice/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))

class AdminForm(forms.ModelForm):
    class Meta:
        model = BillM
        exclude = ['name']


def Jump_to_Bill(modeladmin, request, queryset):
    #ct = ContentType.objects.get_for_model(queryset.model)
    ct = queryset
    form = AdminForm
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)    
    return render(request, 'QS/bill_edit.html',{'selected': selected, 'ct':ct, 'form': form})
    # selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    # ct = ContentType.objects.get_for_model(queryset.model)
    # return HttpResponseRedirect("/bill/new/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))    

#거래명세
class InvoiceD_Inline(admin.TabularInline):
    model = InvoiceD
    fields = (
        'InOutSubSeq','ItemSeq','Qty','Price','Amt','Remark',
    )
@admin.register(InvoiceM)
class InvoiceAdmin(admin.ModelAdmin):
    actions = [make_Cfm,Cancel_Cfm,Print_Invoice,Jump_to_Bill]
    save_on_top = True
    ordering = ['InOutNo']
    list_filter = ['InOutDate']
    search_fields = ['InOutNo']
    list_display = ['InOutDiv','InOutNo','InOutDate','CustSeq','Remark','IsCfm']
    fields = (
        ('InOutNo'),
        ('InOutDate','IsCfm'),
        ('CustSeq','InOutName'),
        ('EmpSeq','Remark'),
    )
    inlines = [InvoiceD_Inline]

    def get_queryset(self, request):
        #qs = InvoiceM.objects.extra(select={'InOutNo':'InOutDiv'},join=['LEFT JOIN tInOutM.InOutSeq ON tInOutD.InOutSeq'])
        #qs = InvoiceM.objects.all().annotate(tInOutD__Amt=InvoiceD.Sum(Amt))
        qs = super(InvoiceAdmin, self).get_queryset(request)
        return qs.filter(InOutDiv=getChoicecode(InOutDiv_Code,"invoice"))
        #return InvoiceM.objects.raw('select InOutDiv, InOutNo, InOutDate, CustSeq, Remark, IsCfm, a.InOutSeq from tInOutM as a join tInOutD as b on a.InOutSeq = b.InOutSeq')
                                       #where a.InOutDiv=%',getChoicecode(InOutDiv_Code,"invoice"))

#계산서
class BillD_Inline(admin.TabularInline):model = BillD
@admin.register(BillM)
class BillAdmin(admin.ModelAdmin):
    actions = [make_Cfm,Cancel_Cfm,Print_Invoice]
    save_on_top = True
    ordering = ['InOutNo']
    list_filter = ['InOutDate']
    search_fields = ['InOutNo']
    list_display = ['InOutDiv','InOutNo','InOutDate','Remark','IsCfm']
    fields = (
        ('InOutNo'),
        ('InOutDate','IsCfm'),
        ('CustSeq','InOutName'),
        ('EmpSeq','Remark'),
        ('ExSeq','ExRatio'),
    )
    inlines = [BillD_Inline]

    #list 조회
    def get_queryset(self, request):
        qs = super(BillAdmin, self).get_queryset(request)
        return qs.filter(InOutDiv=getChoicecode(InOutDiv_Code,"bill"))

    #add view
    def add_view(self, request, form_url='QS/bill_edit.html', extra_context=None):
        return self.changeform_view(request, None, form_url, extra_context)

#수금
class CollectD_Inline(admin.TabularInline):model = CollectD
@admin.register(CollectM)
class CollectAdmin(admin.ModelAdmin):
    actions = [make_Cfm,Cancel_Cfm]
    save_on_top = True
    ordering = ['CollectNo']
    list_filter = ['CollectDate']
    search_fields = ['CollectNo']
    list_display = ['CollectDiv','CollectNo','CollectDate','Remark','IsCfm']
    fields = (
        ('CollectNo'),
        ('CollectDate','IsCfm'),
        ('CustSeq','CollectName'),
        ('EmpSeq','Remark'),
        ('ExSeq','ExRatio'),
    )
    inlines = [CollectD_Inline]



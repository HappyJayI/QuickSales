from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from QS.models import *
from QS.admin import *

def Jump_to_Bill(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    return render(request, 'QS/bill_edit.html',{'selected': selected})
    # selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    # ct = ContentType.objects.get_for_model(queryset.model)
    # return HttpResponseRedirect("/bill/new/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))

#거래명세        
class InvoiceD_Inline(admin.TabularInline):model = InvoiceD
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
        ('ExSeq','ExRatio'),
    )
    inlines = [InvoiceD_Inline]

    def get_queryset(self, request):
        qs = super(InvoiceAdmin, self).get_queryset(request)
        return qs.filter(InOutDiv=getChoicecode(InOutDiv_Code,"invoice"))

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

    def get_queryset(self, request):
        qs = super(BillAdmin, self).get_queryset(request)
        return qs.filter(InOutDiv=getChoicecode(InOutDiv_Code,"bill"))


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



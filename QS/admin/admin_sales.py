from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from QS.models import *
from QS.admin import *

class InvoiceD_Inline(admin.TabularInline):model = InvoiceD
@admin.register(InvoiceM)
class InvoiceAdmin(admin.ModelAdmin):
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
    inlines = [InvoiceD_Inline]

    def get_queryset(self, request):
        qs = super(InvoiceAdmin, self).get_queryset(request)
        return qs.filter(InOutDiv=getChoicecode(InOutDiv_Code,"invoice"))



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



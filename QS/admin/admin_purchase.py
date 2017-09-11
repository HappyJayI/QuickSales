from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from QS.models import *
from QS.admin import *

class PurchaseD_Inline(admin.TabularInline):model = PurchaseD
@admin.register(PurchaseM)
class PurchaseAdmin(admin.ModelAdmin):
    actions = [make_Cfm,Cancel_Cfm]
    save_on_top = True
    ordering = ['InOutNo']
    list_filter = ['InOutDate']
    search_fields = ['InOutNo']
    list_display_links = ['InOutNo']
    list_display = ['InOutDiv','InOutNo','InOutDate','Remark','IsCfm']
    fields = (
        ('InOutNo'),
        ('InOutDate','IsCfm'),
        ('CustSeq','InOutName'),
        ('EmpSeq','Remark'),
        ('ExSeq','ExRatio'),
    )
    inlines = [PurchaseD_Inline]

    def get_queryset(self, request):
        qs = super(PurchaseAdmin, self).get_queryset(request)
        return qs.filter(InOutDiv=getChoicecode(InOutDiv_Code,"purchase"))

    #Todo
    #영업채권
    #시스템코드(입출고)
    #사용자정의config
    #입출고  : 입고, 출고로 분리


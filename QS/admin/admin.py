from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from QS.models import *

#확정, 확정취소
def make_Cfm(modeladmin, request, queryset):
    queryset.update(IsCfm='1')
make_Cfm.short_description = "선택행 확정처리"

def Cancel_Cfm(modeladmin, request, queryset):
    queryset.update(IsCfm='')
Cancel_Cfm.short_description = "선택행 확정취소"

#admin.site.disable_action('delete_selected') #Making actions disable site-wide
#admin.site.add_action(make_Cfm) #sMaking actions available site-wide

def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response

#Admin
class ItemAdmin(admin.ModelAdmin):
    list_display = ['ItemName','ItemNo','Spec']
    search_fields = ['ItemName','ItemNo','Spec']

class CustAdmin(admin.ModelAdmin):
    list_display = ['CustName','CustNo','Remark']
    search_fields = ['CustName','CustNo']

class EmpAdmin(admin.ModelAdmin):
    list_display = ['EmpName','EmpNo','Remark']
    search_fields = ['EmpName','EmpNo']

class InventoryAdmin(admin.ModelAdmin):
    list_display = ['ItemSeq','InQty','OutQty','StockQty']
    search_fields = ['ItemSeq']

admin.site.register(Item,ItemAdmin)
admin.site.register(Cust,CustAdmin)
admin.site.register(Emp,EmpAdmin)
admin.site.register(Inventory,InventoryAdmin)

class DCode_Inline(admin.TabularInline):model = DCode
@admin.register(MCode)
class MCodeAdmin(admin.ModelAdmin):
    search_fields = ['MCodeName']
    list_display = ['MCodeName','MCodeNo','Remark']
    inlines = [DCode_Inline]

class InOutD_Inline(admin.TabularInline):model = InOutD
@admin.register(InOutM)
class InOutMAdmin(admin.ModelAdmin):
    actions = [make_Cfm,Cancel_Cfm]
    save_on_top = True
    ordering = ['InOutNo']
    list_filter = ['InOutDate']
    search_fields = ['InOutNo']
    list_display = ['InOutDiv','InOutNo','InOutDate','Remark','IsCfm']
    fields = (
        ('InOutDiv','InOutNo'),
        ('InOutDate','IsCfm'),
        ('CustSeq','InOutName'),
        ('EmpSeq','Remark'),
        ('ExSeq','ExRatio'),
        ('USpec1','USpec2')
    )
    inlines = [InOutD_Inline]


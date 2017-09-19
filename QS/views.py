from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import *
from .forms import *

def print_invoice(request):
    return render(request,'QS/print_invoice.html')

def bill_new(request):
     return render(request,'QS/bill_edit.html',{"bill":bills})    
    # if request.method == "POST":
    #     form = BillForm(request.POST)
    #     if form.is_valid():
    #         bill = form.save(commit=False)
    #         bill.save()
    #         return redirect('bill_detail', pk=bill.pk)
    # else:
    #     form = BillForm()
    # return render(request, 'QS/bill_edit.html', {'form': form})

def Item_list(request):
    items = Item.objects.all()
    return render(request,'QS/Item_list.html',{"items":items})

def Cust_list(request):
    custs = Cust.objects.all()
    return render(request,'QS/Cust_list.html',{"custs":custs})

def post_list(request):
    posts = InvoiceM.objects.all()
    return render(request, 'QS/post_list.html',{"posts":posts})

def post_detail(request,pk):
    post = get_object_or_404(InvoiceM, pk=pk)
    return render(request,'QS/post_detail.html',{'post':post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'QS/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(InvoiceM, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'QS/post_edit.html', {'form': form})


import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import TestForm


class HomeView(TemplateView):
    template_name = 'QS/home.html'

class AjaxTemplateMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)


class TestFormView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'QS/test_form.html'
    form_class = TestForm
    success_url = reverse_lazy('home')
    success_message = "Way to go!"
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from django.views.generic import TemplateView
from main_app import forms
from main_app import models


# Create your views here.

class IndexView(TemplateView):
    template_name = "main_app/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["illustration_list"] = models.IllustrationModel.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if context["illustration_list"]:
            return self.render_to_response(context)
        else:
            messages.warning(self.request, "Illustration is missing, please upload first")
            return redirect('upload_illustration')



class IllustrationView(TemplateView):
    template_name = "main_app/illustration.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_action"] = models.IllustrationModel._meta.get_field("tag").choices
        context["illustration_list"] = models.IllustrationModel.objects.all()
        return context


class IllustrationFilterView(TemplateView):
    template_name = "main_app/illustration.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = self.request.GET.get("q", None)
        title_filter = self.request.GET.get("title", None)
        context["filter_action"] = models.IllustrationModel._meta.get_field("tag").choices
        if filter:
            context["illustration_list"] = models.IllustrationModel.objects.filter(tag=filter)
        elif title_filter:
            context["illustration_list"] = models.IllustrationModel.objects.filter(title__icontains=title_filter)
        return context



class UploadIllustrationView(TemplateView):
    template_name = "main_app/upload_illustration.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = kwargs.get("form", None)
        if form:
            context["form"] = form
        else:
            context["form"] = forms.UploadIllustrationForm()
        return context

    def post(self, request):
        form = forms.UploadIllustrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("add illustration ok")
            messages.success(request, "Illustration added")
            return redirect("upload_illustration")
        messages.warning(request, "Fail to add illustration")
        return self.get(request, form=form)


class IllustrationDetailView(TemplateView):
    template_name = "main_app/illustration_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = kwargs.get("pk")
        context["illustration"] = models.IllustrationModel.objects.get(id=id)
        return context


class TextView(TemplateView):
    template_name = "main_app/text.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_action"] = models.TextModel._meta.get_field("tag").choices

        context["text_list"] = models.TextModel.objects.all()

        return context


class TextFilterView(TemplateView):
    template_name = "main_app/text.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = self.request.GET.get("q", None)
        title_filter = self.request.GET.get("title", None)
        context["filter_action"] = models.TextModel._meta.get_field("tag").choices
        if filter:
            context["text_list"] = models.TextModel.objects.filter(tag=filter)
        elif title_filter:
            context["text_list"] = models.TextModel.objects.filter(title__icontains=title_filter)

        return context



class TextDetailView(TemplateView):
    template_name = "main_app/text_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = kwargs.get("pk")
        context["text"] = models.TextModel.objects.get(id=id)
        return context


class UploadTextView(TemplateView):
    template_name = "main_app/upload_text.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = kwargs.get("form", None)
        if form:
            context["form"] = form
        else:
            context["form"] = forms.UploadTextForm()
        return context

    def post(self, request):
        form = forms.UploadTextForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("add text ok")
            messages.success(request, "Text added")
            return redirect("upload_text")
        messages.warning(request, "Fail to add text")
        return self.get(request, form=form)


class AddCountView(View):
    def post(self, request):
        obj_id = request.POST.get("obj_id", None)
        obj_type = request.POST.get("obj_type", None)
        btn_type = request.POST.get("btn_type", None)

        obj = self.get_model(obj_type, obj_id)
        if obj:
            if btn_type == "human":
                obj.human += 1
            elif btn_type == "ai":
                obj.ai += 1

            obj.save()

            return JsonResponse({"code": 200, "msg": "success"})
        return JsonResponse({"code": 400, "msg": "fail"})

    def get_model(self, obj_type, obj_id):
        if obj_type == "text":
            obj, is_create = models.TextCommentModel.objects.get_or_create(text_id=obj_id)
            return obj
        elif obj_type == "illustration":
            obj, is_create = models.IllustrationCommentModel.objects.get_or_create(illustration_id=obj_id)
            return obj
        else:
            return None

from django.contrib import admin
from django import forms
from django.shortcuts import redirect, render
from .models import Quote
from .message_processing import process_message
import json
from django.urls import include, path
# Register your models here.

class JSONImportForm(forms.Form):
    json_file = forms.FileField()

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote_text', 'person')
    change_list_template = "admin/quotes_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls =  [path('import-json/', self.import_json)]
        return my_urls + urls

    def import_json(self, request):
        if request.method == "POST":
            json_file = request.FILES["json_file"]
            raw_data = json.load(json_file)
            for message in raw_data["messages"]:
                process_message(message)
            print(raw_data["participants"])
            self.message_user(request, "Your json file has been imported")
            return redirect("..")
        form = JSONImportForm()
        payload = {"form": form}
        return render(
            request, "admin/json_form.html", payload
        )

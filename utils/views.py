from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin

from django.db.models import Q
# Create your views here.

class PartialTemplateMixin:
    '''
    '''
    def get_partial_template(self):
        partial_template_name =  "htmx_partial/" + self.template_name
        return partial_template_name
    
    def get_partial_list_template(self):
        partial_list_template = "htmx_partial/" + self.template_dir + "table_content.html"
        return partial_list_template

    
    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            if (self.request.GET.get("search") or self.request.GET.get("q")):
                return [self.get_partial_list_template()]
            return [self.get_partial_template()]
        return self.template_name
    

class SearchMixin(SuccessMessageMixin):
    search_lookup_fields = []
    success_message = "Successfully saved."

    def get_queryset(self, *args, **kwargs):
        qc = super().get_queryset(*args, **kwargs)
        qc = self.search(qc)
        return qc


    def search(self, qc):
        if self.request.GET.get("q"):
            query = self.request.GET.get("q")
            q_lookup = Q()
            for field in self.search_lookup_fields:
                q_lookup |= Q(**{field + "__icontains": query})
            return qc.filter(q_lookup)
        return qc
    

class DeleteMixin:
    def remove_from_DB(self, request):
        try:
            object_id = request.GET.get("pk", None)
            object = self.model.objects.filter(id=object_id)
            if object:
                object.delete()
                return True
        except Exception as e:
            print(e)
            return str(e)

    def get(self, request):
        status = self.remove_from_DB(request)
        return JsonResponse({"deleted": status})
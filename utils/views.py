from collections import defaultdict
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin

from django.db.models import Q

from meta.forms import MetaDataForm
from meta.models import MetaData
from utils.utils import remove_trailing_comma
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
    model = None

    def get_queryset(self, *args, **kwargs):
        qc = super().get_queryset(*args, **kwargs)
        qc = self.search(qc)
        return qc


    def search(self, qc):
        q_lookup = Q()

        if self.request.GET.get("q"):
            query = self.request.GET.get("q")
            for field in self.search_lookup_fields:
                q_lookup |= Q(**{field + "__icontains": query})

            # if hasattr(self.model,"meta_data"):
            #     q_lookup |= Q(meta_data__value__icontains=query)

        if self.request.GET.get("meta_ids"):
            meta_ids_str = self.request.GET.get("meta_ids")
            if meta_ids_str.endswith(","):
                meta_ids_str = meta_ids_str[:-1] 

            print("meta_ids_str",meta_ids_str)
            if meta_ids_str:
                ids = [int(id) for id in (meta_ids_str.split(","))]
                if ids:
                    for id in ids:
                        qc = qc.filter(meta_data=id)
                    return qc

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
    

class MetadataContextMixin:
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["metadata_form"] = MetaDataForm()
        return context
     
    
class MetaDataFilterMixin:
    def get_context_data(self, **kwargs):
        related_name = self.model._meta.get_field("meta_data").remote_field.related_name
        context = super().get_context_data(**kwargs)
        qs = (
            MetaData.objects
            .filter(**{f"{related_name}__isnull":False})  
            .values("id", "value", "key", "course_metas__id") 
            .order_by("course_metas__id", "key")
        )
        grouped = defaultdict(list)
        for md in qs:
            option = {
                "id": md["id"],
                "value": md["value"],
            }
            if option not in grouped[md["key"]]:
                grouped[md["key"]].append(option)           
        context["dropdowns"] = dict(grouped)
        print(context["dropdowns"])
        try:
            meta_ids = remove_trailing_comma(self.request.GET.get("meta_ids"))
            context["selected_metas"] = [int(id) for id in (meta_ids.split(","))]
        except Exception as e:
            print("Except........",str(e))
            pass
        return context
    

class PrefetchMixin:
    def get_object(self, *args,**kwargs):
        pk = self.kwargs.get("pk")
        return self.model.objects.prefetch_related("meta_data").get(id=pk)
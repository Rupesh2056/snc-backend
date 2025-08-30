from django.http import JsonResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView

from meta.forms import MetaDataForm
from meta.models import MetaData
from user.models import MetaData
from utils.permissions import AccessMixin
from utils.views import DeleteMixin, PartialTemplateMixin, SearchMixin


class MetaDataMixin(AccessMixin, SearchMixin, PartialTemplateMixin):
    form_class = MetaDataForm
    model = MetaData
    success_url = reverse_lazy("metadata_list")
    queryset = MetaData.objects.all()
    paginate_by = 10
    template_dir = "metadata/"


class MetaDataListView(MetaDataMixin, ListView):
    template_name = "metadata/list.html"
    search_lookup_fields = ["key", "value"]
    queryset = MetaData.objects.all()


class MetaDataDetailView(MetaDataMixin, DetailView):
    template_name = "metadata/metadata_detail.html"


class MetaDataCreateView(MetaDataMixin, CreateView):
    template_name = "create.html"


class MetaDataUpdateView(MetaDataMixin, UpdateView):
    template_name = "update.html"


class MetaDataDeleteView(MetaDataMixin, DeleteMixin, View): ...


class MetaDataCreateAJAXView(MetaDataMixin, CreateView):
    """
    Gets called from other create and update form and dynamically adds created metadata in the existing form`s dropdown.
    """

    def post(self, request, *args, **kwargs):
        form = MetaDataForm(request.POST)
        if form.is_valid():
            obj = form.save()

            return JsonResponse(
                {"status": True, "id": obj.id, "key": obj.key, "value": obj.value}
            )
        return JsonResponse({"status": False})

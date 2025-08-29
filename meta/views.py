from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView

from meta.forms import MetaDataForm
from meta.models import MetaData
from user.models import MetaData
from utils.views import DeleteMixin, PartialTemplateMixin, SearchMixin



class MetaDataMixin(SearchMixin,PartialTemplateMixin):
    form_class = MetaDataForm
    model = MetaData
    success_url = reverse_lazy("MetaData_list")
    queryset = MetaData.objects.all()
    paginate_by = 10
    template_dir="MetaData/"


class MetaDataListView(MetaDataMixin, ListView):
    template_name = "metadata/list.html"
    search_lookup_fields = ["title"]
    queryset = MetaData.objects.all()
    

class MetaDataDetailView(MetaDataMixin, DetailView):
    template_name = "metadata/metadata_detail.html"


class MetaDataCreateView(MetaDataMixin, CreateView):
    template_name = "create.html"

class MetaDataUpdateView(MetaDataMixin, UpdateView):
    template_name = "update.html"


class MetaDataDeleteView(MetaDataMixin,DeleteMixin, View):
    ...
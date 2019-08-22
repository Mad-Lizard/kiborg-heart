from recovery.models import Athlet
from django.views import generic
from django.utils import timezone

class AthletListView(generic.ListView):
    model = Athlet
    paginate_by = 5
    context_object_name = 'athlets'
    queryset = Athlet.objects.filter(published_at__lte=timezone.now())

    class Meta:
        app_label = 'recovery'

class AthletDetailView(generic.DetailView):
    model = Athlet

    class Meta:
        app_label = 'recovery'

from .models import Repair

from django.views.generic import ListView


class RepairListView(ListView):
    model = Repair
    template_name = "repairs/repair_types.html"

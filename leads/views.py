from django.shortcuts import render

from .forms import LeadForm
from .models import Lead


# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {"lead": lead}
    return render(request, "leads/lead_detail.html", context)


def lead_create(request):
    form = LeadForm()
    context = {"form": form}
    return render(request, "leads/lead_create.html", context)

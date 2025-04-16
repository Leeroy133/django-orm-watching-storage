from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from datacenter.duration_calculation import get_duration

SECONDS_HOUR = 3600
SECONDS_MINUTE = 60

def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for current_visit in visits:
        duration = get_duration(current_visit)
        formatted_duration = format_duration(duration)
        non_closed_visits.append({
            'who_entered': current_visit.passcard.owner_name,
            'entered_at': current_visit.entered_at,
            'duration': formatted_duration,
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)


def format_duration(duration_visit):
    hours = duration_visit.total_seconds() // SECONDS_HOUR
    minutes = (duration_visit.total_seconds() % SECONDS_HOUR) // SECONDS_MINUTE
    seconds = duration_visit.total_seconds() % SECONDS_MINUTE
    return f"{int(hours)}:{int(minutes):02}:{int(seconds):02}"
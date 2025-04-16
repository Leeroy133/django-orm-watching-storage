from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datacenter.duration_calculation import get_duration


SECONDS_HOUR = 3600


def is_visit_strange(duration):
    return duration.total_seconds() > SECONDS_HOUR


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits_by_this_passcard = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits_by_this_passcard:
        entered_time = timezone.localtime(visit.entered_at)
        duration = get_duration(visit)
        is_strange = is_visit_strange(duration)
        this_passcard_visits.append({
            'entered_at': entered_time.strftime('%Y-%m-%d %H:%M:%S'),
            'duration': format(duration),
            'is_strange': is_strange
        })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

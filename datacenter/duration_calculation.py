from datacenter.models import Visit
from django.utils import timezone


def get_duration(visit):
    entered_time = timezone.localtime(visit.entered_at)
    if visit.leaved_at:
        leaved_time = timezone.localtime(visit.leaved_at)
    else:
        leaved_time = timezone.localtime(timezone.now())
    duration_visit = leaved_time - entered_time
    return duration_visit
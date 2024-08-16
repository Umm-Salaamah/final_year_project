# scanner/tasks.py

from celery import shared_task
from .models import ScanResult, ScheduledScan
from .utils.header_scanner import scan_headers
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

@shared_task
def perform_scheduled_scan(scan_id):
    scan = ScheduledScan.objects.get(id=scan_id)
    results = scan_headers(scan.url)
    ScanResult.objects.create(user=scan.user, url=scan.url, results=results)
    
    send_mail(
        'Scheduled Scan Results',
        f'Scan results for {scan.url}: {results}',
        settings.DEFAULT_FROM_EMAIL,
        [scan.user.email]
    )
    scan.next_run += timezone.timedelta(hours=scan.interval)
    scan.save()

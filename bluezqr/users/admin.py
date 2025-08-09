# admin.py
from django.contrib import admin
from django.utils import timezone
from datetime import timedelta
from .models import Student, Candidate
from django.utils.timezone import localtime

class DateRangeFilter(admin.SimpleListFilter):
    title = 'Created Date'
    parameter_name = 'created_at'

    def lookups(self, request, model_admin):
        return (
            ('today', 'Today'),
            ('this_week', 'This Week'),
            ('this_month', 'This Month'),
            ('this_year', 'This Year'),
        )

    def queryset(self, request, queryset):
        now = timezone.now()

        if self.value() == 'today':
            return queryset.filter(created_at__date=now.date())
        elif self.value() == 'this_week':
            start = now - timedelta(days=now.weekday())
            end = start + timedelta(days=6)
            return queryset.filter(created_at__date__range=[start.date(), end.date()])
        elif self.value() == 'this_month':
            return queryset.filter(created_at__year=now.year, created_at__month=now.month)
        elif self.value() == 'this_year':
            return queryset.filter(created_at__year=now.year)
        return queryset


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'mobile', 'degree', 'department', 'college_name', 'passout_year', 'percentage', 'created_at'
    )
    search_fields = ('name', 'mobile', 'college_name', 'degree', 'department')
    list_filter = ('passout_year', 'degree', 'department', 'city', DateRangeFilter)
    readonly_fields = ('created_at',)

    def formatted_created_at(self, obj):
        local_time = localtime(obj.created_at)  # Converts to TIME_ZONE (Asia/Kolkata)
        return local_time.strftime("%Y-%m-%d %I:%M:%S %p")
    formatted_created_at.short_description = 'Created At (IST)'

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'mobile', 'branch', 'degree', 'department', 'passout_year', 'experience_years', 'created_at'
    )
    search_fields = ('name', 'mobile', 'branch', 'degree', 'department')
    list_filter = ('passout_year', 'experience_years', 'branch', 'city', DateRangeFilter)
    readonly_fields = ('created_at',)


    def formatted_created_at(self, obj):
        local_time = localtime(obj.created_at)  # Converts to TIME_ZONE (Asia/Kolkata)
        return local_time.strftime("%Y-%m-%d %I:%M:%S %p")
    formatted_created_at.short_description = 'Created At (IST)'
from django.contrib import admin
from django.db.models.functions import ExtractYear
from django.utils.translation import gettext_lazy as _


class YearFilter(admin.SimpleListFilter):
    title = _("Year")
    parameter_name = "year"

    def lookups(self, request, model_admin):
        queryset = model_admin.get_queryset(request)
        years = {
            year
            for year in queryset.annotate(
                year=ExtractYear("create_date"),
            )
            .values_list("year", flat=True)
            .distinct()
        }
        values_list = [(year, str(year)) for year in years if year is not None]
        values_list.append(("Unknown", _("Unknown")))
        return values_list

    def queryset(self, _request, queryset):
        if self.value():
            if self.value() == "Unknown":
                return queryset.filter(create_date__isnull=True)
            else:
                return queryset.filter(create_date__year=self.value())

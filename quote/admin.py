from django.contrib import admin

from quote.models import Quote

class GlitchFilterList(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Source'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'source'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        sources = []
        for source in Quote.objects.order_by("source").values_list('source').distinct():
            count = Quote.objects.filter(source=source[0]).count()
            sources.append((source[0], "{}: ({})".format(source[0],count)))

        return sources

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == None:
            q = queryset.filter()
        else:
            q = queryset.filter(source=self.value())
        return q

class GlitchAdmin(admin.ModelAdmin):
    list_filter = ((GlitchFilterList),)
    search_fields = ['quote', 'source', 'body']

admin.site.register(Quote, GlitchAdmin)
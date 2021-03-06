from django.conf import settings
from django.views.generic import ArchiveIndexView

from cmsplugin_blog.models import Entry


class BlogArchiveIndexView(ArchiveIndexView):
    model = Entry
    queryset = Entry.objects.filter(is_published=True)
    date_field = 'pub_date'

    def get_paginate_by(self, queryset):
        return getattr(settings, 'BLOG_PAGINATED_BY', 10)

from django.views.generic import View
from django.views.generic.list import MultipleObjectMixin

from furl import furl

from filters import FieldListViewFilter

class FilterViewMixin(MultipleObjectMixin, View):
    """Add filtering context"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        fragment = furl(self.request.get_full_path())

        # Get list of args; should be a good proxy for filters
        non_page_args = []
        for arg in fragment.args:
            if arg != "page":
                non_page_args.append(arg)

        context["non_page_args"] = non_page_args

        # Start generating actual lists and paths for filters
        filter_list = []

        # for filter in self.filters:
        #     # filter_obj = PartRevisionFilter()
        #     objects, clear_filter_fragment = filter.filter_list(self.request)
        #     filter_list.append((filter.name, objects, clear_filter_fragment))

        for filter in self.filter_specs:
            clear_filter_url = filter.clear_filter_string(self)
            if isinstance(filter, FieldListViewFilter):
                choices = filter.choices(self)
                print("Title: {}".format(filter.title))
                choices_list = []
                for counter, choice in enumerate(choices):
                    print("Choice ({}): {}".format(counter, choice))
                    choices_list.append(choice)
                filter_list.append((filter.title, choices_list, clear_filter_url))

        context["filter_list"] = filter_list

        # Create "clear filter" paths
        new_fragment = fragment.copy()

        size = new_fragment.args.size()
        if size > 0 and not (
            size == 1 and new_fragment.args.has_key("page")
        ):  # Only offer "clear all" button if a non-page arg is present
            context["clear_filter_fragment"] = new_fragment.path

        return context
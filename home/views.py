from django.views.generic import TemplateView


class ContextTemplateView(TemplateView):
    extra_context = None

    def get_context_data(self, *args, **kwargs):
        context = super(ContextTemplateView, self).get_context_data(**kwargs)
        if self.extra_context:
            context.update(self.extra_context)
        return context

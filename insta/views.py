from django.views.generic import TemplateView

class helloWorld(TemplateView):
    template_name = 'frontpage.html'

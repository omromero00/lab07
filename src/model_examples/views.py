#from django.http import HttpResponse
from django.http import HttpResponse
from django.views.generic import View

from django.template.loader import get_template

from model_examples.utils import render_to_pdf


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            'invoice_id': 123,
            'customer_name': "Omar Romero",
            'amount': 1399.99,
            'today':"Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("123456789")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response ['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

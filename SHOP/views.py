from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from SHOP.models import Products, TradeMark, ModelType, GadgetType


class Main(TemplateView):
    template_name = "test.html"

    def get_context_data(self, **kwargs):
        context = super(Main, self).get_context_data(**kwargs)
        return context


class TradeMarkView(ListView):
    template_name = 'trade_mark.html'
    model = Products

    def get_queryset(self):
        trade_mark = get_object_or_404(TradeMark, id=self.kwargs['trade_mark_id'])
        queryset = self.model.objects.filter(trade_mark=trade_mark)
        return queryset


class TypeModelView(ListView):
    template_name = 'type_model.html'
    model = Products

    def get_queryset(self):
        model_type = get_object_or_404(ModelType, id=self.kwargs['model_type_id'])
        queryset = self.model.objects.filter(model_type=model_type)
        return queryset


class GadgetTypeView(ListView):
    template_name = 'gadget_type.html'
    model = Products

    def get_queryset(self):
        gadget_type = get_object_or_404(GadgetType, id=self.kwargs['gadget_type_id'])
        queryset = self.model.objects.filter(gadget_type=gadget_type)
        return queryset
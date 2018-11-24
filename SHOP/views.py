from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, FormView
from SHOP.models import Products, TradeMark, ModelType, GadgetType
from SHOP.forms import RegisterForm
from django.urls import reverse
from django.views import View
from django.conf import settings


class Main(TemplateView):
    template_name = "test.html"

    def get_context_data(self, **kwargs):
        context = super(Main, self).get_context_data(**kwargs)
        products = Products.objects.all().select_related().order_by('-price')[:15]
        context['products'] = products
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


class Register(FormView):
    template_name = 'auth/registration.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(Register, self).form_valid(form)


class CheckoutView(View):
    def post(self, request, *args, **kwargs):
        import stripe
        stripe.api_key = settings.STRIPE_SECRET_KEY
        product = Products.objects.get(id=kwargs['product_id'])
        stripe.Charge.create(
            amount=int(product.price_for_stripe),
            currency="usd",
            source=request.POST['stripeToken'],  # obtained with Stripe.js
            description=""
            )
        product.count -= 1
        product.save()
        return redirect(reverse('thank_you'))


class ThankYouView(TemplateView):
    template_name = 'thank_you.html'

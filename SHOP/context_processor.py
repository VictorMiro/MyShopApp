from SHOP.models import TradeMark, ModelType, GadgetType


def trade_marks(request):
    return {'trade_marks': TradeMark.objects.all()}


def model_type(request):
    return {'model_type': ModelType.objects.all()}


def gadget_type(request):
    return {'gadget_type': GadgetType.objects.all()}

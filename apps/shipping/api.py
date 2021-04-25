from django.http import JsonResponse
from . models import Shipping

def api_can_ship(request):
    json_response = {}

    shipping_code = request.GET.get('shipping_code', '')

    try:
        shipping = Shipping.objects.get(place=shipping_code)

        if shipping.can_ship():
            json_response = {'amount': shipping.value}
        else:
            json_response = {'amount': 0}

    except Exception:
        json_response = {'amount': 0}

    return JsonResponse(json_response)

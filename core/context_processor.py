from product import models as mx


def requisites(request):
    req_obj = mx.Requisites.objects.first()
    if not req_obj:
        return {"requisites": {}}
    return {
        "requisites": {
            k: v for k, v in req_obj.__dict__.items()
            if k in [f.name for f in mx.Requisites._meta.local_fields]
        }
    }

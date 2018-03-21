from product import models as mx


def requisites(request):
    return {
        "requisites": {
            k: v for k, v in mx.Requisites.objects.first().__dict__.items()
            if k in [f.name for f in mx.Requisites._meta.local_fields]
        }
    }

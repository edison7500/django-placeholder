import io
from django.views import generic
from django.http import HttpResponse
from .handles import generate_placeholder


class HexColorConverter(object):
    regex = r"\w{6}"

    def to_python(self, value):
        return value

    def to_url(self, value):
        return f"{value:>06}"


class PlaceHolderView(generic.View):
    def _handle_place_holder(self, request, *args, **kwargs):
        bg_color = kwargs.get("bg", "e2e2e2")
        fnt_color = kwargs.get("fnt", "c9c9c9")
        text = request.GET.get("text", "placeholder")
        img = generate_placeholder(bg_color, fnt_color, text=text)
        fp = io.BytesIO()
        img.save(fp, format="JPEG")
        return HttpResponse(content=fp.getvalue(), content_type="image/jpeg")

    def get(self, request, *args, **kwargs):
        return self._handle_place_holder(request, *args, **kwargs)

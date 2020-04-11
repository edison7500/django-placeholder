from django.views import generic
from .handles import generate_placeholder


class HexColorConverter(object):
    regex = "[0-9,e,f]{6}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return f"{value:>06}"


class PlaceHolderView(generic.View):
    def _handle_place_holder(self, request, *args, **kwargs):

        bg_color = kwargs.get("bg", "e2e2e2")
        fnt_color = kwargs.get("fnt", "d9d9d9")
        text = request.get("text", "placeholder")
        img = generate_placeholder(bg_color, fnt_color, text=text)
        return img

    def get(self, request, *args, **kwargs):
        return self._handle_place_holder(request, *args, **kwargs)

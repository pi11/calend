# -*- coding: utf-8 -*-
# Local replacement for the unavailable `djangohelpers.images.scale` helper
# (the original package was hosted on Bitbucket Mercurial, now gone).

import os

from PIL import Image


def scale(image_field, size):
    """Return the URL of a thumbnail for `image_field`, generating it on
    first access. `size` is a "WxH" string, e.g. "100x150"."""
    if not image_field:
        return ""

    width, height = (int(part) for part in size.split("x"))
    storage = image_field.storage
    base, ext = os.path.splitext(image_field.name)
    thumb_name = "%s_thumb_%sx%s%s" % (base, width, height, ext)

    if not storage.exists(thumb_name):
        with storage.open(image_field.name, "rb") as src:
            img = Image.open(src)
            img = img.convert("RGB") if img.mode not in ("RGB", "RGBA") else img
            img.thumbnail((width, height), Image.LANCZOS)
            from io import BytesIO
            from django.core.files.base import ContentFile

            buffer = BytesIO()
            img.save(buffer, format=img.format or "JPEG")
            storage.save(thumb_name, ContentFile(buffer.getvalue()))

    return storage.url(thumb_name)

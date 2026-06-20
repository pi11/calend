# -*- coding: utf-8 -*-
# Stand-in for the unavailable `django-baner` package (was hosted on
# Bitbucket Mercurial, now gone). Keeps `{% load banertag %}` and
# `{% get_baner zone %}` working in templates without raising errors.
# Currently renders nothing; wire it up to a real banner/zone model if
# the banner rotation feature needs to come back.

from django import template

register = template.Library()


class BanerNode(template.Node):
    def __init__(self, zone):
        self.zone = zone

    def render(self, context):
        return ""


@register.tag(name="get_baner")
def do_get_baner(parser, token):
    bits = token.split_contents()
    zone = bits[1] if len(bits) > 1 else ""
    return BanerNode(zone)

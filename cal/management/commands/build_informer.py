#-*- coding: utf-8 -*-

import os
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from PIL import Image, ImageFont, ImageDraw

from cal.models import Holiday, MONTHS_R

class Command(BaseCommand):
    """This command upadte Holidays dates    """
    help = """This command upadte Holidays dates"""
 
    def handle(self, *args, **options):
        img = Image.open(os.path.join(settings.BASE_DIR,
                                      "static/source_images/inf.png"))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(os.path.join(settings.BASE_DIR,
                                               "static/source_images/font.ttf"),
                                  14)
        font2 = ImageFont.truetype(os.path.join(settings.BASE_DIR,
                                                "static/source_images/font.ttf"),
                                   15)

        next_h = Holiday.objects.filter(next_date__gte=datetime.now()).order_by('next_date')[:3]
        base_y = 60
        last_date = False
        for h in next_h:
            next_date = h.next_date
            text = "%s %s %s:" % (h.next_date.day, MONTHS_R[h.next_date.month-1][1],
                                  h.next_date.year)
            if len(h.name) > 23:
                words = h.name.split(' ')
                texts = []
                t = ""
                for w in words:
                    if len(t) + len(w) > 23:
                        texts.append(t.strip())
                        t = ""
                    t = "%s %s" % (t, w)
                texts.append(t.strip())
                #print texts
                    
            else:
                texts = [h.name, ]

            if next_date == last_date:
                k = 0
                for t in texts:
                    if k == 0:
                        draw.text((10, base_y - 20 + k), "- %s" % t, (0,0,0),
                                  font=font)
                    else:
                        draw.text((10, base_y - 20 + k), "  %s" % t, (0,0,0),
                                  font=font)
                    k += 10
            else:
                draw.text((25, base_y), text, (255,0,0), font=font2)
                k = 0
                for t in texts:
                    if k == 0:
                        draw.text((10, base_y + 20 + k), "- %s" % t, (0,0,0),
                                  font=font)
                    else:
                        draw.text((10, base_y + 20 + k), "  %s" % t, (0,0,0),
                                  font=font)
                    k += 10

            if last_date == next_date:
                base_y += 20
            else:
                base_y += 50
            base_y += k
            last_date = next_date
        img.save(os.path.join(settings.BASE_DIR, 'media/informer.png'))

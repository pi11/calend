#-*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError

from cal.models import Holiday

class Command(BaseCommand):
    """This command upadte Holidays dates    """
    help = """This command upadte Holidays dates"""
 
    def handle(self, *args, **options):
        for h in Holiday.objects.filter(is_public=True):
            h.next_date = h.get_date()
            h.save()

        
                            

                        


                    

            






    


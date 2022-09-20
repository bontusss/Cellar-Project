from django.db import models

from governors.models import Governor

# Create your models here.
class State(models.Model):
    """This models describes all the information we store about states in Nigeria.
    [Name, Capital, governor, deputy governor, senators, Representatives, population, land size, demonym, language, postal code, iso3166-code, website, cordinates, nicknames, date created, map image, flag image, seal image]
    """

    name = models.CharField('name', max_length=100, help_text='Name of the state. Eg: Abia State')
    capital = models.CharField('capital', max_length=100, help_text='Capital of the state')
    governor = models.ForeignKey(Governor, help_text='Governor of the state')

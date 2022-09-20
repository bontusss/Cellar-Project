from django.db import models


class Governor(models.Model):
    """This model describes the informations we need to know about our governors."""

    first_name = models.CharField(
        "first name", max_length=100, help_text="Enter governors first name"
    )
    last_name = models.CharField(
        "last name", max_length=100, help_text="Enter governors last name"
    )
    other_names = models.CharField(
        "other_names", max_length=100, help_text="Enter governors other names", blank=True
    )
    address = models.CharField(
        "address", max_length=200, help_text="Known address of the governor.", blank=True
    )
    # party = models.CharField()
    # phone_number


    Assumed_office = models.DateTimeField()
    ended = models.DateTimeField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.first_name + self.last_name


# Third-party Libraries
from django.db import models

# Own Libraries
from apps.utils.model import Auditable


class City(Auditable):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(
        "Country",
        on_delete=models.PROTECT,
        related_name="city_set",
    )

    class Meta:
        db_table = "city"
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                    "country",
                ],
                name="unique city for country",
            )
        ]

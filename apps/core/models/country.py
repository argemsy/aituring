# Third-party Libraries
from django.db import models
from django.utils.text import slugify

# Own Libraries
from apps.utils.model import Auditable


class Country(Auditable):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=8)
    slug = models.SlugField(
        blank=True,
        null=True,
        max_length=255,
    )

    def save(
        self,
        *args,
        **kwargs,
    ) -> None:
        if not self.pk or not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        db_table = "country"
        constraints = [
            models.UniqueConstraint(fields=["name", "code"], name="unique country name")
        ]

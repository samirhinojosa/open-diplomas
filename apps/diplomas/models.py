from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from apps.core.models import TimeStampedAuthModel
from apps.core.utils import compress_image, thumbnail_image
from .helpers import issuer_image, issuer_image_thumb


class Issuer(TimeStampedAuthModel):
    """
    Issuer's information.
    Missing fields based on OpenBadge: type, publicKey, verification, revocationList
    Other fiels : location
    """
    name = models.CharField("Issuer", max_length=150, help_text="Issuer name")
    url = models.URLField("Website", max_length=250, blank=True, help_text="Issuer website")
    slug = models.SlugField("Slug", max_length=250, help_text="Issuer name on URL format")
    telephone = models.CharField("Telephone", max_length=50, blank=True,
                                    help_text="Issuer telephone")
    description = models.TextField("Description", max_length=500, blank=True,
                                    help_text="Enter a brief description about the Issuer")
    email = models.EmailField("Email", max_length=100, help_text="Issuer email")
    image = models.ImageField("Image", max_length=250, blank=True, upload_to=issuer_image,
                              help_text="Image of the issuer")
    image_thumb = models.ImageField("Thumbnail", max_length=250, blank=True,
                                    upload_to=issuer_image_thumb, help_text="Thumbnail of the post")

    class Meta:
        ordering = ["-created", "-name"]
        verbose_name = "Issuer"
        verbose_name_plural = "Issuers"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        if self.created:
            original = Issuer.objects.get(pk=self.pk)
            if original.image != self.image:
                self.image = compress_image(self.image)
                self.image_thumb = thumbnail_image(self.image)
        else:
            if self.image != "":
                self.image = compress_image(self.image)
                self.image_thumb = thumbnail_image(self.image)

        super(Issuer, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("admin:diplomas_issuer_change", args=[str(self.id)])
    
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# from PIL import Image


class Project(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="user_projects",
        related_query_name="user_project",
        on_delete=models.CASCADE,
    )
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    image = models.ImageField(
        _("Image"), upload_to="project_images", null=True, blank=True
    )
    link = models.URLField(_("Link"), max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Get url for project detail view.

        Returns:
            str: URL for project detail.

        """
        return reverse("projects:detail", kwargs={"pk": self.pk})

    # def save(self, *args, **kwargs):
    #     """
    #     This function resizes an image before saving it.
    #     """
    #     if self.image:
    #         img = Image.open(self.image.path)

    #         if img.height > 300 or img.width > 300:
    #             output_size = (300, 300)
    #             img.thumbnail(output_size)
    #             img.save(self.image.path)

    #     super().save(*args, **kwargs)

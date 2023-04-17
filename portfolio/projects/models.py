from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


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

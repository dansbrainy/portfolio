from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from PIL import Image


class User(AbstractUser):
    """
    Default custom user model for portfolio.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    name = CharField(_("Name of User"), blank=True, max_length=255)
    home_address = models.CharField(_("Home Address"), blank=True, max_length=255)
    phone_number = models.CharField(_("Phone Number"), blank=True, max_length=20)
    location = models.PointField(_("Location"), blank=True, null=True)
    profile_picture = models.ImageField(
        _("Profile Picture"),
        upload_to="profile_pics/",
        blank=True,
        null=True,
        default="default.jpg",
    )
    bio = models.TextField(_("About Me"), blank=True, max_length=1000)
    profession = models.CharField(_("Profession"), blank=True, max_length=40)
    projects = models.ManyToManyField(
        "projects.Project", blank=True, related_name="projects"
    )

    def save(self, *args, **kwargs):
        """
        This function resizes a profile picture before saving it.
        """
        """Override the save method to resize the profile picture before saving it"""
        super().save(*args, **kwargs)

        if self.profile_picture:
            img = Image.open(self.profile_picture.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

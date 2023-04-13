from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.gis.geos import Point
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, View

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = [
        "name",
        "home_address",
        "phone_number",
        "location",
        "profile_picture",
        "bio",
    ]
    success_message = _("Information successfully updated")

    def form_valid(self, form):
        # Set the location field based on the home address field
        address = form.cleaned_data.get("home_address")
        if address:
            # Use a geocoding service to get the latitude and longitude of the address
            # and create a Point object with the coordinates
            # For example, using geopy:
            from geopy.geocoders import Nominatim

            geolocator = Nominatim(user_agent="portfolio")
            location = geolocator.geocode(address)
            if location:
                point = Point(location.longitude, location.latitude)
                form.instance.location = point

        return super().form_valid(form)

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class SendEmailView(View):
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        send_mail(subject, name, message, email, [email])
        return HttpResponseRedirect(
            reverse("users:detail", args=[request.user.username])
        )


send_email_view = SendEmailView.as_view()

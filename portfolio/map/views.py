from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView

from portfolio.users.models import User

# from map.models import UserLocation


class MapView(LoginRequiredMixin, TemplateView):
    template_name = "map/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_locations = User.objects.all()
        user_data = []
        if user_locations:
            for user_location in user_locations:
                # create a Point object from the PostGIS geometry
                point = user_location.location
                lat = point.y
                lng = point.x
                user_data.append(
                    {
                        "name": user_location.username,
                        "lat": lat,
                        "lng": lng,
                        "url": reverse("users:detail", args=[user_location.pk]),
                    }
                )
        context["user_data"] = user_data
        return context


map_view = MapView.as_view()

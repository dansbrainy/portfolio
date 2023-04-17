from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from mypy import api
from PIL import Image
from pytest import mark

from portfolio.projects.models import Project
from portfolio.users.models import User, UserProject


@mark.django_db
class TestUserModel:
    def test_get_absolute_url(self, user: User):
        url = user.get_absolute_url()
        assert url == reverse("users:detail", kwargs={"username": user.username})

    def test_save_profile_picture(self, user: User):
        # create a dummy image file
        image_file = BytesIO()
        image = Image.new("RGBA", size=(50, 50), color=(155, 0, 0))
        image.save(image_file, "png")
        image_file.name = "test.png"
        image_file.seek(0)

        # upload the image to the user's profile
        user.profile_picture = SimpleUploadedFile(
            image_file.name, image_file.read(), content_type="image/png"
        )
        user.save()

        # check if the image was resized
        img = Image.open(user.profile_picture.path)
        assert img.size == (300, 300)

    def test_user_get_absolute_url(self, user: User):
        assert user.get_absolute_url() == f"/users/{user.username}/"

    def test_mypy(self) -> None:
        result = api.run(["users"])
        assert not result[2]


@mark.django_db
class TestUserProjectModel:
    def test_user_project_unique_together(self, user: User, project: Project):
        user_project1 = UserProject(user=user, project=project)
        user_project1.save()

        # creating a second user project with the same user and project should raise IntegrityError
        user_project2 = UserProject(user=user, project=project)
        try:
            user_project2.save()
        except Exception as e:
            assert type(e).__name__ == "IntegrityError"

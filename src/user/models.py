from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    """
    Custom user model.

    This class extends the default AbstractUser provided by Django to customize user behavior and attributes.

    Attributes:
        USERNAME_FIELD (str): The field used for user authentication, set to "username".
        mobile_no (CharField): Field for storing the user's mobile number.

    Methods:
        __str__(): Returns the string representation of the user (username).
        get_full_name(): Returns the full name of the user, composed of first name and last name if available, otherwise username.
        delete(): Overrides the delete method to prevent deletion of staff users.

    Meta:
        managed (bool): Indicates whether the model's table is managed by Django's migrations. Takes the value from settings.MANAGE_DATABASE.
        db_table (str): The name of the database table for the model, set to "user".
        verbose_name_plural (str): The plural name for the model used in the Django admin, set to "Users".
        default_permissions (list): List of default permissions for the model, only included if settings.DEFAULT_PERMISSIONS is False.

    Note:
        This class is intended to be used as a custom user model in Django projects.
    """

    USERNAME_FIELD = "username"

    mobile_no = CharField(unique=True, max_length=100, null=True, blank=True)

    def __str__(self):
        """
        Return the string representation of the user.

        Returns:
            str: The username of the user.
        """
        return self.username

    def get_full_name(self):
        """
        Return the full name of the user.

        If the user has both first name and last name specified, it returns the concatenation
        of the first name and last name separated by a space. If either the first name or last name
        is not specified, it returns the username.

        Returns:
            str: The full name of the user.
        """
        return (
            self.username
            if not self.first_name and not self.last_name
            else f"{self.first_name} {self.last_name}"
        )

    def delete(self, *args, **kwargs):
        """
        Override the delete method to prevent deletion of staff users.

        This method checks if the user is a staff member. If the user is a staff member,
        it sets the is_staff attribute to False and saves the user instance, effectively
        removing staff privileges without deleting the user from the database.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        if self.is_staff:
            self.is_staff = False
            self.save()

    class Meta:
        """
        Metadata options for the User model.

        This class contains metadata options for the User model, specifying various settings
        such as database table name, verbose name plural, managed status, and default permissions.

        Attributes:
            managed (bool): Indicates whether the model's table is managed by Django's migrations.
            db_table (str): The name of the database table for the model.
            verbose_name_plural (str): The plural name for the model used in the Django admin.
            default_permissions (list): List of default permissions for the model.

        Note:
            These options define the behavior and characteristics of the User model.
        """

        managed = settings.MANAGE_DATABASE
        db_table = "user"
        verbose_name_plural = "Users"
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []

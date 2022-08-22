from django.contrib.auth.decorators import user_passes_test
from rest_framework.exceptions import PermissionDenied


def permission_required(func, perm, login_url=None, raise_exception=False):
    """
    Decorator for views that checks whether a user has a particular permission
    enabled, redirecting to the log-in page if necessary.
    If the raise_exception parameter is given the PermissionDenied exception
    is raised.
    """
    print(func)

    def check_perms(user, request):
        print(type(user), request, "********************")
        # First check if the user has the permission (even anon users)
        if user.object.get('role')[0] == perm:
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False

    return user_passes_test(check_perms, login_url=login_url)

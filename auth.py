from kink import inject


@inject
class Auth:
    # The parent class initializing this class does not need to explicitly
    # pass in the "http" parameter. This is done automatically by kink library's @inject decorator.
    # The parameter name simply has to match the name used during dependency injection container setup.
    def __init__(self, default_auth_url: str, http):
        self.http = http
        self.auth_url = default_auth_url

    def authenticate(self, auth_url: str = None):
        result = self.http.get(auth_url or self.auth_url)
        return result["authenticated"]
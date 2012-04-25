import jwt, time

class LFAuthToken(object):
    """Class to create tokens for auth with Livefyre services."""
    def __init__(self, user, domain, key, display_name=None, duration=86400):
        self.domain = domain
        self.duration = duration
        self.key = key
        self.user = user
        self.display_name = display_name
    
    def __str__(self):
        """Return the generated token string."""
        return self.token
    
    @property
    def token(self):
        """Create a signed token from inputs."""
        token = dict(expires=self.duration + time.time(),
                     user_id=self.user,
                     domain=self.domain)
        if self.display_name:
            token['display_name'] = self.display_name
        return jwt.encode(token, self.key)
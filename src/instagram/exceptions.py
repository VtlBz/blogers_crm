from instaloader.exceptions import (
    BadCredentialsException,
    BadResponseException,
    ConnectionException,
    InvalidArgumentException,
    TwoFactorAuthRequiredException,
)


class InstaloaderLoginException(
    ConnectionException,
    InvalidArgumentException,
    BadCredentialsException,
    TwoFactorAuthRequiredException,
    BadResponseException,
):
    pass

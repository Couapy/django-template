ACCOUNTS_PROVIDERS = [
    {
        "provider": "google-oauth2",
        "name": "Google",
        "link": None,
        "username": None,
    },
    {
        "provider": "github",
        "name": "Github",
        "link": "https://github.com/{{ data.login }}",
        "username": "{{ data.login }}",
    },
    {
        "provider": "twitter",
        "name": "Twitter",
        "link": "https://twitter.com/{{ data.access_token.screen_name }}/",
        "username": "@{{ data.access_token.screen_name }}",
    },
    {
        "provider": "facebook",
        "name": "Facebook",
        "link": None,
        "username": None,
    },
]


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "78057430349-snmfbg6n2pn65c10mi77a9tie5hjbbfb.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "098ln2BZf9ZHjT1gkjTm5say"
SOCIAL_AUTH_GITHUB_KEY = ""
SOCIAL_AUTH_GITHUB_SECRET = ""
SOCIAL_AUTH_TWITTER_KEY = ""
SOCIAL_AUTH_TWITTER_SECRET = ""
SOCIAL_AUTH_FACEBOOK_KEY = ""
SOCIAL_AUTH_FACEBOOK_SECRET = ""

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/account/profile/'
LOGOUT_REDIRECT_URL = '/'
SOCIAL_AUTH_URL_NAMESPACE = 'social'
AUTH_PROFILE_MODULE = 'account.Profile'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = LOGIN_REDIRECT_URL
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = LOGIN_REDIRECT_URL
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'

"""
Django AllAuth package related settings
"""

LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/'

# Additional configuration settings
# ACCOUNT_LOGOUT_ON_GET= True
SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_STORE_TOKENS = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True

SSOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
            'https://www.googleapis.com/auth/youtube',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
            'redirect_uri': 'http://example.com:8000/accounts/google/login/callback/',
        }
    }
}

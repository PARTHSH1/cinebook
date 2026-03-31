# In MIDDLEWARE, add after SecurityMiddleware:
'whitenoise.middleware.WhiteNoiseMiddleware',

# Update ALLOWED_HOSTS
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',')

# Add static files config
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'
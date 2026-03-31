# In MIDDLEWARE, add after SecurityMiddleware:
'whitenoise.middleware.WhiteNoiseMiddleware',

# Update ALLOWED_HOSTS
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',')

# Add static files config
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Media files — disable on Render free tier (no persistent disk)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Only serve media in development
if DEBUG:
    from django.conf.urls.static import static

# Local
from .base import *

DEBUG = True
SESSION_COOKIE_SECURE = False
ALLOWED_HOSTS = [
    'localhost',
]
INTERNAL_IPS = [
    '127.0.0.1',
]

# Debug Toolbar
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE
MIDDLEWARE += [
    'querycount.middleware.QueryCountMiddleware',
]

# Cloudinary
CLOUDINARY_PREFIX = 'wapa-dev'
CLOUDINARY_STORAGE = {
    'PREFIX': CLOUDINARY_PREFIX,
}

# Async settings
RQ_QUEUES['default']['ASYNC'] = False

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

INSTALLED_APPS += [
    'debug_toolbar',
    'whitenoise.runserver_nostatic',
]

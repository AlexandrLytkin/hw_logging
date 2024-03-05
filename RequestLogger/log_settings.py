LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'success': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'success_responses.log',
            'encoding': 'utf-8',
        },
        'bad': {
            'level': 'WARNING',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'bad_responses.log',
            'encoding': 'utf-8',
        },
        'blocked': {
            'level': 'ERROR',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'blocked_responses.log',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'RequestsLogger': {
            'handlers': ['success'],
            'level': 'DEBUG',
        },
        'bad_responses': {
            'handlers': ['bad'],
            'level': 'DEBUG',
        },
        'blocked_responses': {
            'handlers': ['blocked'],
            'level': 'DEBUG',
        }
    }
}

import requests as rq
import logging.config
import logging

from RequestLogger.log_settings import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)

log = logging.getLogger('RequestsLogger')
log_bad = logging.getLogger('bad_responses')
log_blocked = logging.getLogger('blocked_responses')

sites = [
    'https://www.youtube.com/',
    'https://instagram.com',
    'https://wikipedia.org', 'https://yahoo.com', 'https://yandex.ru', 'https://whatsapp.com',
    'https://twitter.com',
    'https://amazon.com', 'https://tiktok.com', 'https://www.ozon.ru'
]

for site in sites:
    try:
        print(f'Пробуем сайт {site}')
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            log.info(f'{site}, response - {response.status_code}')
        if response.status_code == 503 or response.status_code == 403:
            log_bad.warning(f'{site}, response - {response.status_code}')

    except rq.exceptions.ConnectTimeout as exc:
        log_blocked.error(f'{site}, NO CONNECTION')
        print(f'Exception - rq.exceptions.ConnectTimeout: {exc}')

    except rq.exceptions.ConnectionError as er:
        log_blocked.error(f'{site}, NO CONNECTION')
        print(f'Exception - rq.exceptions.ConnectionError: {er}')


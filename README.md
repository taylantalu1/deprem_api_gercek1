# Deprem API

Bu küçük Flask uygulaması, Kandilli Rasathanesi'nden alınan en son depremleri JSON formatında bir API ile sunar.

## Endpoint

- `/` : API bilgilendirmesi
- `/api/deprem` : En son depremleri JSON olarak döner

## Kurulum (Render için)

1. Bu klasörü GitHub'a yükle
2. Render.com'da yeni bir web service oluştur
3. Environment: Python 3
4. Start command: `gunicorn app:app`

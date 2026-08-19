# password_services

Wiederverwendbare Python-Klasse fuer Passwort-Hashing und Terminal-Authentifizierung.

## Was macht es?

`PasswordService` bietet drei Funktionen:

- **Passwort hashen** — SHA-256 mit zufaelligem Salt (uuid4), gibt `hash:salt` zurueck
- **Passwort pruefen** — Vergleicht Benutzereingabe gegen gespeicherten Hash
- **Terminal-Login** — Interaktive Passworteingabe (ohne Echo) mit exponentiell steigender Wartezeit bei Fehlversuchen (2s, 4s, 8s...)

## Verwendung

```python
from cl_password_services import PasswordService

ps = PasswordService()

# Neues Passwort setzen (interaktiv, doppelte Eingabe)
hashed = ps.get_new_password()

# Gegen gespeicherten Hash pruefen (interaktiv)
authorized = ps.authorize(hashed)  # True/False
```

## Herkunft

Erstellt Januar 2022 als eigenstaendige Utility-Klasse. Eine weiterentwickelte Version (mit `@staticmethod`, optionalem Salt-Parameter und `unhash_password`) ist in [mathenandik-python](https://github.com/elRicharde/mathenandik) integriert (`password_services.py`).

## Lizenz

GPL-3.0

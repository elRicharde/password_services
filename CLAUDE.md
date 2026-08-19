# password_services

Python-Utility-Klasse fuer Passwort-Hashing (SHA-256 + Salt) und Terminal-Authentifizierung.

## Dateien

- `cl_password_services.py` — Einzige Quelldatei, enthaelt `PasswordService`-Klasse

## Hinweise

- Archiv-Projekt (Januar 2022), keine aktive Entwicklung
- Eine weiterentwickelte Kopie existiert in mathenandik-python (`password_services.py`) — dort werden static methods und ein optionaler Salt-Parameter verwendet
- Nutzt SHA-256 mit uuid4-Salt — fuer Produktiveinsatz waere bcrypt/argon2 besser, aber das hier ist ein Lern-/Prototyp-Projekt

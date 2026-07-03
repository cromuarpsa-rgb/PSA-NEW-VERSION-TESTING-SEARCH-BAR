# PSA-SEARCH

Local PSA Search System for searching PSOC and PSIC workbook data.

## Run

1. Double-click `run.bat`.
2. Open `http://127.0.0.1:8000` in your browser.
3. Log in with your account credentials.

## Features

- Pure Python localhost app
- Login credentials
- PSA logo branding
- Sidebar navigation (search, sheets, admin, appearance)
- Auto-filter keyword search
- Search across workbook sheets
- QR code scanner — scan a code with your camera to fill the search box
- Dark mode toggle (remembers your preference)
- Developer info icon
- Login, logout, search, and error logs

### QR scanner notes

The scanner uses your browser's camera. It first tries the browser's built-in
QR detector (works fully offline in Chrome/Edge); if that's not available it
loads a small QR-decoding library from a CDN, which requires an internet
connection the first time. Camera access requires either `https://` or
`http://127.0.0.1` / `http://localhost` (which `run.bat` already uses).

## Developer

Claverson Romuar  
Registration Kit Operator (National ID)

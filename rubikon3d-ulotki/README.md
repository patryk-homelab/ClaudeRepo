# Rubikon3D – ulotki A6 (jednostronne)

| Plik | Do czego |
|---|---|
| `*-druk-spad3mm.pdf` | do drukarni: 111×154 mm (A6 105×148 + 3 mm spadu), TrimBox ustawiony |
| `*-podglad.png` | podgląd po przycięciu do A6 |

Zestaw do druku (2 × 500 szt.):
- **A-paczka** – wkładka do paczki: podziękowanie + kod `PACZKA10` (−10% od 50 zł, ważny do odwołania).
- **A-paczka-bardzo-dziekujemy** – to samo z nagłówkiem „Bardzo dziękujemy za zamówienie!” (do porównania, wybrać jedną).
- **D-pomysly** – uniwersalna: „Zepsuło się? Nie ma w sklepie? Wydrukujemy to.” + 4 kategorie.

`odrzucone/` – warianty B, B2, C (odrzucone, zostawione do wglądu).

QR → WhatsApp +48 609 692 311 z inną gotową wiadomością na każdej ulotce (widać, z której ulotki ktoś pisze).

Regeneracja: `python3 zrodla/gen.py && node zrodla/render.js <katalog_wyjściowy> [nazwy...] && python3 zrodla/fixboxes.py <katalog_wyjściowy>/*.pdf` (wymaga Playwright/Chromium). Teksty i kolory w `zrodla/gen.py`.
Fonty: Space Grotesk, Space Mono (SIL OFL). Logo wyciągnięte wektorowo z wizytówki v7.

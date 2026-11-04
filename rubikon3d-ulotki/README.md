# Rubikon3D – ulotki A6 (jednostronne)

| Plik | Do czego |
|---|---|
| `*-druk-spad3mm.pdf` | do drukarni: 111×154 mm (A6 105×148 + 3 mm spadu), TrimBox ustawiony |
| `*-podglad.png` | podgląd po przycięciu do A6 |

- **A-paczka** – wkładka do paczki: podziękowanie + kod `PACZKA10` (−10%).
- **B-uslugi** – ogólna, do zostawiania w punktach: 3 kroki + przykłady.
- **C-czesci** – haczyk „Zepsuło się? Nie wyrzucaj.”: części zamienne na wymiar.
- **B2-uslugi-czerwona** – treść B w układzie A (bez czarnej stopki).
- **D-pomysly** – uniwersalna w stylu C: „Nie ma w sklepie? Wydrukujemy to.” + 5 kategorii pomysłów.

QR → WhatsApp +48 609 692 311 z inną gotową wiadomością na każdej ulotce (widać, z której ulotki ktoś pisze).

Regeneracja: `python3 zrodla/gen.py && node zrodla/render.js <katalog_wyjściowy> [nazwy...] && python3 zrodla/fixboxes.py <katalog_wyjściowy>/*.pdf` (wymaga Playwright/Chromium). Teksty i kolory w `zrodla/gen.py`.
Fonty: Space Grotesk, Space Mono (SIL OFL). Logo wyciągnięte wektorowo z wizytówki v7.

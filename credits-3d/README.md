# credits-3d — uchwyty na bity z Printables, sprawdzone skillem projekt-3d-druk

Data: 2026-11-04. Drukarka docelowa: Bambu Lab X2D, dysza 0,4, PETG. Licencje i teksty do ogłoszeń: `CREDITS.md`.

## Wynik w skrócie

| # | Model | Licencja | Co drukować | Stan po sprawdzeniu |
|---|---|---|---|---|
| 01 | [1770956 Bit holder, organizer](https://www.printables.com/model/1770956) — Jirka | CC0 | `oryginal/Bit_holder,_organizer.3mf` | OK bez zmian. 74 gniazda, luz 0,12 mm/stronę, 0 podpór |
| 02 | [1825701 Large bit holder](https://www.printables.com/model/1825701) — Jirka | CC0 | `poprawiony/Large_bit_holder_320_fixed.3mf` | Poprawiony: 16 gniazd w przednim rzędzie było za ciasnych (luz 0,01 mm), otwory na wkręty wymagały podpór. Po poprawce 320 gniazd, luz 0,15 mm, 0 podpór |
| 03 | [1051202 Ultimate Bit Holder](https://www.printables.com/model/1051202) — Carlos Gonzalez | CC BY | `poprawiony/3x7_…_repaired.3mf`, `poprawiony/8x4_…_repaired.3mf` + przegródki z `oryginal/` | Części 3x7 i 8x4 miały uszkodzone siatki, naprawione bez zmiany kształtu. To system na obrotową podstawę z magnesami (kupowane osobno) |
| 04 | [146076 Hex Bit Holder](https://www.printables.com/model/146076) — GUZ_prints | CC0 | `poprawiony/hex_bit_holder_v1_mounting_ears.3mf` | Poprawiony: brak otworów montażowych (skarga w komentarzu). Dodane 2 uszy z otworem Ø4,5 i stożkiem pod łeb. 144 rurki, luz 0,25 mm |

## Dane bitu (urządzenia)

| Wymiar | Wartość | Źródło | Status |
|---|---|---|---|
| Sześciokąt 1/4" — rozstaw płaskich s | 6,292–6,350 mm | ISO 1173:1975, tabela 3.1, forma C i E, wymiar nominalny 6,3 (podgląd normy iTeh) | norma |
| Rozstaw naroży e | 7,11–7,18 mm | j.w. | norma |
| Długość bitu | 25 mm (sprawdzane też 50/70/90 mm na kolizje) | typowy bit C6.3; nie sprawdzone w normie | założenie |
| Minimalny luz na stronę | 0,10 mm | brak `printer.json` z kalibracji X2D (niedostępny z tej sesji) | założenie |

## Metoda (dla każdego pliku)
- Audyt siatki (trimesh): zamknięta, liczba brył, objętość, wymiary, min z, grubość ścianek metodą promieni, nawisy >45°.
- Gniazda: przekroje prostopadłe do osi gniazda co 0,5–1 mm; tylko część prosta gniazda (przekroje identyczne co do pola ±0,1% i wymiarów ±0,01 mm).
- Przegląd tolerancji: siatka s × e = 4 × 3 kombinacji (s co 0,019 mm, e co 0,035 mm, oba końce zakresu normy), bit może się obrócić (szukanie najlepszego kąta co 0,5°).
- Wkładanie: bit 6,350/7,180 przesuwany wzdłuż osi gniazda z 40 mm nad modelem co 0,25 mm (manifold3d), pierwszy kontakt = osadzenie; kontrola kolizji bitów 50/70/90 mm.
- Testy kontrolne w każdym pliku: bit o 0,2 mm większy od gniazda musi zostać wykryty (2D), bit wciśnięty 1 mm za osadzenie musi dać kolizję (3D). Oba wykryte we wszystkich plikach.
- Slicer: PrusaSlicer 2.7.2 jako zastępca Bambu Studio (komenda ze skilla, stół 256×256), zliczanie `;TYPE:Support material`.
- Skrypty i surowe wyniki: `narzedzia/`.
- Podgląd 3D z bitami w gniazdach: `podglad-3d.html` (otwórz w przeglądarce, potrzebny internet do three.js) albo artefakt https://claude.ai/artifact/ExojbNBGfsdRknsn7V3KSo.

## Czego nie zrobiłem (i dlaczego)
1. Nie zapisałem na pulpit: ta sesja działa w chmurze i nie ma dostępu do Twojego komputera. Folder jest w repo, gałąź `claude/blissful-edison-wf7mwj`.
2. Łącznik build123d na MP i `printer.json`/`devices.json` były niedostępne, więc: brak porównania sum kontrolnych MP ↔ workspace, luz minimalny założony (0,10 mm/stronę), wersje bibliotek nieprzypięte (build123d 0.13.0, manifold3d 3.5.4, trimesh 5.2.0). Zamiast tego: ponowne uruchomienie skryptów poprawek daje identyczny STL (sha256), a 3MF różni się tylko losowymi UUID.
3. Poprawki zrobiłem jako operacje na oryginalnej siatce (manifold3d), a nie pełną przebudowę parametryczną w build123d. Dowód zakresu zmian: objętość dodana/usunięta podana w każdym raporcie.
4. Brak niezależnego drugiego odczytu wymiarów przez inny model (skill zapytaj-inne-ai wymaga MM).
5. Brak kodów produktów P0xx i wpisu do arkusza „Druk 3D – rejestr druku”.
6. Slicer to PrusaSlicer, nie Bambu Studio z profilem X2D; czasy druku z domyślnego profilu PrusaSlicera są nieprzydatne i ich nie podaję.

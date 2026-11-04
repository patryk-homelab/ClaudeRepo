# 03 — Ultimate Bit Holder (Printables 1051202)

- Autor: Carlos Gonzalez (`CarlosGonzal_2239591`), licencja **CC BY** (Creative Commons — Attribution), opublikowany 2024-11-03, brak modelu-rodzica.
- Printables (2026-11-04): 1458 polubień, 1294 pobrania, 1 wydruk, ocena 5,0 (1 ocena).
- To **system**, nie jedna część: elementy klejone (CA) na obrotową podstawę 9"/10" („lazy susan”), z magnesami sztabkowymi 60 × 10 mm i okrągłymi 6 × 3 mm — wszystko kupowane osobno (linki Amazon w opisie autora). Część uchwytów jest pod konkretne narzędzia: Amana (pogłębiacz), DeWalt (przystawka kątowa), wiertła do drewna, przedłużki.
- Przy sprzedaży obowiązuje podanie autora (CC BY) — tekst w `../CREDITS.md`.

## Części na bity sześciokątne — poprawione
Pliki: `poprawiony/3x7_hex_bit_holder_angled_repaired.3mf`, `poprawiony/8x4_hex_bit_holder_angled_repaired.3mf`. Skrypt: `poprawiony/repair.py`.

| | 3x7 (21 bitów) | 8x4 (32 bity) |
|---|---|---|
| Błąd oryginału (STL i 3MF to ta sama siatka) | 2 bryły: dodatkowa „śmieciowa” bryła o zerowej objętości (16 trójkątów) — dokładnie w miejscu, gdzie PrusaSlicer wstawiał podporę (42 bloki) | 11 brył: 4 rzędy + podstawa jako osobne bryły i 6 wewnętrznych płatów o zerowej grubości |
| Naprawa | usunięta śmieciowa bryła; kształt bez zmian (objętość 29158,7 mm³ przed i po) | 5 brył scalonych w jedną, płaty usunięte (objętość 67073,8 mm³ przed i po) |
| Siatka po naprawie | zamknięta, 1 bryła, 32 × 110,5 × 15,5 mm | zamknięta, 1 bryła, 80 × 84,5 × 16,1 mm |
| Gniazda | 21 × 6,706 / 7,744 mm, oś 45° | 32 × 6,80 / 7,852 mm, oś 45° |
| Przegląd tolerancji (12 kombinacji) | 0 kolizji, luz 0,177–0,178 mm/stronę | 0 kolizji, luz 0,225 mm/stronę |
| Wkładanie | 21/21 bez blokady | 32/32 bez blokady |
| Głębokość / wystaje bit 25 mm | 12,1–12,3 / 12,8–12,9 mm | 7,8–8,0 / 17,0–17,2 mm |
| Bity 50/70/90 mm | 0 kolizji | 0 kolizji |
| Slicer (PrusaSlicer) | 0 podpór (oryginał: 42) | 0 podpór |
| Uwaga | ostre krawędzie fazek (lokalnie <0,4 mm, łącznie 0,07 mm²) — kosmetyka | ścianki gniazd skierowane w dół dokładnie pod 45° (na granicy); slicer nie chce podpór |

## Pozostałe części — tylko audyt, bez zmian

| Plik | Siatka | Slicer (PrusaSlicer) | Uwagi |
|---|---|---|---|
| DIVIDER_1 … DIVIDER_8 (STL i 3MF) | OK, 1 bryła, ścianki ≥1,9 mm | 0 podpór | **drukować te pojedyncze pliki** |
| DIVIDERS_1-8 (STL i 3MF, zestaw na jednym stole) | uszkodzona: 20509 brył | 0 podpór | nie używać — drukować pojedyncze |
| DIVIDERS_AND_COIN_MAGNET_HOLDER | uszkodzona: 184 bryły | 0 podpór | nie używać |
| SELF-CENTERING_BIT_DIVIDER3_COIN_MAGNET | OK | 0 podpór | |
| SMALL_DIVIDER_2_ENLARGED / Divider_2_Slightly_Bigger | OK, lokalnie 0,23 mm (metoda promieni) | 0 podpór | |
| MAGNETIC_BIT_HOLDER / HEX_BIT_Extension_HOLDERs_v3 | 2 bryły (2 sztuki na stole), STL zaczyna się na z = −2,85 | 1 blok podpór (pierwsze warstwy) | slicer opuszcza na stół |
| BAR_MAGNET_FRAME_60X10.stl | OK | 0 podpór | wersja 3MF uszkodzona (800 brył) — brać STL |
| screw_head_labels_v2 | 6 brył (6 etykiet) | 0 podpór | |
| socket_extension_holder_v2 | 2 bryły | 0 podpór | |
| Amana_Countersunk_Screw_Bit_Holder | OK, lokalnie 0,095 mm (metoda promieni) | 12 bloków podpór | pod konkretny pogłębiacz Amana |
| RIGHT_ANGLE_ATTACHMENT_HOLDER / Dewalt_90_degree… | 2 bryły | 129 bloków podpór | pod przystawkę DeWalt |
| SINGLE_HOLDER_FOR_COIN_MAGNET / Bore_Bit_Holder | OK | 76 bloków podpór | |

Pasowania uchwytów pod konkretne narzędzia (Amana, DeWalt, wiertła do drewna, przedłużki, magnesy) **nie sprawdzałem** — brak zweryfikowanych wymiarów tych produktów.

## Ryzyka
1. Koszt i składanie: podstawa obrotowa + magnesy + klejenie. Sprzedaż jako komplet wymaga zakupu tych elementów. Uchwyty 3x7/8x4 mają płaskie dno, więc mogą też stać samodzielnie (bez podstawy nie testowane).
2. Grubości „lokalnie <0,4 mm” z metody promieni mogą być fałszywe przy pochyłych ściankach przy stole (sprawdzone w 04: tam to był błąd pomiaru). Przed sprzedażą części z tej tabeli zrób wydruk próbny.
3. Brak kalibracji X2D — luz 0,18–0,23 mm/stronę jest raczej bezpieczny, ale nie potwierdzony wydrukiem.

## Do zmierzenia suwmiarką na pierwszym wydruku
1. Rozstaw płaskich gniazda 3x7 (model 6,71 mm) i 8x4 (model 6,80 mm).
2. Szczelina na magnes w 8x4 (w przekroju ok. 60 mm długości) — czy magnes 60 × 10 mm wchodzi. Tej szczeliny nie sprawdzałem numerycznie.

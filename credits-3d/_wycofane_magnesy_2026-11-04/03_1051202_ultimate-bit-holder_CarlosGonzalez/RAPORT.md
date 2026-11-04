# 03 — Ultimate Bit Holder (Printables 1051202)

- Autor: Carlos Gonzalez (`CarlosGonzal_2239591`), licencja **CC BY** (Creative Commons — Attribution), opublikowany 2024-11-03, brak modelu-rodzica.
- Printables (2026-11-04): 1458 polubień, 1294 pobrania, 1 wydruk, ocena 5,0 (1 ocena).
- To **system**, nie jedna część: elementy klejone (CA) na obrotową podstawę 9"/10" („lazy susan”), z magnesami sztabkowymi 60 × 10 mm i okrągłymi 6 × 3 mm — wszystko kupowane osobno (linki Amazon w opisie autora). Część uchwytów jest pod konkretne narzędzia: Amana (pogłębiacz), DeWalt (przystawka kątowa), wiertła do drewna, przedłużki.
- Przy sprzedaży obowiązuje podanie autora (CC BY) — tekst w `../CREDITS.md`.

> **04.11.2026 wieczorem: wszystkie części na magnesy wycofane** (przeniesione do `../_wycofane_magnesy_2026-11-04/`, patrz `../README.md`). Zostały 3x7, 8x4, przegródki i etykiety. Opisy części magnetycznych niżej zostają jako zapis sprawdzeń.

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
2. Magnes 60 × 10 mm w nowej ramce (otwór 60,4 × 10,4 mm) i magnesy 6 mm w gniazdach (6,09–6,20 mm). Uwaga: w 8x4 nie ma szczeliny na magnes (sprawdzone przekrojami 04.11; wcześniejsza uwaga była błędna).

## Dopisane 04.11.2026 (ten sam poziom sprawdzeń co przy wkrętakach)
### Projekty Bambu (X2D, bez podpór) dla każdej części
- `poprawiony/`: 3x7 i 8x4 (naprawione), nowa ramka magnesu, `MAGNETIC_BIT_HOLDER_na_stole` — każdy z `*_X2D_PETG.3mf`.
- `projekt_X2D/`: części autora bez zmian kształtu: DIVIDER_1…8, SELF-CENTERING_BIT_DIVIDER3_COIN_MAGNET, SMALL_DIVIDER_2_ENLARGED_, screw_head_labels_v2, socket_extension_holder_v2, Amana_Countersunk_Screw_Bit_Holder, SINGLE_HOLDER_FOR_COIN_MAGNET, Dewalt_90_degree_adapter_holder_v3.
- Wszystkie siatki w projektach zamknięte, liczba trójkątów jak w plikach źródłowych.

### Bambu Studio 2.8.2 X2D, podpory auto (drzewiaste, próg 30°)
- **Żadna część nie potrzebuje podpór** w Bambu, także Amana i uchwyt na magnes (PrusaSlicer: 12 i 76 bloków) oraz oryginały 3x7 i 8x4.
- Dwie części autora miały złe ułożenie do druku, poprawione bez zmiany kształtu:
  1. `RIGHT_ANGLE_ATTACHMENT_HOLDER.stl` to 2 części ustawione jak po złożeniu (jedna 107 mm nad stołem): Bambu daje 340 fragmentów podpór, a z podporami tylko od stołu w ogóle nie tnie. Ten sam kształt jest w 3MF autora `Dewalt_90_degree_adapter_holder_v3.3mf` położony na stole: 0 podpór. Drukować ten.
  2. `MAGNETIC_BIT_HOLDER` (i `HEX_BIT_Extension_HOLDERs_v3.3mf`): jedna z 2 części wisi 1,5 mm nad stołem, Bambu stawia pod nią 7 fragmentów podpór. Nowy plik `poprawiony/MAGNETIC_BIT_HOLDER_na_stole.3mf`: obie części na stole (płaskie spody 800 i 900 mm²), 0 podpór.
- `socket_extension_holder_v2.stl` i `socket_extension_holder_with_small_magnet_frame_v2.3mf` to ta sama siatka (618 trójkątów, ta sama objętość); `Vertical_3x7_Hex_Bit_Holder_Angled.3mf` to ta sama siatka co 3x7 z tym samym błędem — zastępuje go naprawiony 3x7.

| Część | Filament | Czas |
|---|---|---|
| 3x7 naprawiony | 22,35 g | 1,11 h |
| 8x4 naprawiony | 36,90 g | 1,31 h |
| ramka magnesu (nowa) | 1,32 g | 0,06 h |
| MAGNETIC_BIT_HOLDER_na_stole | 6,88 g | 0,27 h |
| Dewalt 90° (2 części) | 11,57 g | 0,50 h |
| Amana | 3,92 g | 0,40 h |
| SINGLE_HOLDER_FOR_COIN_MAGNET | 2,25 g | 0,43 h |
| SELF-CENTERING…COIN_MAGNET | 7,49 g | 0,36 h |
| SMALL_DIVIDER_2_ENLARGED_ | 1,46 g | 0,23 h |
| DIVIDER_1 … DIVIDER_8 | 1,27 … 6,48 g | 0,19 … 0,29 h |
| screw_head_labels_v2 (6 szt.) | 3,74 g | 0,16 h |
| socket_extension_holder_v2 | 5,09 g | 0,31 h |

Wiersze 3x7 i 8x4 z ustawieniami projektu (model na środku stołu); reszta z krojenia z automatycznym rozmieszczeniem. Surowe wyniki: `../narzedzia/wyniki/bambu_studio_x2d_bity_wszystkie.tsv`.

### Magnesy (autor: „Bar Magnets (60x10mm)”, „Coin Magnets (6x3mm)”; linkowane oferty Amazon: 60 × 10 × 3 mm i 6 × 3 mm; dwa niezależne odczyty zgodne; status: osoby trzecie)
- `BAR_MAGNET_FRAME_60X10`: otwór **dokładnie 60,0 × 10,0 mm**, ramka 66 × 16 × 2,8 mm. Magnes 60 × 10 mm nie ma luzu, a otwory w druku FDM wychodzą mniejsze, więc magnes nie wejdzie bez piłowania. Nowa ramka `poprawiony/bar_magnet_frame_60x10_clearance_0.2.3mf`: ten sam obrys i wysokość, otwór 60,4 × 10,4 mm (0,2 mm na stronę). Zbudowana w build123d-mcp (`validate` PASS, `analyze_printability` 0 uwag), dwa eksporty identyczne; kod: `../narzedzia/build123d_ramka_magnesu/`. Magnes 3 mm wystaje 0,2 mm ponad ramkę 2,8 mm, jak u autora.
- Gniazda na magnesy 6 mm: SELF-CENTERING (6 szt.) Ø6,09 mm, dno 2,5 mm; SINGLE_HOLDER (2 szt.) Ø6,10 mm, głębokość ok. 3,5 mm; MAGNETIC_BIT_HOLDER (4 szt.) i socket_extension_holder (2 szt.) Ø6,18–6,20 mm. Luz 0,05–0,10 mm na stronę: magnes wchodzi na wcisk albo na klej; tego nie zmieniałem. Ryzyko: kupujący na Amazon zmierzyli te magnesy na ok. 1,7 mm grubości zamiast 3 mm (opinie, niesprawdzone) — wtedy siedzą płycej, pasowanie średnicy bez zmian.

- Wymiar bitu: ISO 1173:2001 (wydanie 3, obowiązuje; wcześniej podałem błędnie 1975), tabele 3 i 5: s 6,29–6,35 mm, e 7,11–7,18 mm, sześciokąt formy C min. 11 mm, formy E min. 25 mm. Dwa niezależne odczyty (dwa różne modele, bez wymiany wyników) zgodne. Przegląd tolerancji liczyłem dla s 6,292–6,350: różnica 0,002 mm na dolnej granicy nie zmienia wyniku (decyduje górna granica 6,35 / 7,18, ta sama).
- Dłuższe bity: Wera i Wiha sprzedają E6.3 do 150–152 mm, obrys ok. 7 mm (karty producentów). Bity 50/70/90 mm nie kolidowały, a każdy punkt bitu dalej niż 90 mm od dna gniazda leży wyżej niż cały uchwyt, więc bity do 152 mm też się mieszczą.

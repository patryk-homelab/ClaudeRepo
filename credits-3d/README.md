# credits-3d — uchwyty na bity z Printables, sprawdzone skillem projekt-3d-druk

Data: 2026-11-04. Drukarka docelowa: Bambu Lab X2D, dysza 0,4, PETG. Licencje i teksty do ogłoszeń: `CREDITS.md`.

**Uchwyty na wkrętaki** (1808383, 1782552, 41393, 123412): folder `wkretaki/`, opis w `wkretaki/README.md`. Od 04.11 po południu bity są sprawdzone tym samym zestawem narzędzi co wkrętaki (Bambu Studio X2D, projekty, dwa odczyty danych).

## Wynik w skrócie

| # | Model | Licencja | Co drukować (projekt Bambu X2D) | Stan po sprawdzeniu |
|---|---|---|---|---|
| 01 | [1770956 Bit holder, organizer](https://www.printables.com/model/1770956) — Jirka | CC0 | `projekt_X2D/Bit_holder_organizer_1770956_X2D_PETG.3mf` | OK bez zmian. 74 gniazda, luz 0,12 mm/stronę, 0 podpór. Wkręty 4 mm |
| 02 | [1825701 Large bit holder](https://www.printables.com/model/1825701) — Jirka | CC0 | `poprawiony/Large_bit_holder_320_fixed_X2D_PETG.3mf` | Poprawiony: 16 gniazd w przednim rzędzie było za ciasnych (luz 0,01 mm). 320 gniazd, luz 0,15 mm, 0 podpór. Wkręty 3,5 mm |
| 03 | [1051202 Ultimate Bit Holder](https://www.printables.com/model/1051202) — Carlos Gonzalez | CC BY | `poprawiony/*_X2D_PETG.3mf` (3x7, 8x4) + `projekt_X2D/` (przegródki, etykiety) | Siatki 3x7 i 8x4 naprawione. **Części na magnesy wycofane** (patrz niżej). Bez podpór. Autor zaprojektował całość na obrotową podstawę z magnesami |
| 04 | [146076 Hex Bit Holder](https://www.printables.com/model/146076) — GUZ_prints | CC0 | `poprawiony/hex_bit_holder_v1_mounting_ears_X2D_PETG.3mf` | Poprawiony: dodane 2 uszy na wkręty 4 mm (stożek Ø9,5). **Plik z 04.11 rano miał 2 zerowe trójkąty i otwierał się w Bambu dziurawy — zastąpiony.** 144 rurki, luz 0,25 mm |

Kody w arkuszu „Druk 3D – rejestr druku”: 01 = P071, 02 = P072, 03 = P073, 04 = P074.

## Wycofane: wszystkie części na magnesy (04.11.2026 wieczorem, decyzja Patryka)
Przeniesione do `_wycofane_magnesy_2026-11-04/` (te same ścieżki co wcześniej, nic nie skasowane; ostateczne usunięcie zostaje Tobie):
- 1051202: ramki magnesu sztabkowego (autora i moja z luzem), SELF-CENTERING…COIN_MAGNET, SINGLE_HOLDER_FOR_COIN_MAGNET = Bore_Bit_Holder, MAGNETIC_BIT_HOLDER = HEX_BIT_Extension_HOLDERs_v3 (i moja wersja na stole), socket_extension_holder (oba pliki), DIVIDERS_AND_COIN_MAGNET_HOLDER, **Amana i DeWalt** (mają po 2 gniazda Ø6,1–6,2 mm na magnesy okrągłe — sprawdzone przekrojami) oraz ich projekty Bambu i kod ramki.
- 123412 (wkrętaki Wera): szyna `rail_200mm_magnets_10x3mm` i jej projekt.
- Zostały z 1051202: uchwyty bitów 3x7 i 8x4, przegródki DIVIDER_1…8 i SMALL_DIVIDER_2_ENLARGED, etykiety screw_head_labels — bez gniazd na magnesy. Uwaga: autor pisze, że cały system jest „optimized to work with magnets” (magnesy pod uchwytami przyciągają bity). Bez magnesów bity trzymają się w gniazdach pod kątem 45° tylko grawitacją i tarciem (wniosek, nie sprawdzone wydrukiem).

## Co zrobiłem 04.11 po południu (ten sam poziom co przy wkrętakach)
1. **Bambu Studio 2.8.2 z profilem X2D** zamiast PrusaSlicera: każda część pocięta z podporami auto (drzewiaste, próg 30°), oryginały też (przed/po). Czasy i gramy z ustawieniami zapisanymi w projekcie.
2. **Projekty Bambu `*_X2D_PETG.3mf`** dla każdego pliku do druku (22 projekty). W każdym sprawdziłem siatkę po wczytaniu przez Bambu: zamknięta, liczba trójkątów jak w źródle. Ten test znalazł błąd w 04 (poprawiony) i potwierdził wszystkie 158 projektów wkrętaków.
3. **Dwa niezależne odczyty danych** (dwa różne modele, bez wymiany wyników): norma bitu, długości bitów, łby wkrętów, magnesy. Wynik: tabela niżej; obowiązuje ISO 1173:2001, nie 1975.
4. **Nowe sprawdzenia z tych danych:** łby wkrętów w stożkach (01, 02, 04), magnesy w gniazdach (03), bity do 152 mm i ściana (wszystkie).
5. **build123d-mcp:** nowa ramka magnesu zbudowana i sprawdzona narzędziem skilla (`validate`, `analyze_printability`, `export`), eksport powtarzalny. Wieczorem wycofana razem z magnesami (`_wycofane_magnesy_2026-11-04/`).
6. **Dokładne źródła:** sprawdziłem STEP autora 146076. Bryła v1 w nim to ta sama siatka co STL (nie dokładniejsza); prawdziwy CAD ma tylko v2 z cieńszymi ściankami. 01, 02, 03 mają tylko siatki. Poprawki zostają więc operacjami na siatce, z bilansem objętości.

## Dane urządzeń (bity, wkręty, magnesy)

| Dane | Wartość | Źródło | Status |
|---|---|---|---|
| Sześciokąt 1/4" (C6.3, E6.3): rozstaw płaskich s | 6,29–6,35 mm | ISO 1173:2001 (wyd. 3), tabele 3 i 5 (podgląd iTeh) | norma; oba odczyty zgodne |
| Rozstaw naroży e | 7,11–7,18 mm | j.w. | norma; oba zgodne |
| Długość sześciokąta | C6.3 min. 11 mm, E6.3 min. 25 mm; rowek E6.3: Ø4,7 mm, 9,5 mm od końca | j.w. | norma; oba zgodne |
| Długość bitów w sprzedaży | C6.3: 25 mm; E6.3: 50, 70, 89/90, 110, 127, 150/152 mm; obrys ok. 7 mm | karty Wera (851/1 Z, 851/4 Z, 855/4 Z) i Wiha (7011 Z, 7041 Z) | producent; oba zgodne |
| Łeb wkrętu stożkowego 3,5 / 4,0 / 4,5 mm | 6,5 / 7,5 / 8,3 mm (DIN 7997); producenci: 4,0 mm 7,0–8,9, 4,5 mm 7,6–9,6 mm | DIN 7997 (tabela z fasten.it), Würth ASSY (ETA-11/0190), SPAX (karta Bossard), ISO 7050 (90°) | DIN 7997: oba odczyty zgodne (ta sama tabela osób trzecich, norma niedostępna); Würth, SPAX, ISO 7050: jeden odczyt |
| Magnes sztabkowy | 60 × 10 mm wg autora; 60 × 10 × 3 mm wg linkowanej oferty | opis 1051202, Amazon (MIKEDE) | osoby trzecie; oba zgodne |
| Magnes okrągły | 6 × 3 mm (Ø6 × 3 — wniosek); w opiniach kupujących ok. 1,7 mm grubości | opis 1051202, Amazon (DIYMAG) | osoby trzecie; 6 × 3 oba zgodne, 1,7 mm tylko jeden odczyt (podsumowanie opinii) |
| Minimalny luz na stronę | 0,10 mm | brak `printer.json` z kalibracji X2D | założenie |

## Metoda (dla każdego pliku)
- Audyt siatki (trimesh): zamknięta, liczba brył, objętość, wymiary, min z, grubość ścianek metodą promieni, nawisy >45°.
- Gniazda: przekroje prostopadłe do osi gniazda co 0,5–1 mm; tylko część prosta gniazda (przekroje identyczne co do pola ±0,1% i wymiarów ±0,01 mm).
- Przegląd tolerancji: siatka s × e = 4 × 3 kombinacji (s co 0,019 mm, e co 0,035 mm, oba końce zakresu normy), bit może się obrócić (szukanie najlepszego kąta co 0,5°).
- Wkładanie: bit 6,350/7,180 przesuwany wzdłuż osi gniazda z 40 mm nad modelem co 0,25 mm (manifold3d), pierwszy kontakt = osadzenie; kontrola kolizji bitów 50/70/90 mm.
- Testy kontrolne w każdym pliku: bit o 0,2 mm większy od gniazda musi zostać wykryty (2D), bit wciśnięty 1 mm za osadzenie musi dać kolizję (3D). Oba wykryte we wszystkich plikach.
- Slicer: od 04.11 po południu Bambu Studio 2.8.2 z profilem X2D (jak przy wkrętakach; skrypty `narzedzia/bambu_studio/` i `wkretaki/narzedzia/bambu_studio/`). Wcześniej PrusaSlicer 2.7.2 — jego liczby podpór zostały w raportach dla porównania.
- Skrypty i surowe wyniki: `narzedzia/`.
- Podgląd 3D z bitami w gniazdach: `podglad-3d.html` (otwórz w przeglądarce, potrzebny internet do three.js) albo artefakt https://claude.ai/artifact/ExojbNBGfsdRknsn7V3KSo.

## Bambu Studio X2D

Bambu Studio 2.8.2, `Bambu Lab X2D 0.4 nozzle`, `0.20mm Standard @BBL X2D`, `Bambu PETG Basic @BBL X2D 0.4 nozzle` (1,25 g/cm³), Textured PEI. Podpory: auto, drzewiaste, próg 30°. Filament i czas z ustawieniami projektu (bez podpór, model na środku stołu). Surowe wyniki: `narzedzia/wyniki/bambu_x2d_jak_w_projekcie.txt` i `bambu_studio_x2d_bity_wszystkie.tsv`.

| # | Plik do druku | Podpory: oryginał → do druku | Filament | Czas |
|---|---|---|---|---|
| 01 (P071) | oryginał | 0 | 89,36 g | 3,27 h |
| 02 (P072) | poprawiony | 0 → 0 (PrusaSlicer: 155 → 0) | 115,84 g | 5,71 h |
| 03 (P073) | 3x7 / 8x4 naprawione | 0 → 0 (PrusaSlicer 3x7: 42 → 0) | 22,35 g / 36,90 g | 1,11 h / 1,31 h |
| 03 (P073) | RIGHT_ANGLE / Dewalt 90° (wycofany: magnesy) | 340 → 0 (ułożenie z 3MF autora) | 11,57 g | 0,50 h |
| 03 (P073) | MAGNETIC_BIT_HOLDER (wycofany: magnesy) | 7 → 0 (obie części na stole) | 6,88 g | 0,27 h |
| 04 (P074) | z uszami | 0 → 0 | 83,50 g | 4,07 h |

## Czego nie zrobiłem (i dlaczego)
1. Nie zapisałem na pulpit: ta sesja działa w chmurze i nie ma dostępu do Twojego komputera. Folder jest w repo, gałąź `claude/blissful-edison-wf7mwj`.
2. Sesja na MiniPC zablokowana przez filtr bezpieczeństwa sesji chmurowej, więc: brak porównania sum kontrolnych MP ↔ chmura, brak `printer.json`/`devices.json` (luz minimalny dalej założony 0,10 mm/stronę), brak wpisu nowych danych do biblioteki na MP. Zamiast tego: powtórne uruchomienie skryptów daje identyczny STL (sha256).
3. Poprawki 02, 03 (siatki), 04 są operacjami na siatkach autorów (manifold3d), bo dokładnego CAD nie ma (patrz wyżej). Zakres zmian: bilans objętości w każdym raporcie.
4. Drugi odczyt przez ChatGPT/Gemini/Grok (skill zapytaj-inne-ai) wymaga sieci domowej; zastąpiony dwoma niezależnymi odczytami dwóch modeli Claude.
5. Projekty Bambu powstały w trybie wiersza poleceń i nie były otwierane w aplikacji z ekranem. Jeśli któryś się nie otworzy, użyj samej geometrii (`.3mf` obok).
6. Pasowań pod konkretne narzędzia w 1051202 (Amana, DeWalt, wiertła do drewna, przedłużki) nie sprawdzałem: brak zweryfikowanych wymiarów tych produktów.

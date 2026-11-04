# 01 — Large screwdriver holder with honeycomb pattern (Printables 1808383)

- Autor: Jirka (`Jirka_4226633`), **CC0**, opublikowany 2026-08-12, brak modelu nadrzędnego.
- Printables (2026-11-04): 870 polubień, 2990 pobrań, 4 wydruki, ocena 4,8 (5 ocen). Komentarz: „Great for screwdrivers and similar tools”.
- Opis autora: 220 × 114 × 45 mm, sześciokąt 9 mm „dla średnich i większych wkrętaków”, 2 lub 4 wkręty. 3MF autora: PrusaSlicer, MK4S, PETG, 0,2 mm, 3 obrysy, 15%, podpory wyłączone.

## Decyzja: drukować wersję poprawioną
- Projekt Bambu (X2D, 0,20 mm Standard, Bambu PETG Basic, Textured PEI): `poprawiony/screwdriver_holder_honeycomb_1808383_fixed_X2D_PETG.3mf`
- Sama geometria: `poprawiony/screwdriver_holder_honeycomb_1808383_fixed.3mf`; skrypt: `poprawiony/fix_shelves.py` (argument `1808383`).

## Co było nie tak
Jeden otwór (x 121,3, y 151,3) jest od spodu, na 10 mm wysokości, poszerzony do sześciokąta 10,4 mm. Ścianka do sąsiednich otworów ma tam 0,7 mm (wszędzie indziej 1,4 mm). Bambu Studio X2D z automatycznymi podporami stawia tam podporę od stołu (49 fragmentów, tylko w tym miejscu). Funkcji to nie ma; wygląda na pozostałość po modelowaniu.

## Poprawka
Wypełnienie poszerzenia i ponowne wycięcie zwykłego otworu 9,0 mm (kształt skopiowany z otworu nad nim). Dodano 235,21 mm³ = (93,67 − 70,15) mm² × 10 mm, usunięto 0. Nic innego się nie zmieniło.

## Wyniki

| Sprawdzenie | Oryginał | Poprawiony |
|---|---|---|
| Siatka | zamknięta, 1 bryła | zamknięta, 1 bryła |
| Wymiary | 220 × 114 × 45 mm | bez zmian |
| Otwory | 195 × 9,0 mm + 1 poszerzony od spodu do 10,4 | 196 × 9,0 mm (naroża 10,39), rozstaw 10,4 |
| Ścianki między otworami (przekrój) | min. 0,70 mm | min. 1,40 mm |
| Grubość półki | 20 mm | bez zmian |
| Bambu Studio X2D, auto podpory | 49 fragmentów podpór (jeden otwór) | **0** |
| Bambu Studio: filament / czas | 160,3 g / 6,9 h | 160,5 g / 6,9 h |
| Stół X2D | mieści się | mieści się |

## Pasowanie wkrętaków (otwór 9,0 mm na płaskich)
- Trzonki do 8 mm przechodzą (ISO PH3/PZ3 8 mm: luz 0,5 mm na stronę; Wiha płaski 10–12 mm ma trzonek 8 mm).
- Nie przejdą: PH4/PZ4 (10 mm), Wera 334 1,6×10 (9,0 mm), grube izolowane VDE (np. Cimco PZ3 10,7 mm).
- Rękojeść musi być większa niż 10,4 mm (naroża otworu). Każda pełnowymiarowa rękojeść jest; bardzo cienkie wkrętaki precyzyjne mogą wpaść.

## Pojemność praktyczna (wszystkie naraz, 1 mm między rękojeściami)

| Średnica rękojeści | 23 mm (PH0) | 27 | 30 (PH1) | 36 (PH2) | 41 mm (PH3) |
|---|---|---|---|---|---|
| Wkrętaków naraz | 27 | 18 | 18 | 15 | 11 |
| Otwory, które w ogóle da się użyć (uszy montażowe i ściana blokują resztę) | 190 | 186 | 184 | 182 | 176 |

Liczone zachłannie od przodu, więc to dolna granica. W ogłoszeniu nie pisać „196 wkrętaków”.

## Ryzyka
1. Luzy liczone bez kurczenia otworów w druku. Jeśli trzonek 8 mm wchodzi ciasno, ustaw w Bambu Studio kompensację otworów XY.
2. Projekt Bambu (`*_X2D_PETG.3mf`) powstał w Bambu Studio 2.8.2 w trybie wiersza poleceń i nie był otwierany w aplikacji z ekranem. Cięcie z tymi samymi ustawieniami działa ze źródłowego STL. Jeśli projekt się nie otworzy, użyj `screwdriver_holder_honeycomb_1808383_fixed.3mf`.

## Do zmierzenia suwmiarką na pierwszym wydruku
1. Otwór na płaskich (model 9,0 mm), w środku i przy krawędzi.
2. Otwory na wkręty w uszach.

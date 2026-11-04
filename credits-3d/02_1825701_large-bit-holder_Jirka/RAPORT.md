# 02 — Large bit holder (wall mounted) (Printables 1825701)

- Autor: Jirka (`Jirka_4226633`), licencja **CC0**, opublikowany 2026-08-28, brak modelu-rodzica.
- Printables (2026-11-04): 289 polubień, 888 pobrań, 1 wydruk, ocena 5,0 (1 ocena).
- Opis autora: 176 bitów, PETG, 3 wkręty. 3MF autora: PrusaSlicer, MK4S, PETG, 0,2 mm, 3 obrysy, 12%, **podpory wyłączone**.
- **Nazwa jest myląca: model ma 320 gniazd, nie 176.**

## Decyzja: drukować wersję poprawioną
Plik: `poprawiony/Large_bit_holder_320_fixed.3mf`. Skrypt: `poprawiony/fix_1825701.py` (wejście: oryginalny STL).

## Co było nie tak (oryginał)
1. Przedni rząd 16 gniazd jest przycięty przez krawędź wzoru autora na y = 82,0 mm: 6,439 mm zamiast 6,65 mm między płaskimi. Bit z normy mieści się tylko z luzem 0,011–0,040 mm/stronę (przy dobrym obrocie), czyli po druku praktycznie nie wejdzie.
2. 3 otwory na wkręty (Ø4,2 mm, poziome, ze stożkiem 90° pod łeb) — PrusaSlicer wstawia w nie podpory (155 bloków).

## Poprawka (operacja na oryginalnej siatce, manifold3d)
1. 16 gniazd przedniego rzędu wycięte pełnym sześciokątem skopiowanym z pozostałych 304 gniazd, w pozycji siatki y = 88,96 − 3,85 = 85,11 mm (rozstaw rzędów zmierzony: 3,85 mm), dno bez zmian (z = 2,0).
2. Otwory: dach „łezka” 45° (wierzchołek r·√2 nad osią) na całej długości otworu i w stożku pod łeb.
3. Bilans: usunięto 182,2 mm³, dodano 0,0 mm³. Nic poza tymi miejscami się nie zmieniło.

## Wyniki (wersja poprawiona)

| Sprawdzenie | Oryginał | Poprawiony |
|---|---|---|
| Siatka | zamknięta, 1 bryła | zamknięta, 1 bryła |
| Wymiary | 226 × 98 × 42 mm | 226 × 98 × 42 mm |
| Objętość bryły | 143,20 cm³ | 143,01 cm³ |
| Ścianki (promienie) | min 1,04 mm | min 1,04 mm |
| Gniazda | 304 × 6,65 + 16 × 6,439 mm | 320 × 6,65 mm (naroża 7,68) |
| Przegląd tolerancji (12 kombinacji) | 0 kolizji; 16 gniazd poniżej luzu 0,10 mm | 0 kolizji; luz 0,150–0,151 mm/stronę we wszystkich 320 |
| Wkładanie | 320/320 bez blokady | 320/320 bez blokady, bit na dnie |
| Głębokość / wystaje bit 25 mm | 10,0 / 15,0 mm | 10,0 / 15,0 mm |
| Bity 50/70/90 mm | 0 kolizji | 0 kolizji |
| Slicer (PrusaSlicer, auto podpory) | 155 bloków podpór (otwory) | **0** |
| Stół X2D | mieści się | mieści się (226 mm ≤ 256) |

## Ryzyka
1. Luz 0,15 mm/stronę i brak kalibracji X2D: przy ciasnym pasowaniu użyj kompensacji otworów XY w slicerze.
2. Otwory na wkręty mają kształt łezki z ostrym wierzchołkiem u góry — tylko wygląd; łeb wkrętu opiera się na części stożkowej jak wcześniej.
3. W projekcie 3MF autora podpory są wyłączone, więc oryginalne otwory prawdopodobnie też dają się wydrukować mostkiem (hipoteza, nie sprawdzałem wydrukiem); poprawka usuwa to ryzyko, nie zmienia funkcji.

## Do zmierzenia suwmiarką na pierwszym wydruku
1. Rozstaw płaskich gniazda w przednim i w środkowym rzędzie (model 6,65 mm).
2. Głębokość gniazda (model 10,0 mm).
3. Otwór na wkręt w najwęższym miejscu (model Ø4,2 mm).

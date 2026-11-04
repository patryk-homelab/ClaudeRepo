# 02 — Large bit holder (wall mounted) (Printables 1825701)

- Autor: Jirka (`Jirka_4226633`), licencja **CC0**, opublikowany 2026-08-28, brak modelu-rodzica.
- Printables (2026-11-04): 289 polubień, 888 pobrań, 1 wydruk, ocena 5,0 (1 ocena).
- Opis autora: 176 bitów, PETG, 3 wkręty. 3MF autora: PrusaSlicer, MK4S, PETG, 0,2 mm, 3 obrysy, 12%, **podpory wyłączone**.
- **Nazwa jest myląca: model ma 320 gniazd, nie 176.**

## Decyzja: drukować wersję poprawioną
Projekt Bambu (X2D, bez podpór): `poprawiony/Large_bit_holder_320_fixed_X2D_PETG.3mf`. Sama geometria: `poprawiony/Large_bit_holder_320_fixed.3mf`. Skrypt: `poprawiony/fix_1825701.py` (wejście: oryginalny STL).

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

## Dopisane 04.11.2026 (ten sam poziom sprawdzeń co przy wkrętakach)
- Bambu Studio 2.8.2 X2D, podpory auto (drzewiaste, próg 30°): **oryginał też 0 podpór** (PrusaSlicer stawiał 155 bloków w otworach na wkręty). Poprawka otworów (dach 45°) nie była więc potrzebna dla X2D; zostaje, bo nie zmienia funkcji (łeb dalej opiera się na stożku) i chroni przy innym slicerze. Najważniejsza poprawka to 16 przyciętych gniazd. Z ustawieniami projektu: 115,84 g, 5,71 h (oryginał 115,80 g).
- Siatka w projekcie Bambu zamknięta, 10 302 trójkąty jak w pliku.
- Wymiar bitu: ISO 1173:2001 (wydanie 3, obowiązuje; wcześniej podałem błędnie 1975), tabele 3 i 5: s 6,29–6,35 mm, e 7,11–7,18 mm, sześciokąt formy C min. 11 mm, formy E min. 25 mm. Dwa niezależne odczyty (dwa różne modele, bez wymiany wyników) zgodne. Przegląd tolerancji liczyłem dla s 6,292–6,350: różnica 0,002 mm na dolnej granicy nie zmienia wyniku (decyduje górna granica 6,35 / 7,18, ta sama).
- Dłuższe bity: Wera i Wiha sprzedają E6.3 do 150–152 mm, obrys ok. 7 mm (karty producentów). Bity 50/70/90 mm nie kolidowały, a każdy punkt bitu dalej niż 90 mm od dna gniazda leży wyżej niż cały uchwyt, więc bity do 152 mm też się mieszczą.
- Wkręty: 3 poziome otwory Ø4,2 mm, stożek 90° Ø8,5 mm; bity stoją równolegle do ściany. Wkręt 3,5 mm: luz 0,35 mm na stronę, łeb 6,5–7,3 mm mieści się. Wkręt 4 mm: luz tylko 0,1 mm na stronę (po druku może wchodzić ciasno), łeb do 8,5 mm (Würth ASSY 8,9 mm wystanie). W ogłoszeniu: wkręty 3,5 mm z łbem stożkowym.

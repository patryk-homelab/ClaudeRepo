# 01 — Bit holder, organizer / Držák bitů (Printables 1770956)

- Autor: Jirka (`Jirka_4226633`), licencja **CC0**, opublikowany 2026-07-03, brak modelu-rodzica.
- Printables (2026-11-04): 324 polubienia, 884 pobrania, 4 wydruki, ocena 4,75 (4 oceny).
- Opis autora: uchwyt ścienny, PETG, 2 wkręty. 3MF autora: PrusaSlicer, MK4S, PETG, warstwa 0,2, 2 obrysy, wypełnienie 12%.
- Komentarz 2026-09-09: „Printed 2 of them, came out perfect and work perfectly.”

## Decyzja: drukować oryginał bez zmian
Projekt Bambu (X2D, bez podpór): `projekt_X2D/Bit_holder_organizer_1770956_X2D_PETG.3mf`. Sama geometria: `oryginal/Bit_holder,_organizer.3mf` (siatka identyczna z STL: 2852 trójkąty, ta sama objętość).

## Wyniki

| Sprawdzenie | Wynik |
|---|---|
| Siatka | zamknięta, 1 bryła, 236,6 cm³ (bryła), 80,2 × 191,2 × 38,3 mm, min z = 0 |
| Ścianki (promienie, wszystkie ściany) | min 1,97 mm |
| Nawisy > 45° | 0 mm² |
| Gniazda | 74, sześciokąt 6,605 mm (płaskie) / 7,621 mm (naroża), głębokość 9,0 mm, oś pochylona 21,7° od pionu |
| Przegląd tolerancji (12 kombinacji s × e) | 0 kolizji, min luz 0,123 mm/stronę (najgorszy bit 6,350/7,180) |
| Luz minimalny 0,10 mm/stronę | spełniony we wszystkich 74 |
| Wkładanie (co 0,25 mm) | 74/74 bez blokady, bit siada na dnie |
| Bit 25 mm | wystaje 16,0 mm |
| Bity 50/70/90 mm | 0 kolizji |
| Otwory montażowe | 2 × Ø4,49 mm |
| Slicer (PrusaSlicer, auto podpory) | 0 bloków podpór, ~93 cm³ filamentu (profil domyślny) |
| Stół X2D 256 × 256 × 260 | mieści się |

## Ryzyka
1. Luz 0,12 mm/stronę zakłada otwory drukowane w wymiarze; FDM drukuje otwory mniejsze. Zmierz pierwsze gniazdo; jeśli bit wchodzi ciasno, poszerz otwory kompensacją otworów XY w slicerze o 0,05–0,1 mm.
2. Komentarze potwierdzają, że bity pasują przy druku autora (Prusa MK4S, PETG), nie na X2D.

## Do zmierzenia suwmiarką na pierwszym wydruku
1. Rozstaw płaskich gniazda (model 6,60 mm).
2. Głębokość gniazda (model 9,0 mm).
3. Średnica otworów na wkręty (model 4,49 mm).

## Dopisane 04.11.2026 (ten sam poziom sprawdzeń co przy wkrętakach)
- Bambu Studio 2.8.2 X2D (0.20mm Standard, Bambu PETG Basic 1,25 g/cm³, Textured PEI): z podporami auto (drzewiaste, próg 30°) 0 podpór. Z ustawieniami projektu (bez podpór, model na środku stołu): 89,36 g, 3,27 h.
- Siatka w projekcie Bambu zamknięta, 2852 trójkąty jak w pliku autora (Bambu niczego nie usuwa przy wczytaniu).
- Wymiar bitu: ISO 1173:2001 (wydanie 3, obowiązuje; wcześniej podałem błędnie 1975), tabele 3 i 5: s 6,29–6,35 mm, e 7,11–7,18 mm, sześciokąt formy C min. 11 mm, formy E min. 25 mm. Dwa niezależne odczyty (dwa różne modele, bez wymiany wyników) zgodne. Przegląd tolerancji liczyłem dla s 6,292–6,350: różnica 0,002 mm na dolnej granicy nie zmienia wyniku (decyduje górna granica 6,35 / 7,18, ta sama).
- Dłuższe bity: Wera i Wiha sprzedają E6.3 do 150–152 mm, obrys ok. 7 mm (karty producentów). Bity 50/70/90 mm nie kolidowały, a każdy punkt bitu dalej niż 90 mm od dna gniazda leży wyżej niż cały uchwyt, więc bity do 152 mm też się mieszczą.
- Wkręty: 2 otwory Ø4,5 mm ze stożkiem 90° Ø9,4 mm, stożek od strony widocznej, ściana po stronie stołu; bit oddala się od ściany. Wkręt 4 mm: luz 0,25 mm na stronę, łeb do 8,9 mm chowa się w stożku (DIN 7997: 7,5 mm; SPAX 8,0; Würth ASSY 7,0–8,9 mm). Wkręt 4,5 mm nie przejdzie (luz 0). W ogłoszeniu: wkręty 3,5–4 mm z łbem stożkowym.

# 04 — Hex Bit Holder (Printables 146076)

- Autor: GUZ_prints (`GUZ_prints_227736`), licencja **CC0**, data publikacji w API: 2023-08-14, brak modelu-rodzica.
- Printables (2026-11-04): 251 polubień, 1872 pobrania, 9 wydruków, ocena 4,91 (11 ocen).
- Pliki autora: `hex_bit_holder.stl` (v1), `hex_bit_holder_v2.stl`, `single_unit_hex_bit.stp` (jedna komórka), `hex_bit_holder.stp` (52 MB, w repo jako `.zip`). Duży STEP to 146 osobnych brył (560 × 86 × 132 mm), nie gotowa część — nie nadaje się jako źródło.
- Komentarze: 2022-06-03 „Its not easily screwed. It can twist and bow. I would prefer … a pre-drilled hole for a screw”; 2023-11-27 „Bits are a bit loose but stay in just fine.”

## Decyzja: drukować wersję poprawioną (v1 + uszy montażowe)
Projekt Bambu (X2D, bez podpór): `poprawiony/hex_bit_holder_v1_mounting_ears_X2D_PETG.3mf`. Sama geometria: `poprawiony/hex_bit_holder_v1_mounting_ears.3mf` (wersja z 04.11.2026, patrz niżej). Skrypt: `poprawiony/fix_146076.py` (wejście: `oryginal/hex_bit_holder.stl`).

Dlaczego v1, nie v2: ścianki między rurkami w przekroju poziomym v1 = 2,05 mm, v2 = 1,60 mm (v2 jest mniejsza: 164 × 82 mm, 55,5 cm³). Grubsza v1 jest sztywniejsza, a skarga dotyczyła wyginania. Obie mają 144 rurki tego samego rozmiaru.

## Poprawka (operacja na oryginalnej siatce, manifold3d)
- 2 płaskie uszy na tylnej ściance (strona stołu), na obu końcach w kierunku pochylenia rurek — po przykręceniu: góra i dół.
- Ucho: szerokość 26 mm, grubość 5 mm, zaokrąglony koniec R13, otwór Ø4,5 mm (wkręt 4 mm), stożek 90° Ø9,5 mm od strony widocznej (do 04.11: Ø9,0), środek otworu 9 mm za krawędzią plastra.
- Ucho zachodzi 14 mm pod plaster i jest wycięte kształtem 144 rurek: dodany materiał wewnątrz rurek = 0,0 mm³ (sprawdzone).
- Bilans: dodano 5967,5 mm³, usunięto 0,012 mm³ (uproszczenie siatki).

## Wyniki

| Sprawdzenie | Oryginał v1 | Poprawiony |
|---|---|---|
| Siatka | zamknięta, 1 bryła | zamknięta, 1 bryła |
| Wymiary | 175,2 × 85,6 × 14,7 mm | 219,2 × 85,6 × 14,7 mm |
| Objętość bryły | 69,02 cm³ | 74,99 cm³ |
| Ścianki między rurkami (przekrój poziomy z = 0,1…7 mm) | 2,05 mm, do krawędzi 1,60 mm | bez zmian |
| Rurki | 144 przelotowe, sześciokąt 6,842 / 7,90 mm, oś 40° od prostopadłej do ściany | bez zmian |
| Przegląd tolerancji (12 kombinacji) | 0 kolizji, luz 0,246 mm/stronę | 0 kolizji, luz 0,246 mm/stronę |
| Wkładanie | — | 144/144 bez blokady, bit opiera się o ścianę |
| Głębokość / wystaje bit 25 mm | — | 11,2–11,4 / 7,0–13,7 mm |
| Bity 50/70/90 mm | — | 0 kolizji |
| Slicer (PrusaSlicer) | 0 podpór | 0 podpór |
| Stół X2D | mieści się | mieści się (219 mm ≤ 256) |

Uwaga do audytu: metoda promieni pokazuje w poprawionym pliku „min 0,29 mm” przy samym stole. To błąd pomiaru (promień z pochyłej ścianki rurki wychodzi przez płaszczyznę stołu po 0,3 mm), potwierdzony pomiarem przekrojów powyżej. Ten sam błąd wcześniej fałszywie wskazywał za cienkie ścianki w v2.

## Ryzyka
1. Rurki są przelotowe — bit opiera się o ścianę. Na nierównej ścianie lub perforowanej płycie (pegboard) krótkie bity mogą się przesunąć głębiej; przy montażu na płycie z otworami podłóż płaską płytę.
2. Luz 0,25 mm/stronę: zgodnie z komentarzem bity siedzą luźno, ale nie wypadają (oś 40°). Bez kalibracji X2D nie wiem, czy po druku luz zostanie.
3. Uszy wystają 22 mm poza plaster (góra i dół) — podaj w ogłoszeniu wymiar całkowity 219 × 86 mm.

## Do zmierzenia suwmiarką na pierwszym wydruku
1. Rozstaw płaskich rurki (model 6,84 mm).
2. Otwór w uchu (model Ø4,5 mm) i średnica stożka (Ø9,5 mm).
3. Grubość ucha (model 5,0 mm).

## Dopisane 04.11.2026 (ten sam poziom sprawdzeń co przy wkrętakach)
- **Błąd w poprzedniej wersji pliku:** Bambu Studio przy wczytaniu usuwało z niej 2 trójkąty o zerowej powierzchni (na spodzie, przy styku ucha z plastrem) i siatka w projekcie była otwarta (6 trójkątów mniej). Poprawione w `fix_146076.py`: przed uproszczeniem siatka przechodzi przez float32 (jak w STL), uproszczenie 1e-4 mm usuwa te trójkąty; skrypt sprawdza, że nie ma zerowych trójkątów. Zmiana kształtu < 0,02 mm³. Teraz siatka w projekcie Bambu zamknięta, 6872 trójkąty przed i po wczytaniu. Dwa przebiegi skryptu dają ten sam STL (sha256 1a1a1023…6f99).
- **Stożek pod łeb Ø9,0 → Ø9,5 mm:** łby wkrętów 4 mm mają 7,0–8,9 mm (DIN 7997: 7,5; SPAX 8,0; Würth ASSY do 8,9). Przy Ø9,0 łeb 8,9 mm byłby równo z powierzchnią bez zapasu. Zmierzone na nowym pliku: Ø4,5 → Ø9,4 mm w przekroju 0,05 mm pod powierzchnią, kąt 90°. Wkręt 4 mm: luz 0,25 mm na stronę; wkręt 4,5 mm nie przejdzie.
- Pasowanie bitów po zmianie sprawdzone od nowa: 144 rurki, luz 0,246 mm na stronę, 144/144 bez blokady, testy kontrolne wykryte (`../narzedzia/wyniki/pasowanie_F_146076.json`).
- Bambu Studio 2.8.2 X2D, podpory auto: oryginał v1 i wersja z uszami 0 podpór. Z ustawieniami projektu (bez podpór): 83,50 g, 4,07 h (przy włączonych podporach, choć żadnych nie stawia, Bambu liczy 4,29 h; projekt ma podpory wyłączone).
- **STEP autora:** `hex_bit_holder.stp` zawiera 146 brył: 144 pojedyncze komórki, **całą v1** i całą v2. Bryła v1 w STEP to ta sama siatka co STL (33 052 trójkątne ściany B-spline = 33 052 trójkąty STL, objętość 69 021 mm³), więc nie jest dokładniejsza. Prawdziwą bryłą CAD jest tylko v2 (1505 ścian, głównie płaskich), ale v2 ma cieńsze ścianki (1,60 mm) i jej nie wybrałem. v1 ma wyłącznie płaskie ściany, więc STL odwzorowuje ją bez błędu zaokrąglenia.
- Wymiar bitu: ISO 1173:2001 (wydanie 3, obowiązuje; wcześniej podałem błędnie 1975), tabele 3 i 5: s 6,29–6,35 mm, e 7,11–7,18 mm, sześciokąt formy C min. 11 mm, formy E min. 25 mm. Dwa niezależne odczyty (dwa różne modele, bez wymiany wyników) zgodne. Przegląd tolerancji liczyłem dla s 6,292–6,350: różnica 0,002 mm na dolnej granicy nie zmienia wyniku (decyduje górna granica 6,35 / 7,18, ta sama).
- Dłuższe bity: Wera i Wiha sprzedają E6.3 do 150–152 mm, obrys ok. 7 mm (karty producentów). Bity 50/70/90 mm nie kolidowały, a każdy punkt bitu dalej niż 90 mm od dna gniazda leży wyżej niż cały uchwyt, więc bity do 152 mm też się mieszczą.

# 02 — Large massive screwdriver holder (Printables 1782552)

- Autor: Jirka (`Jirka_4226633`), **CC0**, opublikowany 2026-07-16, brak modelu nadrzędnego.
- Printables (2026-11-04): 820 polubień, 2036 pobrań, 2 wydruki, ocena 5,0 (2 oceny). Komentarz: „gedruckt mit PLA. Schraubenzieher passen gut rein.”
- Opis autora: półokrągły, plaster miodu, „dla małych i średnich wkrętaków”. 3MF autora: PrusaSlicer, MK4S, PETG, 0,2 mm, 3 obrysy, 12%, podpory wyłączone.

## Decyzja: drukować wersję poprawioną
- Projekt Bambu (X2D, 0,20 mm Standard, Bambu PETG Basic, Textured PEI, model wyśrodkowany): `poprawiony/massive_screwdriver_holder_1782552_fixed_X2D_PETG.3mf`
- Sama geometria: `poprawiony/massive_screwdriver_holder_1782552_fixed.3mf`; skrypt: `poprawiony/fix_shelves.py` (argument `1782552`).

## Co było nie tak
Wzór plastra miodu jest przycięty krawędzią obszaru otworów: 21 otworów przy łukach i przy uszach ma tylko 3,9–7,5 mm zamiast 8,0 mm. Trzonek PH2 (6 mm) nie wejdzie w 13 z nich. Ten sam typ błędu był w uchwycie na bity 1825701 tego autora.

## Poprawka
W każdym z 21 miejsc wycięty pełny sześciokąt (kształt skopiowany z regularnego otworu) w węźle siatki, którego pełny sześciokąt zawiera przycięty otwór (pokrycie 100%). Wycinak jest większy o 0,005 mm na stronę, żeby jego ściany nie pokrywały się ze ścianami starego otworu: pokrywające się ściany zostawiały 10 trójkątów o zerowej powierzchni, a Bambu Studio usuwało je przy imporcie i otwierało siatkę. Te 21 otworów ma więc 8,01 mm zamiast 8,00. Usunięto 9916,4 mm³, dodano 0. Ścianka do krawędzi spadła miejscami do 1,47 mm, czyli tyle co ścianki między otworami (1,39–1,40 mm).

## Wyniki

| Sprawdzenie | Oryginał | Poprawiony |
|---|---|---|
| Siatka | zamknięta, 1 bryła | zamknięta, 1 bryła |
| Wymiary | 244 × 135 × 55 mm | bez zmian |
| Otwory | 184 × 8,0 mm + 21 przyciętych (3,9–7,5) | 184 × 8,00 + 21 × 8,01 mm (naroża 9,24–9,25), rozstaw 9,4 |
| Ścianki między otworami / do krawędzi | 1,40 / 5,86 mm | 1,39 / 1,47 mm |
| Grubość półki | 25 mm | bez zmian |
| Bambu Studio X2D, auto podpory | 0 | 0 |
| Bambu Studio: filament / czas | 205,1 g / 8,7 h | 203,9 g / 8,7 h |
| Stół X2D | 244 mm z 256: mieści się tylko wyśrodkowany; automatyczne rozmieszczanie Bambu Studio go odrzuca | j.w. (w projekcie ustawiony na środku) |

## Pasowanie wkrętaków (otwór 8,0 mm na płaskich)
- PH0–PH2 / PZ0–PZ2 (3–6 mm): luz 1,0–2,5 mm na stronę; płaskie do 7 mm trzonka.
- PH3/PZ3 (8 mm): luz 0, **nie wejdzie** po druku. Zgodne z opisem autora („małe i średnie”).

## Pojemność praktyczna (wszystkie naraz, 1 mm między rękojeściami)

| Średnica rękojeści | 23 mm | 27 | 30 | 36 | 41 mm |
|---|---|---|---|---|---|
| Oryginał | ≥25 | ≥17 | ≥15 | ≥13 | ≥9 |
| Poprawiony | ≥28 | ≥21 | ≥16 | ≥13 | ≥11 |

Liczone zachłannie od przodu, więc to dolna granica (drobne zmiany kolejności dają ±5 przy Ø27).

## Ryzyka
1. Model ma 244 mm: w Bambu Studio nie przesuwaj go z środka i drukuj dyszą z pełnym obszarem 256 mm (druga strefa X2D ma 235,5 mm).
2. Ścianka 1,47 mm do krawędzi w kilku miejscach na łuku: wytrzymałość jak ścianek wewnętrznych, ale to zewnętrzna powierzchnia.
3. Projekt Bambu (`*_X2D_PETG.3mf`) powstał w Bambu Studio 2.8.2 w trybie wiersza poleceń i nie był otwierany w aplikacji z ekranem. Cięcie z tymi samymi ustawieniami działa ze źródłowego STL. Jeśli projekt się nie otworzy, użyj `massive_screwdriver_holder_1782552_fixed.3mf` i wybierz profile ręcznie.

## Do zmierzenia suwmiarką na pierwszym wydruku
1. Otwór na płaskich (model 8,0 mm), w tym jeden z dawniej przyciętych przy łuku.
2. Grubość ścianki przy łuku w tym miejscu (model 1,47 mm).

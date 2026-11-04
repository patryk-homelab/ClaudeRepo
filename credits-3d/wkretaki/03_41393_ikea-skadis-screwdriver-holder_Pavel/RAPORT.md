# 03 — IKEA Skadis screwdriver holder (Printables 41393)

- Autor: Pavel (`Pavel_81109`), **CC BY**, opublikowany 2020-09-23, brak modelu nadrzędnego.
- Printables (2026-11-04): 1123 polubienia, 7145 pobrań, **97 wydruków**, ocena 4,94 (84 oceny).
- Pliki: `screwdriver_small.stl`, `screwdriver_big.stl` (+ źródła FreeCAD `.FCStd`), `hook_skadis_universal.stl` (2 haki na grzebień).
- Komentarze potwierdzają pasowanie haków: „tolerances for the hooks is just right”, „Fits Perfect on Skadis”, „Printed it … without supports”. Jedna uwaga: „some of the slots are a bit close together on the larger model” (zgodne z pomiarem: skrajne szczeliny co 21 mm).

## Decyzja: drukować bez zmian kształtu, z dokładnej bryły
- Projekty Bambu (X2D, PETG, **bez podpór**): `z_bryly_FreeCAD/…_X2D_PETG.3mf` (grzebień mały, duży, hak).
- Geometria z bryły FreeCAD autora przez build123d-mcp `export`: `z_bryly_FreeCAD/ikea_skadis_screwdriver_comb_*_41393.3mf`.
- Bryła FreeCAD (ostatnia operacja `Pocket004`) to źródło STL autora: różnica 0,1% objętości wynika z zaokrąglenia łuków w STL.

## Wyniki

| Sprawdzenie | Grzebień mały | Grzebień duży | Hak |
|---|---|---|---|
| build123d-mcp `validate` | PASS (1 bryła, poprawny B-rep) | PASS | — (tylko STL) |
| Siatka | zamknięta, 1 bryła | zamknięta, 1 bryła | zamknięta, 1 bryła |
| Wymiary | 155 × 45 × 28 mm | 155 × 45 × 28 mm | 20,8 × 51 × 4,7 mm |
| Szczeliny | 8 × 7,5 mm, co 20 mm (jedna co 19,5) | 5 × 10 mm + 1 × 16 mm, co 21/32/33/32/21 mm | — |
| `analyze_printability` (45°, 0,4) | 2 płaskie sufity 3,0 mm (kieszenie haków) + 2 mostki 3,5 mm | j.w. | — |
| Bambu X2D z auto podporami | 106 fragmentów, tylko w 2 kieszeniach haków | 107, j.w. | 0 |
| Bambu X2D bez podpór | 0, mostki 3,0/3,5 mm | 0 | 0 |
| Filament / czas | 44,2 g / 1,3 h | 41,0 g / 1,2 h | 1,5 g / 0,1 h |

Opis autora podaje rozstaw 18 mm w małym grzebieniu; zmierzony rozstaw to 20 mm.

## Pasowanie
- **Hak ↔ SKÅDIS** (szczelina 5 × 15 mm, płyta 5,0–5,1 mm): trzon haka 4,7 × 4,7 mm (luz 0,15 mm/stronę), zaczep 5,2–5,35 mm na płytę, cały hak 14,75 mm przechodzi przez szczelinę 15 mm.
- **Trzonki:** mały grzebień 7,5 mm: PH0–PH2, płaskie do trzonka 7 mm; PH3 (8 mm) nie. Duży 10 mm: PH3 z luzem 1 mm/stronę; PH4 (10) nie; szczelina 16 mm na grube narzędzia.
- **Rękojeść ↔ płyta:** rowek na górze ma środek 20 mm od płyty, więc rękojeść do Ø40 mm stoi pionowo, a Ø41 (Wiha PH3) opiera się o płytę (0,5 mm).

## Pojemność praktyczna (wszystkie naraz)

| Średnica rękojeści | 23 | 27 | 30 | 36 | 41 mm |
|---|---|---|---|---|---|
| Mały grzebień (8 szczelin) | 4 | 4 | 4 | 4 | 3 |
| Duży grzebień (6 szczelin) | 4 | 4 | 4 | 3 | 3 |

## Ryzyka
1. Przy włączonych podporach Bambu Studio wstawia je do kieszeni haków, skąd trudno je wyjąć. W projektach podpory są wyłączone; nie włączaj ich.
2. Grubość płyty SKÅDIS znam tylko z pomiarów osób trzecich (5,0–5,1 mm). Przy płycie 5,85 mm zaczep (5,2–5,35) nie wejdzie.
3. Projekty Bambu (`*_X2D_PETG.3mf`) powstały w Bambu Studio 2.8.2 w trybie wiersza poleceń i nie były otwierane w aplikacji z ekranem. Cięcie z tymi samymi ustawieniami działa ze źródłowego STL. Jeśli projekt się nie otworzy, użyj `ikea_skadis_screwdriver_comb_*_41393.3mf`.

## Do zmierzenia suwmiarką na pierwszym wydruku
1. Szczelina zaczepu haka (model 5,2–5,35 mm) i grubość Twojej płyty SKÅDIS.
2. Szerokość szczeliny w grzebieniu (7,5 / 10 mm).

# 04 — Wera Screwdriver Holder (Printables 123412)

- Autor: ksuszka (`ksuszka_192195`); w skryptach OpenSCAD: Krzysztof Suszka. **CC BY**. Model nadrzędny: Thingiverse thing:5213820 (według listingu-lustra ten sam autor; patrz `../CREDITS.md`).
- Printables (2026-11-04): 437 polubień, 1911 pobrań, 36 wydruków, ocena 4,87 (31 ocen).
- System modułowy: 140 uchwytów (każdy pod konkretny wkrętak Wera lub Holex), 13 szyn, 5 dystansów, skrypty OpenSCAD v1/v2/v3, rysunki DXF.

## Decyzja: drukować uchwyty z `poprawiony/`, szyny z `poprawiony/szyny/` (kształt szyn bez zmian)
- Projekty Bambu (X2D, PETG, podpora tylko od stołu pod tylną wnęką, tak jak zaleca autor): `poprawiony/*_snapfix_X2D_PETG.3mf` (140 plików).
- Sama geometria: `poprawiony/*_snapfix.3mf`; skrypt: `poprawiony/wera_snapfix.py`; raport każdego pliku: `poprawiony/snapfix_report.json`.
- Nowe, własne uchwyty: `poprawiony/wera_screwdriver_holder_v3_snapfix.scad` (parametr `snap_relief_end_y = 12`; `0` = oryginał).
- Projekty szyn: `poprawiony/szyny/*_X2D_PETG.3mf` (12 szyn, wypełnienie 100% jak zaleca autor; szyna na magnesy wycofana).

## Co było nie tak: zatrzask pęka
Komentarze: 2023-11-21 „every time I want to hook the holder onto the rail, the thin part breaks off”, 2025-02-13 „very fragile to breaking when mounting on a rail”, 2025-07-20 „issues with broken clips”, 2024-02-05 „hard time attaching”.

Analiza (geometria ze skryptu v3, przekrój zatrzasku):
- Uchwyt wpina się na szynę zaczepem C: górny haczyk (zakładany pod kątem) i dolna stopka, która musi się ugiąć o **0,7 mm**.
- Stopka ma 2 mm grubości i ok. 5,75 mm długości. Odkształcenie zginające wynosi 1,5·t·y/L² = 1,5·2·0,7/5,75² ≈ **6,4%**.
- Uchwyty drukuje się na plecach, więc stopka jest zginana w poprzek warstw. Bambu PETG Basic (karta TDS V2.0): wydłużenie przy zerwaniu w osi Z **5,7 ± 0,6%** (X-Y 11,2%), wytrzymałość Z 39 MPa przy module 1460 MPa, czyli koniec zakresu sprężystego ok. 2,7%. Pęknięcie jest więc spodziewane, zgodnie z komentarzami.

## Poprawka
Szczelina odciążająca 1 mm (z −13…−12 mm, od 3 do 12 mm od tylnej ściany, na całej szerokości) przedłuża sprężynujący odcinek stopki do ok. 10,5 mm. Grubość u nasady ok. 1,57–1,7 mm. Odkształcenie ≈ 1,5·1,57·0,7/10,5² ≈ **1,5%**, poniżej 2,7%.
- Zastosowana do każdego z 140 opublikowanych plików osobno, z zachowaniem napisów autora.
- Każdy plik po zapisie: zamknięty, 1 bryła, objętość zgodna. Usunięto 4,5–6,9 mm³ na mm szerokości, zależnie od wersji skryptu, z której powstał plik (5 grup).
- Profil stopki po poprawce identyczny we wszystkich grupach: stopka −15…−13 mm, szczelina −13…−12 mm, nasada na 12 mm.
- Osadzenie na szynie bez zmian, sprawdzone w 2D na 5 reprezentantach różnych wersji: kolizja po osadzeniu 0, haczyk górny 1,5 mm, stopka 0,7 mm.
- Bambu Studio X2D: te same 19 fragmentów podpory pod tylną wnęką przed i po poprawce (poprawka nie dodaje podpór).

## Gniazda vs katalog Wera
- 68 uchwytów da się porównać z katalogiem Wera (wera.de; oba niezależne odczyty zgodne). We wszystkich gniazdo rękojeści odpowiada klasie rękojeści Wera (70/81/98/105/112), a otwór trzonka jest większy od średnicy katalogowej: luz 0,25–1,00 mm na stronę (n = 40 z podaną średnicą).
- Komentarze z 2023 r. („PH0 holder about 3 mm too small”, „PH1 about 2 mm smaller”): obecne pliki 350 PH0 i PH1 są zgodne z katalogiem (PH0: rękojeść 81, otwór 4,0 mm na trzonek 3,0). Hipoteza: skargi dotyczyły starszych plików.
- Starsze wersje skryptu mają gniazdo rękojeści 0,23–1,02 mm ciaśniejsze niż v3. Autor wydrukował i potwierdził wiele z nich, więc ich nie zmieniałem. Wyjątek do obserwacji: **352 hex 1,5 i 2** (−0,97 mm, autor ich nie testował).
- VDE (160i/162i/165i/167i): Wera nie publikuje średnic izolowanych trzonków. Sprawdzona jest tylko klasa rękojeści; średnice trzonka pochodzą z pomiarów autora.

## Szyny
- Szyna 270 mm **nie mieści się prosto na stole X2D** (270 > 256 mm). Po przekątnej (45°) mieści się, 0 podpór; projekt jest tak ustawiony.
- Pozostałe szyny (81,8–250 mm) mieszczą się prosto.
- Szyna SKÅDIS 240 mm: kołki 4,5 × 4,5 mm co 40 mm, zaczep na płytę 5,2 mm, zgodnie z SKÅDIS (5 × 15 mm, raster 40 mm, płyta 5,0–5,1). Potrzebuje podpór pod 6 hakami (24 fragmenty; po odwróceniu 48, więc zostaje orientacja z pliku).

## Montaż (do instrukcji dla klienta)
Najpierw zahacz górny haczyk uchwytu o górną krawędź szyny, trzymając uchwyt pochylony, potem dociśnij dół, aż zatrzaśnie. Nie wciskaj uchwytu prosto na szynę.

## Ryzyka
1. Obliczenie zatrzasku to teoria belki (stała grubość, sztywne utwierdzenie). Daje proporcje, nie siłę. Poprawka zmniejsza sztywność stopki kilkukrotnie, więc uchwyt może łatwiej spadać przy szarpnięciu. Górny haczyk nadal przenosi ciężar.
2. Pierwsze warstwy (strona stołu) to zaczepy: kompensacja „stopy słonia” w profilu X2D wynosi 0,15 mm. Nie wyłączaj jej, bo zwiększa wcisk.
3. 352 hex 1,5 / 2: gniazdo o 1 mm ciaśniejsze niż v3. W razie problemu wygeneruj nowy plik z `wera_screwdriver_holder_v3_snapfix.scad` (linie `352 1.5` i `352 2.0`).
4. Napisy na uchwytach używają czcionek Bahnschrift i Arial. Nowe pliki generowane z `.scad` bez tych czcionek będą miały inne litery.
5. Projekty Bambu (`*_X2D_PETG.3mf`) powstały w Bambu Studio 2.8.2 w trybie wiersza poleceń i nie były otwierane w aplikacji z ekranem. Cięcie z tymi samymi ustawieniami działa ze źródłowego STL. Jeśli projekt się nie otworzy, użyj `*_snapfix.3mf`.

## Do zmierzenia na pierwszym wydruku
1. Wpięcie na szynę: czy stopka zatrzaskuje się palcem bez trzasku materiału.
2. Szczelina odciążająca (1,0 mm), czy nie zarosła.
3. Gniazdo trzonka wybranego uchwytu vs trzonek wkrętaka.

## Dopisane 04.11.2026 wieczorem
- **Szyny z wypełnieniem 100%** (autor: „I recommend to print rails with 100% infill”). Wcześniejsze projekty miały domyślne 15%. Wzór wypełnienia zig-zag, bo Bambu nie przyjmuje wzoru grid przy 100%. Reszta ustawień i ułożenie bez zmian; siatki w projektach zamknięte. Z ustawieniami projektu:

| Szyna | Filament | Czas | Podpory |
|---|---|---|---|
| 81,76 mm (ściana plaster miodu) | 7,48 g | 0,21 h | 0 |
| 122,64 mm (plaster miodu) | 11,17 g | 0,30 h | 0 |
| 163,52 mm (plaster miodu) | 14,86 g | 0,39 h | 0 |
| 245,28 mm (plaster miodu) | 22,26 g | 0,59 h | 0 |
| 200 mm, otwory co 50 mm | 18,28 g | 0,47 h | 0 |
| 240 mm, otwory co 40 mm | 21,75 g | 0,57 h | 0 |
| 250 mm, otwory co 50 mm | 22,83 g | 0,59 h | 0 |
| 270 mm, otwory co 45 mm (po przekątnej) | 24,13 g | 0,57 h | 0 |
| 240 mm IKEA SKÅDIS | 25,88 g | 0,76 h | 24 fragmenty |
| 8" otwory co 1" | 18,04 g | 0,51 h | 0 |
| 8" tablica calowa cienka | 19,50 g | 0,59 h | 0 |
| 2" tablica calowa cienka | 4,94 g | 0,24 h | 0 |

Dla porównania: szyna 200 mm przy 15% — 15,64 g. Surowe wyniki: `../narzedzia/wyniki/szyny_wera_100proc.txt`.
- **Szyna na magnesy 10 × 3 mm wycofana** (decyzja Patryka: bez magnesów) — w `../../_wycofane_magnesy_2026-11-04/`.
- **Napisy są wypukłe:** skrypt autora dodaje je jako wypukłość 1 mm na froncie (`linear_extrude(height = 1)`), sprawdzone na pliku: ostatni 1 mm wysokości to same napisy (86 mm² przekroju, przód 473 mm²). Uchwyt drukuje się na plecach, więc napisy są na górze — **podpór nie potrzebują**. Zmiana koloru na ostatnich warstwach jest opcjonalna; w jednym kolorze napis jest czytelny jako relief.

## Warianty do sprzedaży (04.11.2026 wieczorem)
- Oferta podzielona: P077 = 1 uchwyt z wyborem modelu, P078 = szyna z wyborem mocowania i długości.
- `warianty_P077_uchwyty_wera.csv`: wszystkie 140 uchwytów z kodem SKU, nazwą, statusem u autora (31 modeli przetestowanych, 49 nieprzetestowanych, reszta spoza jego listy), zgodnością z katalogiem Wera, gramami, czasem i liczbą fragmentów podpór z Bambu X2D (ustawienia projektu). Generator: `../narzedzia/warianty_csv.py`, surowe wyniki: `../narzedzia/wyniki/uchwyty_wera_140_bambu.txt`.
- Wszystkie 140: 12,94–15,01 g, 0,89–0,94 h. 130 uchwytów ma tylko podporę pod tylną wnęką (19 fragmentów). **10 uchwytów** (334 płaski 5, 335 płaski 4 i 5,5, 350 PH1, 352 imbus 1,5/2/4, 355 PZ1, 367 TX15 i TX20) dostaje dodatkową podporę od stołu przy dolnej krawędzi, do ok. 39 mm (180–197 fragmentów); tak samo w oryginałach autora (sprawdzone na TX20 i PH1). Do obejrzenia w Bambu z ekranem.
- 5 par duplikatów w plikach autora (160i płaski 2,5 i 3,5; 917 PH3; 932A płaski 9 i 10 — zwykły i „v2”): przed wystawieniem wybrać jeden.

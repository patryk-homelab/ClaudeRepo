# credits-3d / wkrętaki — uchwyty z Printables sprawdzone skillem projekt-3d-druk

Data: 2026-11-04. Drukarka: Bambu Lab X2D, dysza 0,4, PETG. Licencje i teksty do ogłoszeń: `CREDITS.md`.

## Wynik w skrócie

| # | Model | Licencja | Co drukować | Stan |
|---|---|---|---|---|
| 01 | [1808383 Large screwdriver holder (honeycomb)](https://www.printables.com/model/1808383) — Jirka | CC0 | `poprawiony/…_X2D_PETG.3mf` | **Poprawiony.** 1 z 196 otworów był od spodu poszerzony (ścianka 0,7 mm, Bambu Studio chciało tam podporę). Teraz 196 równych otworów 9,0 mm, 0 podpór |
| 02 | [1782552 Large massive screwdriver holder](https://www.printables.com/model/1782552) — Jirka | CC0 | `poprawiony/…_X2D_PETG.3mf` | **Poprawiony.** 21 otworów przy krawędzi było przyciętych (3,9–7,5 mm zamiast 8,0). Teraz 205 pełnych otworów |
| 03 | [41393 IKEA Skadis screwdriver holder](https://www.printables.com/model/41393) — Pavel | CC BY | `z_bryly_FreeCAD/…_X2D_PETG.3mf` + hak | **Bez zmian kształtu.** Eksport z dokładnej bryły FreeCAD autora. Drukować bez podpór |
| 04 | [123412 Wera Screwdriver Holder](https://www.printables.com/model/123412) — ksuszka | CC BY | `poprawiony/` (140 uchwytów) + szyna z `oryginal/` | **Poprawiony.** Zatrzask pękał przy wpinaniu (≥3 zgłoszenia). Szczelina odciążająca zmniejsza odkształcenie z ok. 6,4% do ok. 1,5% |

Podgląd 3D z wkrętakami osadzonymi w uchwytach: `podglad-3d.html` (otwórz w przeglądarce, potrzebny internet do three.js) albo artefakt https://claude.ai/artifact/GQUG9JMqrCRWQgWFQkN6tg.

## Co zrobiłem inaczej niż przy bitach (dokładność)

1. **Prawdziwy slicer X2D.** Bambu Studio 2.8.2.61 (Flathub, ta sama wersja co na MacBooku) w trybie wiersza poleceń, z profilami X2D wyciągniętymi z aplikacji i spłaszczonymi: `Bambu Lab X2D 0.4 nozzle`, `0.20mm Standard @BBL X2D`, `Bambu PETG Basic @BBL X2D 0.4 nozzle`, płyta Textured PEI. Wcześniej był PrusaSlicer z ogólnym profilem.
2. **Gotowe projekty Bambu (`*_X2D_PETG.3mf`)** z ustawieniami X2D, a nie gołe siatki. Projekty nie były otwierane w aplikacji z ekranem: ponowne cięcie projektu z wiersza poleceń się nie udaje (także dla modelu, który tnie się poprawnie ze źródłowego STL, więc to ograniczenie trybu CLI). Dlatego obok każdego projektu jest też sam 3MF z geometrią.
3. **Dokładne źródła zamiast STL:** 41393 z bryły FreeCAD autora (BREP; różni się od STL o 0,1% objętości przez zaokrąglenie łuków w STL). 123412 ze skryptu OpenSCAD autora (v3 odtwarza opublikowane pliki).
4. **build123d-mcp 0.3.91 w kopii roboczej** (`validate`, `analyze_printability`, `export`). Eksport jest deterministyczny: dwa przebiegi dają ten sam STL i ten sam model w 3MF.
5. **Dwa niezależne odczyty wymiarów urządzeń** (dwa różne modele językowe, bez wymiany wyników; zgodne we wszystkich użytych wartościach) zamiast jednego.
6. **Dane materiałowe z karty producenta** (Bambu PETG Basic TDS V2.0) do obliczenia zatrzasku.
7. **Pojemność praktyczna** każdej półki i grzebienia dla realnych średnic rękojeści (ile wkrętaków mieści się naraz).

## Dane urządzeń (wkrętaki, płyta SKÅDIS)

| Dane | Wartość | Źródło | Status |
|---|---|---|---|
| Średnica trzonka PH/PZ 0/1/2/3/4 | 3 / 4,5 / 6 / 8 / 10 mm | ISO 8764-1:2004, tab. 1 i 2 (podgląd iTeh) | norma; oba odczyty zgodne |
| Trzonek płaskiego, forma B | = szerokość ostrza b | ISO 2380-2:2004, przypis do rys. 1 | norma; oba zgodne |
| Wera 350/355/335/334/367: trzonek i długość rękojeści | np. PH2: 6,0 mm, rękojeść 105; TX20: 4,5 mm, 98 | wera.de, „Facts and figures” | producent; oba zgodne |
| Wera: gabaryt rękojeści 70/81/98/105/112 | 22 / 26 / 33 / 37 / 40 mm | karty Wera „Size” (interpretacja: obrys narzędzia) | producent, interpretacja; jeden odczyt; zgodne z pomiarami autora 123412 (25,5/32/36) w granicach 1 mm |
| Wiha SoftFinish 311 PH0/1/2/3: średnica rękojeści | 23 / 30 / 36 / 41 mm | wiha.com | producent; oba zgodne |
| Felo Ergonic 402 PH0–PH3: szerokość rękojeści | 25 / 30 / 36 / 39 mm | katalog Felo 2022 | producent; jeden odczyt |
| VDE (izolowane), obrys trzonka | np. Cimco PH2 8,6, PZ3 10,7 mm | karty Cimco | producent; dane niespójne (błędy w tabeli); Wera VDE nie publikuje |
| SKÅDIS: otwór | 5 × 15 mm, zaokrąglone końce | 6 niezależnych generatorów/bibliotek | pomiary osób trzecich; oba zgodne |
| SKÅDIS: raster | 40 mm w rzędzie, rzędy co 20 mm, przesunięte o 20 mm | j.w. | pomiary osób trzecich; oba zgodne |
| SKÅDIS: grubość płyty | ok. 5 mm (5,0 / 5,1; jedno źródło 3, jedno 5,85) | j.w. | pomiary osób trzecich; zakres |
| Rękojeści do sprawdzeń | Ø 23 / 27 / 30 / 36 / 41 mm | z powyższych | zakres od PH0 do PH3 |

## Czego nie zrobiłem i dlaczego
1. **Sesja na MiniPC została zablokowana** przez automatyczny filtr bezpieczeństwa tej sesji chmurowej (uruchomienie sesji na Twoim komputerze z chmury). Nie obchodziłem tego. Przez to: brak porównania sum kontrolnych MP ↔ chmura, brak `printer.json`/`devices.json` (luz minimalny dalej założony), brak wpisu nowych danych do biblioteki na MP. Gotowy prompt do wklejenia w sesję MiniPC jest w rozmowie.
2. **Drugi odczyt przez ChatGPT/Gemini/Grok** (skill zapytaj-inne-ai) wymaga usługi AI Compare w sieci domowej. Zastąpiłem go dwoma niezależnymi odczytami dwóch różnych modeli Claude.
3. **Wersje bibliotek** w chmurze (`narzedzia/wyniki/wersje_bibliotek_workspace.txt`) nie są potwierdzone z `requirements.txt` na MP.
4. **Poprawki 01, 02 i 04 są operacjami na oryginalnych siatkach** (manifold3d), a nie przebudową w build123d, bo autorzy nie udostępnili źródeł CAD (01, 02), a w 04 zachowuję napisy autora. Zakres zmian jest udowodniony bilansem objętości w każdym raporcie.
5. Brak kodów P0xx i wpisu do arkusza „Druk 3D – rejestr druku”.

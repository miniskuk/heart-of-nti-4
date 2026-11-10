# Heart of NTI 4

Det här repot innehåller två mods till Hearts of Iron IV som byter ledarnas porträtt mot bilder på kompisar och lärare.

> ⚠️ Repot ska vara **privat**, eftersom det innehåller bilder på riktiga personer.

## Innehåll

| Mapp | Vad det är |
|---|---|
| `mods/miku_japan/` | Modden **Heart of NTI 4**. Workshop-ID: `3836823642`. |
| `mods/samuel/` | Modden **Samuel** (Tyskland/Hitler → Samuel). Workshop-ID: `3836091919`. |
| `bilder/` | Originalbilderna som porträtten är gjorda av. |
| `verktyg/leaders.py` | Hittar vilka porträttfiler ett lands ledare använder. |
| `verktyg/byt_land.sh` | Byter alla ledarporträtt för ett land i ett steg. |

## Vilka länder som är bytta (Heart of NTI 4)

| Land | Tag | Bild |
|---|---|---|
| USA | USA | Trump.jpg |
| Japan | JAP | Miku.jpg |
| Italien | ITA | nunzia.jpg |
| Finland | FIN | Casper.jpg |
| Sverige | SWE | liam.png |
| Korea | KOR | eamma.png |
| Frankrike | FRA | Arnaudw2.png |
| Sovjet | SOV | timmoy.jpg |
| Grekland | GRE | Georgios.png |
| Turkiet | TUR | Deniz.png |
| Iran/Persien | PER | Javad.png |
| Storbritannien | ENG | Viktor.png |
| Danmark | DEN | danmark.png |
| Schweiz | SWI | schweiz.png |
| Norge | NOR | norge.png |
| Portugal | POR | portugal.png |
| Jugoslavien | YUG | jugoslavien.png |
| Nederländerna | HOL | nederlanderna.png |
| Belgien | BEL | belgien.png |
| Polen | POL | polen.png |
| Argentina | ARG | `bilder/argentina-katter/` – **alla** karaktärer (ledare, generaler, rådgivare, forskare) är katter och hundar |

Bara de som kan bli **landets ledare** byts (utom Argentina, där alla är djur – se `verktyg/argentina_djur.py`; modden ersätter då `common/characters/ARG.txt`, så den filen kan behöva göras om efter stora speluppdateringar). Generaler, rådgivare och forskare byts inte. Gemensamma standardbilder (`Generic`) byts inte heller, eftersom andra länder också använder dem.

## Installera på en ny dator

1. Kopiera `mods/miku_japan` till HoI4:s mod-mapp:
   - **Windows:** `Dokument\Paradox Interactive\Hearts of Iron IV\mod\`
   - **Linux (Proton):** `~/.local/share/Steam/steamapps/compatdata/394360/pfx/drive_c/users/steamuser/Documents/Paradox Interactive/Hearts of Iron IV/mod/`
2. I samma `mod`-mapp, skapa filen `miku_japan.mod` med det här innehållet:
   ```
   version="1.0"
   tags={
   	"Graphics"
   }
   name="Heart of NTI 4"
   picture="thumbnail.png"
   supported_version="1.19.*"
   path="mod/miku_japan"
   remote_file_id="3836823642"
   ```
3. Starta launchern och aktivera **Heart of NTI 4** i din playset.

Det går också att prenumerera på modden på Steam Workshop istället.

Ha **inte** både Workshop-versionen och den lokala versionen av samma mod aktiva samtidigt. Då hoppar spelet över modden eller kraschar.

## Lägga till ett nytt land

Porträtten är DDS-filer (DXT5, utan mipmaps) som ligger på samma sökväg som spelets egna filer, till exempel `gfx/leaders/SWE/...`. Stora porträtt är 156x210 och små ikoner är oftast 65x67.

På Linux med ImageMagick 7 och Python 3:

```bash
./verktyg/byt_land.sh SWI bilder/schweiz.png 760x1023+230+30 440x453+400+110 switzerland swiss
```

- **Första crop:** utsnittet för stora porträtt, alltså ansikte och bröst.
- **Andra crop:** utsnittet för små ikoner, alltså bara ansiktet.
- **Sista orden:** extra sökord för landets händelsefiler.

Kopiera sedan den uppdaterade `mods/miku_japan` till spelets mod-mapp.

## Uppdatera på Workshop

Öppna launchern och välj **Mod Tools** → **Upload Mod**. Fyll i Mod ID `3836823642` så uppdateras den befintliga modden istället för att en ny skapas.

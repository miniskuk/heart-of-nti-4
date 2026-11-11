# Heart of NTI 4

Det här repot innehåller modden Heart of NTI 4 till Hearts of Iron IV som byter ledarnas porträtt mot bilder på kompisar och lärare.

> Alla personer på bilderna har sagt att det är okej att bilderna är publika.

## Innehåll

| Mapp | Vad det är |
|---|---|
| `mods/miku_japan/` | Modden **Heart of NTI 4**. Workshop-ID: `3836823642`. |
| `bilder/` | Originalbilderna som porträtten är gjorda av. |
| `verktyg/leaders.py` | Hittar vilka porträttfiler ett lands ledare använder. |
| `verktyg/byt_land.sh` | Byter alla ledarporträtt för ett land i ett steg. |

## Vilka länder som är bytta (Heart of NTI 4)

| Land | Tag | Vem | Bild |
|---|---|---|---|
| USA | USA | Donald Trump | Trump.jpg |
| Japan | JAP | Hatsune Miku | Miku.jpg |
| Italien | ITA | Nunzia Lampitelli (Naturkunskap & tekniker) – Mussolini heter "Nunzia Mussolini" i spelet | italien.png |
| Finland | FIN | Casper | Casper.jpg |
| Sverige | SWE | Liam | liam.png |
| Korea | KOR | Emma | eamma.png |
| Frankrike | FRA | Arnaud Dillinger (Programmering, Samhällskunskap) | Arnaudw2.png |
| Sovjet | SOV | Timmy | timmoy.jpg |
| Grekland | GRE | Georgios Arvanitidis (Matematik, Fysik) | Georgios.png |
| Turkiet | TUR | Deniz Özgurdamar (Programansvarig EE, Svenska) | Deniz.png |
| Iran/Persien | PER | Javad Maafi (Teknik, Matematik, Elektronik) | Javad.png |
| Storbritannien | ENG | Viktor Tsouplakis (Rektor) | Viktor.png |
| Danmark | DEN | Katarina Gladun Komaromi (SYV) | danmark.png |
| Schweiz | SWI | Jonas Nyman (Förstelärare, Matematik) | schweiz.png |
| Norge | NOR | Anton | norge.png |
| Portugal | POR | Lina Aker (Administratör) | portugal.png |
| Jugoslavien | YUG | Anna Hjalmarsson (Specialpedagog) | jugoslavien.png |
| Nederländerna | HOL | Anna Jeppsson (Skolsköterska) | nederlanderna.png |
| Belgien | BEL | Ida Pettersson (Kurator) | belgien.png |
| Albanien | ALB | Mathias Sandström (Yrkeslärare) | albanien.png |
| Österrike | AUS | Pelle Helander (Idrott, Historia, Samhällskunskap) | osterrike.png |
| Tjeckoslovakien | CZE | Per Björkil (Svenska, Historia) | tjeckoslovakien.png |
| Polen | POL | Marcus Persson (Medieämnen) – utom björnen Wojtek, han är sigma 🐻 | polen.png |
| Kurdistan | KUR | Agiri | kurdistan.png |
| Indien (Brittiska Raj) | RAJ | Brave | indien.png |
| Chile | CHL | Stefan Löfven | chile.png |
| Venezuela | VEN | Markus Allard | venezuela.png |
| Peru | PRU | Nunzia2 (den onda Nunzia) och Timmy2 – varannan ledare, se [backstoryn](#peru-backstory) | peru.png |
| Argentina | ARG | Katterna (och några hundar) – **alla** karaktärer (ledare, generaler, rådgivare, forskare) | `bilder/argentina-katter/` |

Bara de som kan bli **landets ledare** byts (utom Argentina, där alla är djur – se `verktyg/argentina_djur.py`; modden ersätter då `common/characters/ARG.txt`, så den filen kan behöva göras om efter stora speluppdateringar). Generaler, rådgivare och forskare byts inte. Gemensamma standardbilder (`Generic`) byts inte heller, eftersom andra länder också använder dem.

## Peru-backstory

Långt uppe i Anderna, på ett hemligt NTI-gymnasium byggt av gamla Inka-stenar, fanns en spegel. Den som tittade i den kom ut på andra sidan – fast lite… *ondare*.

**Nunzia2** var den första. Medan den vanliga Nunzia rättar labbrapporter i Italien, kom Nunzia2 ut ur spegeln med solglasögon, en sash i Perus färger och en enda plan: att ta över Lima med fredstecken och ett leende som får generaler att svettas. Hennes motto: *”Naturkunskap är makt.”*

Strax efter klev **Timmy2** ut. Han hade lämnat Sovjet bakom sig, odlat ett skägg på rekordtid och lärt sig korsa armarna så hårt att hela Andernas armé kände sig granskad. Ingen har någonsin sett hans ögon bakom glasögonen. Ingen vågar fråga.

Tillsammans bildade de **Juntan av Två**: varannan gång Peru byter ledare tar den ena över efter den andra. Ingen i spelet vet vem som egentligen styr – och det är precis så de vill ha det.

Deras enda svaghet? En mystisk QR-kod som sägs leda till landets största hemlighet. Ingen som har skannat den har någonsin blivit densamma igen. 🎵

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

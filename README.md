# Sisäinen Varastonhallintajärjestelmä

Moderni web-sovellus yrityksen sisäisten ja ulkoisten varastojen hallintaan. Rakennettu Flaskilla ja SQLitellä, moderneilla käyttöliittymäratkaisuilla.

## Ominaisuudet

- 📦 **Selaa tuotteita**: Näytä kaikki tuotteet responsiivisessa ruudukkojärjestyksessä
- ➕ **Lisää tuotteita**: Lisää helposti uusia tuotteita tiedoilla kuten nimi, kuvaus, hinta, määrä, kategoria ja sijainti
- ✏️ **Muokkaa tuotteita**: Päivitä tuotetiedot ja määrät
- 🗑️ **Poista tuotteita**: Poista tuotteita varastosta
- 🔍 **Haku**: Etsi tuotteita nimellä tai kuvauksella
- 🏷️ **Suodata**: Suodata tuotteita kategorian ja varastosijainnin mukaan
- ⚙️ **Hallinnoi kategorioita**: Lisää ja poista kategorioita järjestelmässä
- 📊 **Tilastot**: Näytä keskeiset mittarit kuten tuotteiden kokonaismäärä, varastotasot ja varaston arvo
- 📍 **Varastopaikat**: Seuraa tuotteita eri varastopaikoissa (3 sisäistä + 3 ulkoista varastoa)
- 🎨 **Moderni käyttöliittymä**: Kaunis gradient-muotoilu responsiivisilla korteilla ja sujuvilla animaatioilla

## Varastopaikat

### Sisäiset varastot
- Vantaa
- Tampere
- Hollola

### Ulkoiset varastot
- Ulkovarasto 1
- Ulkovarasto 2
- Ulkovarasto 3

## Oletuskategoriat

- DEMOLAITTEET
- VALMIIT
- KOTELOT
- IT TAVARAT
- TARVIKKEET
- LAITEOSAT

Kategorioita voi lisätä ja poistaa käyttöliittymän kautta.

## Edellytykset

- Python 3.7 tai uudempi
- pip (Python-paketinhallinta)

## Asennus

1. Kloonaa repositorio:
```bash
git clone https://github.com/anstaman/Inventory.git
cd Inventory
```

2. Asenna riippuvuudet:
```bash
pip install -r requirements.txt
```

3. Alusta tietokanta esimerkkituotteilla:
```bash
python init_db.py
```

Tämä luo SQLite-tietokannan 20 esimerkkituotteella, jotka on jaettu eri kategorioihin ja varastoihin.

## Sovelluksen käynnistäminen

Käynnistä Flask-kehityspalvelin:
```bash
python app.py
```

Sovellus on käytettävissä osoitteessa `http://localhost:5000`

## Käyttö

### Tuotteiden selaus
- Pääsivu näyttää kaikki tuotteet ruudukkonäkymässä
- Jokainen tuotekortti näyttää nimen, kuvauksen, hinnan, määrän, kategorian ja varastopaikan
- Tuotteet on värikoodattu varastotason mukaan (vähäinen, keskitaso, korkea)

### Tuotteen lisääminen
1. Klikkaa "Lisää tuote" -painiketta
2. Täytä tuotetiedot modaalilomakkeessa
3. Klikkaa "Tallenna tuote"

### Tuotteen muokkaaminen
1. Klikkaa "Muokkaa"-painiketta tuotekortissa
2. Muokkaa tuotetietoja modaalilomakkeessa
3. Klikkaa "Tallenna tuote"

### Tuotteen poistaminen
1. Klikkaa "Poista"-painiketta tuotekortissa
2. Vahvista poistaminen

### Haku ja suodatus
- Käytä hakukenttää löytääksesi tuotteita nimellä tai kuvauksella
- Käytä kategoria-pudotusvalikkoa suodattaaksesi kategorian mukaan
- Käytä varasto-pudotusvalikkoa suodattaaksesi varastopaikan mukaan
- Kaikkia suodattimia voi käyttää yhdessä

### Kategorioiden hallinta
1. Klikkaa "Hallinnoi kategorioita" -painiketta
2. Lisää uusi kategoria kirjoittamalla nimi ja klikkaamalla "Lisää"
3. Poista kategoria klikkaamalla "Poista"-painiketta kategorian kohdalla

## Tietokantarakenne

Sovellus käyttää yksinkertaista SQLite-tietokantaa kahdella taululla:

### Product-taulu

| Kenttä | Tyyppi | Kuvaus |
|--------|--------|---------|
| id | Integer | Pääavain |
| name | String(100) | Tuotteen nimi |
| description | String(500) | Tuotteen kuvaus |
| quantity | Integer | Varastomäärä |
| price | Float | Tuotteen hinta |
| category | String(100) | Tuotteen kategoria |
| location | String(100) | Varastopaikka |
| created_at | DateTime | Luontiaika |

### Category-taulu

| Kenttä | Tyyppi | Kuvaus |
|--------|--------|---------|
| id | Integer | Pääavain |
| name | String(100) | Kategorian nimi (uniikki) |
| created_at | DateTime | Luontiaika |

## API-päätepisteet

### Tuotteet
- `GET /` - Pääsovelluksen sivu
- `GET /api/products` - Hae kaikki tuotteet
- `GET /api/products/<id>` - Hae tietty tuote
- `POST /api/products` - Luo uusi tuote
- `PUT /api/products/<id>` - Päivitä tuote
- `DELETE /api/products/<id>` - Poista tuote

### Kategoriat
- `GET /api/categories` - Hae kaikki kategoriat
- `POST /api/categories` - Luo uusi kategoria
- `DELETE /api/categories/<id>` - Poista kategoria

## Käytetyt teknologiat

- **Backend**: Flask (Python web-kehys)
- **Tietokanta**: SQLite Flask-SQLAlchemy ORM:llä
- **Frontend**: HTML5, CSS3 (vanilla), JavaScript (vanilla)
- **Suunnittelu**: Moderni gradient-käyttöliittymä responsiivisella ruudukkoasettelulla

## Projektirakenne

```
Inventory/
├── app.py              # Pää-Flask-sovellus
├── init_db.py          # Tietokannan alustusohjelma
├── requirements.txt    # Python-riippuvuudet
├── templates/
│   └── index.html      # Frontend-sovellus
└── inventory.db        # SQLite-tietokanta (luodaan init_db.py:n jälkeen)
```

## Lisenssi

Tämä projekti on avointa lähdekoodia ja saatavilla MIT-lisenssillä.

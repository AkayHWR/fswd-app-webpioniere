---
title: Karl Tebbe
parent: Individual Contributions
nav_order: 1
---


# Karl Tebbe

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

1,3

### Personal goals
- Sicherer Umgang mit Flask (Routing, Templates, Datenbankanbindung)  
- Verständnis für die Struktur einer Full-Stack Webanwendung  
- Erste praktische Erfahrung mit einer Two-Sided Plattform  
- Effektive Zusammenarbeit im Team  


---

## Eidesstattliche Erklärung

**[Karl Tebbe, Matrikelnr.: 77205564852]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | **Dynamische Kategorisierung & Fragen-Erstellung (`create_question`)**. Implementierung der Route und der Hilfsfunktion `hashtags_from_text(text)`. Nutzer können Fragen stellen und mit beliebigen Hashtags versehen, die per Regex extrahiert, dedupliziert und alphabetisch sortiert werden (vgl. DD-04). | Anstatt ein starres Dropdown-Menü zu nutzen, erlaubt diese Funktion maximale inhaltliche Flexibilität für die Studierenden. Die Plattform passt sich dadurch organisch an neue Module oder Nischenthemen an. | Die Herausforderung lag in der Backend-Normalisierung der unstrukturierten Freitexte. Mittels `set()` und regulären Ausdrücken (`r'#[A-Za-z0-9_ÄÖÜäöüß]+'`) werden Duplikate entfernt und Umlaute korrekt für die Dashboard-Filterung aufbereitet. |
| 2 | **Gamification-Logik & All-Time Leaderboard**. Entwicklung der Route `/leaderboard` und der Punktelogik `calculate_points`, welche Upvotes (+1), Downvotes (-1) und akzeptierte Lösungen (+5) über separate SQL-Abfragen für alle Nutzer aggregiert (vgl. DD-07). | Die Berechnungslogik verknüpft mehrere relationale Abhängigkeiten fehlerfrei und baut ein dauerhaftes, motivierendes "Hall of Fame"-Ranking für die engagiertesten Helfer der Hochschule auf. | Das Zusammenführen der getrennten Abfragen pro Nutzer erforderte eine saubere Strukturierung der Python-Schleifen. Zudem musste die finale Liste dynamisch in Python sortiert werden (`sort(key=lambda user: user['points'])`), um das Ranking korrekt darzustellen. |
| 3 | **Plattform-Integrität & Fehlerbehandlung (`login_required` und Errorhandler)**. Entwicklung eines eigenen Python-Dekorators zur Absicherung geschützter Routen und Abstimmungen (vgl. DD-10) sowie Implementierung der globalen 404/500-Fehlerseiten. | Durch den Login-Zwang wird das "One User, One Vote"-Prinzip garantiert, was Manipulationen am Leaderboard unmöglich macht. Zudem leiten die Errorhandler bei Abstürzen sicher ins Dashboard zurück. | Die Template-Vererbung (`extends base.html`) für die Fehlerseiten musste reibungslos integriert werden, ohne die globalen CSS-Regeln des Teams zu durchbrechen. Außerdem musste der Umgang mit `functools.wraps` verstanden werden, um den Dekorator zu bauen. |

## Design Decisions that I led

1. [DD #04](../design-decisions/dd-04.md) (Dynamic Categorization vs. Fixed Category List)
2. [DD #07](../design-decisions/dd-07.md) (Leaderboard Timeframe: All-Time Ranking vs. Time-Boxed Windows)
3. [DD #10](../design-decisions/dd-10.md) (Voting Permissions: Authenticated vs. Anonymous Voting)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Architekturentscheidung zur freien Hashtag-Kategorisierung `(DD-04)` | https://github.com/AkayHWR/fswd-app-webpioniere/commit/695c133 | Keine externen Quellen außer fswd-home und gemini |
| Architekturentscheidung zur Festlegung des All-Time Rankings `(DD-07)` | https://github.com/AkayHWR/fswd-app-webpioniere/commit/4bfc421 | Keine externen Quellen außer fswd-home und gemini |
| Architekturentscheidung zum Authentifizierungszwang beim Voting `(DD-10)` https://github.com/AkayHWR/fswd-app-webpioniere/commit/ecd04c3 | Keine externen Quellen außer fswd-home und gemini |
| Route `/question/create` für das Erstellen von Beiträgen inklusive Formulardaten-Validierung | https://github.com/AkayHWR/fswd-app-webpioniere/commit/1333046 | Keine externen Quellen außer fswd-home und gemini |
| Hilfsfunktion `hashtags_from_text` mit regulären Ausdrücken zur automatischen Tag-Generierung | https://github.com/AkayHWR/fswd-app-webpioniere/commit/66efeb7 | Keine externen Quellen außer fswd-home und gemini |
| Kern-Logik für das `Leaderboard` und die Einzelpunktberechnung `calculate_points` in app.py | https://github.com/AkayHWR/fswd-app-webpioniere/commit/672b803 | Keine externen Quellen außer fswd-home und gemini |
| Eigener Python-Dekorator `@login_required` zur strikten Zugriffskontrolle geschützter Endpunkte | https://github.com/AkayHWR/fswd-app-webpioniere/commit/1bb69da | Keine externen Quellen außer fswd-home und gemini |
| Globale Errorhandler `@app.errorhandler` für HTTP 404 und `404.html` Statuscode | https://github.com/AkayHWR/fswd-app-webpioniere/commit/cd54c8f | Keine externen Quellen außer fswd-home und gemini |
| Globale Errorhandler `@app.errorhandler` für HTTP 500 und `500.html` Statuscode | https://github.com/AkayHWR/fswd-app-webpioniere/commit/54741c9 | Keine externen Quellen außer fswd-home und gemini |
| Erstellung des korrespondierenden Frontend-Templates `create_question.html` | https://github.com/AkayHWR/fswd-app-webpioniere/commit/5a97466 | Keine externen Quellen außer fswd-home und gemini |
| Erstellung des korrespondierenden Frontend-Templates `leaderboard.html` | https://github.com/AkayHWR/fswd-app-webpioniere/commit/1836a17 | Keine externen Quellen außer fswd-home und gemini |

---

### AI Directory

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  | Gemini  | Unterstützung bei der Umsetzung der Hashtag-Generierung und Validierung für die Fragenerstellung | [`app.py` – `create_question`, `hashtags_from_text`], [DD-04](../design-decisions/dd-04.md) | Nach Lösungsvorschlägen für das Extrahieren von Hashtags mittels Regex gefragt. Zudem nach Best-Practices für das Abfangen von leeren Formularfeldern (`.strip()`) gefragt und bei der Ausformulierung der Doku (DD-04) helfen lassen. |
| 02  | Gemini  | Unterstützung bei der Strukturierung der Punkteberechnung und des Leaderboard-Rankings | [`app.py` – `leaderboard`, `calculate_points`], [DD-07](../design-decisions/dd-07.md) | Nach Methoden gefragt, um mehrere SQL-Zählungen in Python iterativ zusammenzuführen. Außerdem nach der Syntax zum Sortieren der finalen Liste (`lambda`) sowie nach Argumenten für die Gamification-Abwägungen in DD-07 gefragt. |
| 03  | Gemini  | Unterstützung bei der Erstellung eines eigenen Python-Dekorators für geschützte Routen | [`app.py` – `@login_required`], [DD-10](../design-decisions/dd-10.md) | Mir die generelle Funktionsweise von Dekoratoren (`functools.wraps`) an einem Beispiel erklären lassen und die Logik dann für den eigenen Session-Check adaptiert. Auch Hilfe beim Strukturieren der Argumentation in DD-10 genutzt. |
| 04  | Gemini  | Syntax-Unterstützung beim globalen Exception-Handling und Einbinden der Error-Templates | [`app.py` – `@app.errorhandler`], `404.html`, `500.html` | Nach dem korrekten syntaktischen Aufbau gefragt, wie man in Flask HTTP-Fehlercodes (`404`, `500`) in Kombination mit Jinja-Templates zurückgibt. |
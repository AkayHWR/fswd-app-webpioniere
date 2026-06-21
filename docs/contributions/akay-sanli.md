---
title: Akay Mert Sanli
parent: Individual Contributions
nav_order: 1
---


# Akay Sanli

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

1,0

### Personal goals

Ich möchte meine Full-Stack App-Entwicklung Skills aktiv verbessern und interessiere mich persönlich für die entwicklung von Webapps. Außerdem finde ich Python sehr cool und möchte insgesamt eine coole App im Rahmen dieses Kurses entwickeln.

---

## Eidesstattliche Erklärung

**[Akay Sanli, Matrikelnr.: 77209531265]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | **Kern-Datenmodell und Datenmodell-Dokumentation** für StudySwap, insbesondere die Strukturen `user`, `question` und `answer` sowie ihre Beziehungen. Den später von einem Teammitglied ergänzten Abstimmungsteil beanspruche ich dabei nicht als eigene Leistung. | Diese Grundlage trägt fast alle Funktionen der Anwendung: Login, Dashboard, Fragen, Antworten und die API greifen auf dieselbe relationale Struktur zurück. Außerdem war das der Beginn des Projekts und so eine der wichtigsten Commits. | Das Modell musste für eine kleine Flask-/SQLite-App verständlich bleiben und zugleich realistische Abläufe sowie spätere Erweiterungen durch das Team ermöglichen. |
| 2 | **Dashboard-Ablauf in `app.py` und `templates/dashboard.html`** mit Suche, Hashtag-Filtern, Fragevorschauen, Antwortanzahlen und Links zu den Fragendetails. | Besonders gelungen finde ich, dass der zentrale Einstiegspunkt der App ihren Nutzen sofort sichtbar macht: Studierende können Fragen finden, filtern und direkt öffnen. | SQL-Joins, GET-Parameter, ausgewählte Tags und das Jinja-Rendering mussten zusammengeführt werden. Außerdem musste in der dashboard.html vieles angezeigt werden, u.a. die hashtags bei der die Umsetzung schwerer war als gedahct, weil ich nicht ganz wusste, wie ich die tags anzeigen lassen soll und die Anzahl der Tags "herausfinde". |
| 3 | **Technische Ausrichtung durch DD-00 und DD-01 sowie gemeinsame Template-Arbeit in `templates/base.html`**. Ich habe die Entscheidungen für reines SQL/SQLite und Bootstrap geleitet und mit der tatsächlichen App-Struktur verbunden. | Die Entscheidungen hatten unmittelbaren Einfluss auf die gemeinsame Entwicklung: Sie schufen eine konsistente Basis für Quellcode, Datenbank und Benutzeroberfläche. | Hier galt es, Geschwindigkeit, Lernwert und Wartbarkeit abzuwägen, da zu viel Abstraktion oder zu viel eigenes CSS die Zusammenarbeit unnötig erschwert hätte. |

## Design Decisions that I led

1. [DD #00](../design-decisions/dd-00.md)
2. [DD #01](../design-decisions/dd-01.md)
3. [DD #08](../design-decisions/dd-08.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Relationale Datenbankgrundlage mit Schema, Beispieldaten und korrigierter Löschreihenfolge | [Initiales Datenbankkonzept](https://github.com/AkayHWR/fswd-app-webpioniere/commit/63666b6), [Korrektur der Datenbankinitialisierung](https://github.com/AkayHWR/fswd-app-webpioniere/commit/282cd2b) | Keine externen Quellen außer fswd-home und chatgpt |
| Dashboard-Route und Anbindung an das Jinja-Template | [Route und `base.html`](https://github.com/AkayHWR/fswd-app-webpioniere/commit/3669b5b), [Template-Anbindung](https://github.com/AkayHWR/fswd-app-webpioniere/commit/f4f5879) | Keine externen Quellen außer fswd-home und chatgpt |
| Fragenkarten im Dashboard inklusive Antworten, Stimmen und Verlinkung zur Detailansicht | [Fragenübersicht](https://github.com/AkayHWR/fswd-app-webpioniere/commit/de99bad), [Antworten, Stimmen und Detail-Link](https://github.com/AkayHWR/fswd-app-webpioniere/commit/0c72860), [Überarbeitung des Dashboards](https://github.com/AkayHWR/fswd-app-webpioniere/commit/8a22bb9) | Keine externen Quellen außer fswd-home und chatgpt |
| Suche und Hashtag-Navigation im Dashboard | [Suche](https://github.com/AkayHWR/fswd-app-webpioniere/commit/f139e86), [Tags](https://github.com/AkayHWR/fswd-app-webpioniere/commit/2cb92f5), [Top- und weitere Tags](https://github.com/AkayHWR/fswd-app-webpioniere/commit/f8accd0) | Keine externen Quellen außer fswd-home und chatgpt |
| Gemeinsames Basis-Template, Navigation und Logout-Integration | [Alle Templates angelegt](https://github.com/AkayHWR/fswd-app-webpioniere/commit/210c342), [`base.html` ergänzt](https://github.com/AkayHWR/fswd-app-webpioniere/commit/ef87c08), [Logout in `base.html`](https://github.com/AkayHWR/fswd-app-webpioniere/commit/35b0e98) | Keine externen Quellen außer fswd-home und chatgpt |
| Dashboard-Layout und eigenes CSS überarbeitet und gepflegt | [Dashboard und CSS überarbeitet](https://github.com/AkayHWR/fswd-app-webpioniere/commit/479760b) | Keine externen Quellen außer fswd-home und chatgpt |
| Datenmodelldokumentation und ER-Diagramm erstellt bzw. korrigiert | [Datenmodell dokumentiert](https://github.com/AkayHWR/fswd-app-webpioniere/commit/f8ff985), [Diagramm korrigiert](https://github.com/AkayHWR/fswd-app-webpioniere/commit/58e6ae2) | Eigenes implementiertes Schema und Projektdokumentation |
| JSON-API für Fragen umgesetzt und die zugehörige Architekturentscheidung dokumentiert | [API-Route und DD-08](https://github.com/AkayHWR/fswd-app-webpioniere/commit/abd1845), [DD-08 angelegt](https://github.com/AkayHWR/fswd-app-webpioniere/commit/ef7afb3) | Keine externen Quellen außer fswd-home und chatgpt |
| Architekturentscheidungen zu SQL/SQLite und Bootstrap dokumentiert | [DD-00: SQL oder SQLAlchemy](https://github.com/AkayHWR/fswd-app-webpioniere/commit/75f0f3f), [DD-01: Bootstrap oder eigenes CSS](https://github.com/AkayHWR/fswd-app-webpioniere/commit/386d997) | Keine externen Quellen außer fswd-home und chatgpt |

---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  | ChatGPT | Ideen für ein gemeinsames Basis-Template und ein einheitliches Standard-Styling der Anwendung | [`base.html`](../../templates/base.html), [`style.css`](../../static/css/style.css) | Erstellen eines base-templates, welches unseren Anforderungen entspricht. Ich habe mir einige Grundgerüste generieren lassen und mich für das schönste base-template enschieden. Eigene Überarbeitung hinsichtlich der Erweiterungen des Logouts. |
| 02  | ChatGPT | Unterstützung bei der Gestaltung und Strukturierung der Dashboard-Ansicht mit Suche, Tags und Fragekarten | [`dashboard.html`](../../templates/dashboard.html), [`style.css`](../../static/css/style.css) | Unterstützung bei der Umsetzung mit Buttons und das Aufteilen der Tags zu top_tags und other_tags. Grundsätzlich habe ich die "Bootstrap-Formalien" mir generieren lassen. Außerdem habe ich nach Lösungsvorschlägen für das Hinzufügen von Tags gefragt und mich für die beste Variante entschieden. Auch nach Methoden zum Erweitern/Anzeigen der other_tags gefragt. |
| 03  | ChatGPT | Unterstützung bei der Umsetzung der Hashtag-Ermittlung für das Dashboard | [`app.py` – `all_hashtags`](../../app.py#L21) | Nach Lösungsvorschlägen der Umsetzung des "Hashtag-Anzahl-Ermittelns" gefragt.  |
| 04  | ChatGPT | Abwägung einer separaten JSON-API gegenüber einer JSON-Ausgabe über bestehende HTML-Routen | [`app.py` – `api_questions`](../../app.py#L508), [DD-08](../design-decisions/dd-08.md) | Nach einer alternativen Möglichkeit zur fswd-home Methode gefragt. |

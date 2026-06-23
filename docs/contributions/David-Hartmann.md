---
title: David Hartmann
parent: Individual Contributions
nav_order: 1
---


# David Hartmann

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
Meine Python Kentnisse zu verbessern/festigen und eine interessante WebApp zu erstellen als auch zu verstehen wie diese aufgebaut ist und wie sie funktioniert


---

## Eidesstattliche Erklärung

**[David Hartmann, Matrikelnr.: 77208499611]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 |Die Umsetzung der Registrierungslogik und die dazugehörigen Eingabeprüfungen. Dazu gehören die Überprüfung der E-Mail-Adressen, die Prüfung auf bereits vorhandene Accounts sowie das automatische Einloggen nach der erfolgreichen Registrierung. | Ich bin auf diesen Beitrag stolz, da die Registrierung nicht nur neue Nutzerdaten speichert, sondern auch verschiedene mögliche Fehler erkennt und den Nutzern verständliche Rückmeldungen gibt. | Bei der Registrierung musste ich sicherstellen, dass ungültige Daten nicht gespeichert werden. Dabei war es wichtig, die E-Mail-Adressen mithilfe von `strip()` und `lower()` zu normalisieren und die eingegebenen Daten mit den bereits vorhandenen Benutzerdaten abzugleichen. Außerdem habe ich `cursor.lastrowid` verwendet, um nach der Registrierung die ID des neu erstellten Benutzers zu erhalten. |
| 2 | Die Umsetzung der Login- und Logout-Logik. Dazu gehören die Überprüfung der eingegebenen E-Mail-Adresse und des Passworts, das Speichern der Benutzerdaten in der Session sowie das Weiterleiten zum Dashboard nach einer erfolgreichen Anmeldung. | Ich bin auf diesen Beitrag stolz, da der Login eine wichtige Grundlage für weitere Funktionen der Anwendung bildet. Nur angemeldete Benutzer können beispielsweise neue Fragen erstellen oder Bewertungen abgeben. Durch die Logout-Funktion können die gespeicherten Session-Daten außerdem wieder vollständig entfernt werden. | Bei der Umsetzung musste ich verstehen, wie Daten aus der Datenbank abgefragt und mit den eingegebenen Anmeldedaten verglichen werden. Außerdem musste ich sicherstellen, dass bei einer falschen E-Mail-Adresse oder einem falschen Passwort eine verständliche Fehlermeldung angezeigt wird und bei einer erfolgreichen Anmeldung die richtige Benutzer-ID in der Session gespeichert wird. |
| 3 | Die Entscheidung, normale HTML-Formulare mit Flask `request.form` anstelle von Flask-WTF beziehungsweise WTForms zu verwenden. Dafür habe ich beide Möglichkeiten verglichen und die Vor- und Nachteile in einer Design Decision festgehalten. | Die Entscheidung hatte unmittelbaren Einfluss auf die gemeinsame Entwicklung, da sie eine einheitliche Grundlage für die Flask-Routen, die Formularverarbeitung und die HTML-Templates geschaffen hat. Dadurch konnten alle Formulare nach demselben Prinzip umgesetzt und leichter nachvollzogen werden. | Hier galt es, Einfachheit, Lernwert und Wartbarkeit abzuwägen. Flask-WTF hätte zwar zentrale Validierung und CSRF-Schutz geboten, gleichzeitig aber zusätzliche Abhängigkeiten, Konfiguration und komplexere Templates erfordert. Für die wenigen und vergleichsweise einfachen Formulare erschien die direkte Verarbeitung mit `request.form` deshalb geeigneter. |


## Design Decisions that I led

1. [DD #02](../design-decisions/dd-02.md)
2. [DD #03](../design-decisions/dd-03.md)
3. [DD #11](../design-decisions/dd-11.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Erstellung der persönlichen Projektdokumentation | [Persönliche Seite und Meta-Ziele](https://github.com/AkayHWR/fswd-app-webpioniere/commit/b82963a), [Erstellung der Target-Scope-Dokumentation](https://github.com/AkayHWR/fswd-app-webpioniere/commit/f827a8a) | Keine externen Quellen | 
| Bereinigung der Projekt- und Dokumentationsstruktur durch das Entfernen doppelter, nicht benötigter und technischer Dateien beziehungsweise Seiten | [Bereinigung des Repositorys](https://github.com/AkayHWR/fswd-app-webpioniere/commit/8074291), [Entfernung unnötiger `.todo`-Dateien](https://github.com/AkayHWR/fswd-app-webpioniere/commit/1b0916d), [Ausblenden einer Seite aus der Navigation](https://github.com/AkayHWR/fswd-app-webpioniere/commit/61cfc39) | keine externen Quellen | 
| Erstellung der ersten Routen für Registrierung und Login sowie Anbindung an die entsprechenden Templates | [Register- und Login-Routen](https://github.com/AkayHWR/fswd-app-webpioniere/commit/5d701bf), [Anbindung der Routen an die Templates](https://github.com/AkayHWR/fswd-app-webpioniere/commit/6b3e2b0) | Beispielcode des Dozenten und ChatGPT | 
| Dokumentation der Designentscheidungen zu Benutzernamen und Formularverarbeitung | [Design Decision DD-02](https://github.com/AkayHWR/fswd-app-webpioniere/commit/4bb3b88), [Korrektur der Listenformatierung](https://github.com/AkayHWR/fswd-app-webpioniere/commit/1543d52), [Design Decision DD-03](https://github.com/AkayHWR/fswd-app-webpioniere/commit/723c83f), [Korrektur der Autorenangabe](https://github.com/AkayHWR/fswd-app-webpioniere/commit/5b8ad41), [Aktualisierung von DD-03](https://github.com/AkayHWR/fswd-app-webpioniere/commit/af04a6d) | Projektvorgaben und ChatGPT |
| Dokumentation der offenen Entscheidung zur Verifizierung studentischer HWR-E-Mail-Adressen | [Design Decision DD-11](https://github.com/AkayHWR/fswd-app-webpioniere/commit/e8d22c1) | Vorhandene Registrierungslogik und ChatGPT |
| Umsetzung der Login-Funktion mit Datenbankabfrage, Prüfung der Zugangsdaten und Speicherung der Benutzerdaten in der Session | [Session-Import](https://github.com/AkayHWR/fswd-app-webpioniere/commit/f526276), [Login-Logik mit Datenbankprüfung und Session](https://github.com/AkayHWR/fswd-app-webpioniere/commit/8d534f1), [Login-Formular](https://github.com/AkayHWR/fswd-app-webpioniere/commit/bd9142b), [Secret Key für Sessions](https://github.com/AkayHWR/fswd-app-webpioniere/commit/95550c5) | fswd-home, Beispielcode des Dozenten und ChatGPT |
| Umsetzung der Logout-Funktion zum Löschen der gespeicherten Session-Daten und zur Weiterleitung zum Dashboard | [Logout-Funktion](https://github.com/AkayHWR/fswd-app-webpioniere/commit/8f85ab4) | Keine externen Quellen |
| Korrektur der E-Mail-Adressen in den Beispieldaten, damit sie mit der Login- und Registrierungslogik übereinstimmen | [Korrektur der Beispiel-E-Mail-Adressen](https://github.com/AkayHWR/fswd-app-webpioniere/commit/d897abd), [Entfernung eines Leerzeichens aus einer Beispiel-E-Mail-Adresse](https://github.com/AkayHWR/fswd-app-webpioniere/commit/3202707) | Keine externen Quellen |
| Erstellung einer Hilfsfunktion zur Prüfung studentischer HWR-E-Mail-Adressen | [HWR-E-Mail-Validierung](https://github.com/AkayHWR/fswd-app-webpioniere/commit/2c0ed24) | Keine externen Quellen | 
| Vereinheitlichung der Session-Schlüssel für die Anzeige des Benutzernamens nach Login und Registrierung | [Umbenennung von `full_name` zu `username`](https://github.com/AkayHWR/fswd-app-webpioniere/commit/5209dee) | Keine externen Quellen | 
| Umsetzung der Registrierungslogik mit Eingabeprüfungen, Prüfung auf bereits vorhandene Accounts und automatischem Login | [Registrierungslogik mit Validierung und automatischem Login](https://github.com/AkayHWR/fswd-app-webpioniere/commit/88ceaac), [Registrierungsformular](https://github.com/AkayHWR/fswd-app-webpioniere/commit/1230de5) | fswd-home, Beispielcode des Dozenten und ChatGPT | 
| Ausarbeitung der finalen Design Challenge und Erstellung des zugehörigen Raw Materials | [Design Challenge und Raw Material](https://github.com/AkayHWR/fswd-app-webpioniere/commit/06ae45f) | keine externen Quellen | 
| Dokumentation der Zielgruppen, Nutzerrollen und Kernprobleme sowie Erstellung des zugehörigen Raw Materials | [Target Users, Problems und Raw Material](https://github.com/AkayHWR/fswd-app-webpioniere/commit/dd96e6c) | keine externen Quellen | 
| Ergänzung der Startseite um eine kurze Projektbeschreibung und einen repräsentativen Screenshot der Web-App | [Projektbeschreibung und App-Screenshot](https://github.com/AkayHWR/fswd-app-webpioniere/commit/85f0bb7) | keine externen Quellen | 

---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01 | ChatGPT | Sprachliche Überarbeitung und Strukturierung von Entwürfen  | [DD-03](../design-decisions/dd-03.md), [DD-02](../design-decisions/dd-02.md) | ChatGPT wurde genutzt, um Formulierungen verständlicher zu gestalten und die Vor- und Nachteile übersichtlich zu strukturieren |
| 02 | ChatGPT | Unterstützung bei der Formulierung einer noch offenen Entscheidung zur Verifizierung von HWR-E-Mail-Adressen | [DD-11](../design-decisions/dd-11.md) | ChatGPT wurde genutzt um Formulierungen verständlicher zu gestalten und zur Beratung über möglichen Verfizierungs Optionen genutzt. |
| 03 | ChatGPT | Sprachliche Überarbeitung der persönlichen Beiträge zum Projekt | Abschnitt Top-3 Contributions, Abschnitt Contributions | Prüfung auf Rechtschreibung, Verständlichkeit und einheitliche Formulierungen. |
| 04 | ChatGPT | Unterstützung bei der automatischen Anmeldung nach der Registrierung | app.py – register() | Nach einer Möglichkeit gefragt, den neu registrierten Benutzer direkt einzuloggen.|
| 05 | ChatGPT | Beantwortung einzelner Fragen zur Verarbeitung von HTML-Formularen | app.py – login() und register(), login.html, register.html | Beantwortung einzelner Fragen zur Formular- und Session-Verarbeitung |


---
title: Masin hassan
parent: Individual Contributions
nav_order: 1
---


# Masin Hassan

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

Ich will meine Python-Skills im Backend vertiefen und fit im Umgang mit flask werden. Außerdem ist mir wichtig, den ganzen Prozess von der ersten Idee bis zum Deployment mal in der Praxis mitzumachen und dabei die Zusammenarbeit im Team über Git sicher zu beherschen

---

## Eidesstattliche Erklärung

**[Masin Hassan, Matrikelnr.: 77212022426]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Implementierung der Detailansicht für Fragen mit Antworten, Voting-System und Markierung der besten Antwort.|Die Detailansicht verbindet mehrere zentrale Funktionen der Anwendung: Nutzer können Fragen ansehen, Antworten erstellen, abstimmen und Lösungen markieren.|Die Herausforderung war, die verschiedenen Datenbankbeziehungen (Fragen, Antworten, Votes und User) korrekt mit Flask-Routen und Jinja-Templates zu verbinden.|
| 2 |Umsetzung der Antwort-Funktion inklusive Erstellung neuer Antworten, Anzeige von Antworten und Integration der Lösungsmarkierung.|Dadurch wurde die Anwendung von einer reinen Fragenübersicht zu einer interaktiven Plattform erweitert.|Besonders anspruchsvoll war die Verbindung zwischen Formularen, Datenbankoperationen und der Darstellung im Template.|
| 3 |Erstellung und Integration der question_detail.html in das bestehende Template-System.|Die Detailseite bietet eine konsistente Benutzeroberfläche und erweitert die vorhandene App um einen vollständigen Frage-Antwort-Workflow.|Die Herausforderung war, die neue Detailansicht in die vorhandene Struktur mit base.html, Jinja-Templates und Bootstrap-Komponenten einzubauen.|

## Design Decisions that I led

1. [DD #05](../design-decisions/dd-05.md)
2. [DD #06](../design-decisions/dd-06.md)
3. [DD #09](../design-decisions/dd-09.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
|Question Detail View mit Antworten und Template-Anbindung| [feat: add question detail page](https://github.com/AkayHWR/fswd-app-webpioniere/commit/127bf32), [feat: initialize question detail route and basic template inheritance](https://github.com/AkayHWR/fswd-app-webpioniere/commit/bce5e53)|Keine externen Quellen außer fswd-home und ChatGPT|
|Antwort-Erstellung in der Detailansicht|[feat: add answer creation to question detail view](https://github.com/AkayHWR/fswd-app-webpioniere/commit/2d6e832)|Keine externen Quellen außer fswd-home und ChatGPT|
|Voting-System für Fragen und Antworten|[Feat: add voting tables to database](https://github.com/AkayHWR/fswd-app-webpioniere/commit/f2ddad9), [feat: finalize question_detail.html, vote tables, sample votes, voting, and mark as solve](https://github.com/AkayHWR/fswd-app-webpioniere/commit/b0945a5)|Keine externen Quellen außer fswd-home und ChatGPT |
|Markierung einer Antwort als Lösung|[feat: finalize question_detail.html, vote tables, sample votes, voting, and mark as solve](https://github.com/AkayHWR/fswd-app-webpioniere/commit/b0945a5)|Keine externen Quellen außer fswd-home und ChatGPT |
|  |  |  |

---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
|01|ChatGPT|Unterstützung bei Strukturierung der question_detail.html| templates/question_detail.html| Nach Vorschlägen für Aufbau mit Bootstrap Cards, Buttons und Jinja-Schleifen gefragt und anschließend angepasst|
|02|ChatGPT|Unterstützung bei Flask-Routen und Datenbanklogik für Antworten und Votes|app.py|Unterstützung beim Finden von Fehlern bei Datenbankabfragen und Vote-Handling|
|03|ChatGPT|Die Herausforderung war, die neue Detailansicht in die vorhandene Struktur mit base.html, Jinja-Templates und Bootstrap-Komponenten einzubauen.| docs|Hilfe bei der Formulierungen, Inhalte selbst geprüft und angepasst.|

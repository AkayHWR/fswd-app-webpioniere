---
title: Value Proposition
nav_order: 1
---

{: .no_toc }
# Value Proposition

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

# Value Proposition

## The Problem

Viele Studierende haben Schwierigkeiten, bei konkreten fachlichen Problemen schnell und unkompliziert Hilfe zu finden, insbesondere in Fächern wie Programmierung, Mathematik oder Statistik. Gleichzeitig gibt es viele Studierende, die über entsprechendes Wissen verfügen und bereit wären zu helfen.

Bestehende Lösungen wie Foren, WhatsApp-Gruppen oder Lernplattformen sind oft unübersichtlich, langsam oder nicht auf spontane, konkrete Unterstützung ausgelegt. Es fehlt eine einfache, zentrale Plattform, die beide Seiten effizient miteinander verbindet.

## Our Solution

Unsere Anwendung **StudySwap** ist eine einfache Web-App, die Studierende mit Unterstützungsbedarf (Help Seeker) mit Studierenden verbindet, die Hilfe anbieten möchten (Helper).

Die App ermöglicht:
- das Erstellen von Hilfeanfragen
- das Durchsuchen bestehender Anfragen
- das Bewerben auf Anfragen als Helfer

Die Funktionalität ist bewusst einfach gehalten und entspricht genau dem Umfang der tatsächlich implementierten Anwendung.

## Target User(s)

**Primäre Zielgruppe:** Studierende

Wir unterscheiden zwei typische Nutzergruppen:

**1. Help Seeker (z. B. Anna, 22)**
- Studiert z. B. BWL oder Informatik
- Hat Schwierigkeiten bei bestimmten Themen (z. B. Datenbanken, Programmierung)
- Sucht schnelle, verständliche Hilfe

**2. Helper (z. B. Max, 24)**
- Fortgeschrittener Student mit guten Kenntnissen in bestimmten Fächern
- Möchte anderen helfen oder eigenes Wissen festigen
- Sucht eine einfache Möglichkeit, mit Hilfesuchenden in Kontakt zu treten

## Happy Path

Der „Happy Path“ beschreibt den typischen Ablauf innerhalb der App:

1. Nutzer öffnet die Web-App (Startseite)
2. Nutzer registriert sich oder loggt sich ein
3. Nutzer gelangt zum Dashboard
4. Nutzer erstellt eine Hilfeanfrage
   - *Eingabe von Titel, Beschreibung und Kategorie*
5. Ein anderer Nutzer durchsucht die Liste der Anfragen
6. Der zweite Nutzer wählt eine Anfrage aus
7. Der zweite Nutzer klickt auf „Helfen“
8. Verbindung zwischen Hilfesuchendem und Helfer entsteht

Dieser Ablauf zeigt klar die Funktionsweise der zweiseitigen Plattform, bei der zwei Nutzergruppen aktiv miteinander interagieren.

---

## Target Scope

Die Anwendung umfasst folgende UI-Screens:

**1. Login / Registrierungsseite**
- Eingabefelder für Benutzername und Passwort
- Button zum Einloggen oder Registrieren

**2. Dashboard**
- Übersicht aller Hilfeanfragen
- Navigation zum Erstellen einer neuen Anfrage

**3. Anfrage erstellen**
- Formular mit: Titel, Beschreibung, Kategorie
- Submit-Button

**4. Anfragen durchsuchen**
- Liste aller Anfragen
- Anzeige von Titel und Kurzbeschreibung
- Button: „Helfen“

**5. Detailansicht einer Anfrage**
- Vollständige Beschreibung
- Button zum Bewerben als Helfer

Die Screens sind bewusst einfach gehalten und entsprechen genau der geplanten und umsetzbaren Funktionalität der Web-App.
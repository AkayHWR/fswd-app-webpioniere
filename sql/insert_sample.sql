INSERT INTO user (email, first_name, last_name, password) VALUES
('anna@stud.hwr-berlin.de ', 'Anna', 'Schmidt', 'passwort'),
('max@stud.hwr-berlin.de', 'Max', 'Mueller', 'passwort'),
('julia@stud.hwr-berlin.de', 'Julia', 'Fischer', 'passwort'),
('tobias@stud.hwr-berlin.de', 'Tobias', 'Weber', 'passwort'),
('sara@stud.hwr-berlin.de', 'Sara', 'Klein', 'passwort');

INSERT INTO question (user_id, title, description, hashtags, upvotes, downvotes) VALUES
(1, 'Welche Vertiefung lohnt sich?', 'Ich bin unsicher, welche Vertiefung am besten passt.', '#Vertiefung #Studium', 2, 0),
(2, 'Wie lernt ihr fuer Mathe?', 'Welche Lernmethode hilft euch vor der Klausur?', '#Mathe #Klausur #Lernen', 1, 0),
(3, 'Bachelorarbeit im Unternehmen?', 'Hat jemand Erfahrung mit einer externen Bachelorarbeit?', '#Bachelorarbeit #Unternehmen', 1, 1),
(4, 'Gute Wahlpflichtmodule?', 'Welche Module sind interessant und fair bewertet?', '#Module #Studium', 0, 0),
(1, 'Tipps fuer Praxissemester', 'Worauf sollte man bei Bewerbungen achten?', '#Praxissemester #Bewerbung', 3, 0),
(2, 'Englische Literatur finden', 'Wo findet ihr gute wissenschaftliche Quellen?', '#Literatur #Hausarbeit', 0, 0),
(3, 'Pruefungsangst vor Statistik', 'Was hilft euch kurz vor der Statistikpruefung?', '#Statistik #Klausur #Lernen', 1, 0),
(4, 'Nebenjob neben Vollzeitstudium?', 'Wie viele Stunden sind realistisch?', '#Nebenjob #Studium', 2, 1),
(5, 'Wo findet man gute Gruppen?', 'Ich suche Leute fuer Lerngruppen vor den Pruefungen.', '#Lerngruppe #Klausur #Studium', 1, 0);

INSERT INTO answer (question_id, user_id, content, is_solution, upvotes, downvotes) VALUES
(1, 2, 'Ich fand Finance gut, weil die Beispiele sehr praktisch waren.', 0, 2, 0),
(1, 3, 'Marketing war bei mir gut machbar und spannend.', 0, 1, 1),
(2, 1, 'Alte Klausuren rechnen und danach die Fehlerliste wiederholen.', 1, 1, 0),
(3, 2, 'Ich habe meine Bachelorarbeit im Unternehmen geschrieben. Planung ist wichtig.', 1, 2, 0),
(4, 1, 'Projektmanagement war fair und gut organisiert.', 0, 0, 0);

INSERT INTO question_vote (question_id, user_id, vote) VALUES
(1, 2, 1),
(1, 3, 1),
(2, 1, 1),
(3, 1, 1),
(3, 2, -1),
(5, 2, 1),
(5, 3, 1),
(5, 4, 1),
(7, 1, 1),
(8, 1, 1),
(8, 2, 1),
(8, 3, -1);

INSERT INTO answer_vote (answer_id, user_id, vote) VALUES
(1, 1, 1),
(1, 3, 1),
(2, 1, 1),
(2, 2, -1),
(3, 2, 1),
(4, 1, 1),
(4, 3, 1);
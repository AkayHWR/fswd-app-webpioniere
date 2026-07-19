INSERT INTO user (email, first_name, last_name, password) VALUES
('anna@stud.hwr-berlin.de', 'Anna', 'Schmidt', 'scrypt:32768:8:1$MNYzYVsmljf8TTMx$df034b3c274a71dff52869dcbeee480896350649b2e548ea9b83181a8d126345cd7dd2fb4da5e0355ce6ccb76561b9cf601a9d57202d2f8d3fcde7a4bb388264'),
('max@stud.hwr-berlin.de', 'Max', 'Mueller', 'scrypt:32768:8:1$49bmxGZzweJzzqnB$d768091e3bc44d9238e98ca312f69069a72cbe636afcbb2a0a168d70df30e45c0fe0ea6962f0e0fbc1b56e30a5a3adf75b4302c7b2c4abc6ac818cb5d606e11c'),
('julia@stud.hwr-berlin.de', 'Julia', 'Fischer', 'scrypt:32768:8:1$GnQNaErRMYTRJP7T$699699f21b36e582606b9a09f7d53466815d9138be18455e9eb68e711d8c8d8f78e3dbf7318ac972e0f2dd78cf1a609b3c0a211207f83cbe6c4df828399f2905'),
('tobias@stud.hwr-berlin.de', 'Tobias', 'Weber', 'scrypt:32768:8:1$mFzcTe289CBtLAgQ$707ce8eb7f51912995e44d498f857166698a42a13795f1469f038b251525ffe99e58cf669dbce81c4c62ed09d0d8aaa178e00c801ce2bf85ad6a25360b2e75b8'),
('sara@stud.hwr-berlin.de', 'Sara', 'Klein', 'scrypt:32768:8:1$QgmexJ6gqMIvmAHs$a284e8b5f80f9cb721cdfc46d70399b6ab7a2610a42d1d366b1f05d18701234beaa46729ad706f2664ee725c243c382ac1200160a1e7ea910e3c313dc0d0ca54');

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

INSERT INTO saved_question (user_id, question_id) VALUES
(1, 2),
(1, 3),
(2, 1),
(3, 7);

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
-- CHAPTER 8
CREATE TABLE 'mood' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'label' TEXT NOT NULL
);

CREATE TABLE 'entries' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'concept' TEXT NOT NULL,
    'entry' TEXT NOT NULL,
    'date' TEXT NOT NULL,
    'mood_id' INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `mood`(`id`)
);

-- CHAPTER 9
INSERT INTO 'mood' VALUES (null, "Happy");
INSERT INTO 'mood' VALUES (null, "Sad");
INSERT INTO 'mood' VALUES (null, "Angry");
INSERT INTO 'mood' VALUES (null, "OK");

INSERT INTO 'entries' VALUES (null, "JavaScript", "I learned about loops today. They can be a lot of fun.", "Wed Sep 15 2021 10:10:47", 1);
INSERT INTO 'entries' VALUES (null, "Python", "Python is named after the Monty Python comedy group from the UK.", "Wed Sep 15 2021 10:11:33", 4);
INSERT INTO 'entries' VALUES (null, "Python", "Why did it take so long for python to have a switch statement? It's much cleaner than if/elif blocks", "Wed Sep 15 2021 10:13:11", 3);
INSERT INTO 'entries' VALUES (null, "JavaScript", "Dealing with Date is terrible. Why do you have to add an entire package just to format a date. It makes no sense.", "Wed Sep 15 2021 10:14:05", 3);
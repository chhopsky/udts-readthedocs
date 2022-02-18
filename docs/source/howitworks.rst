############
How it works
############

Update the Stream (UDTS) uses your input about teams, matches, and scores to build .txt and .png files you can use with your stream. This lets you build scenes with elements that automatically update as you register scores and progress through a tournament --- eliminating the need to manually edit overlays while streaming.

UDTS also lets you import tournament information directly from Challonge and FACEIT.

************************
The /streamlabels folder
************************

When UDTS creates or updates .txt and .png files, it puts them in the **/streamlabels** folder.

These files automatically update when you record a win in UDTS.

File name components (keywords) indicate the type of information that a file contains.

+------------+-------------------------------------------------+----------------------------------+
| Keyword    | Significance                                    | Example                          |
+============+=================================================+==================================+
| current    | Related to current match                        | **current**-match-team2-name.txt |
+------------+-------------------------------------------------+----------------------------------+
| last       | Related to previous match                       | **last**-match.txt               |
+------------+-------------------------------------------------+----------------------------------+
| match      | Match information                               | **match**-1-scores.txt           |
+------------+-------------------------------------------------+----------------------------------+
| team(s)    | Team information                                | schedule-**teams**.txt           |
+------------+-------------------------------------------------+----------------------------------+
| team1      | Team currently in the Team 1 (red) position     | match-1-**team1**-icon.png       |
+------------+-------------------------------------------------+----------------------------------+
| team2      | Team currently in the Team 2 (blue) position    | current-match-**team2**-hero.png |
+------------+-------------------------------------------------+----------------------------------+
| score(s)   | Score (match)                                   | match-2-**scores**.txt           |
+------------+-------------------------------------------------+----------------------------------+
| point(s)   | Score (tournament)                              | standings-teams-**points**.txt   |
+------------+-------------------------------------------------+----------------------------------+
| name(s)    | Team full name                                  | standing-teams-**names**.txt     |
+------------+-------------------------------------------------+----------------------------------+
| tricode(s) | Team three-letter tricode                       | current-match-**tricodes**.txt   |
+------------+-------------------------------------------------+----------------------------------+
| icon       | Icon image                                      | match-4-team2-**icon**.png       |
+------------+-------------------------------------------------+----------------------------------+
| hero       | Hero image                                      | match-3-team1-**hero**.png       |
+------------+-------------------------------------------------+----------------------------------+
| horizontal | Horizontal text placement (default is vertical) | match-3-teams-**horizontal**.txt |
+------------+-------------------------------------------------+----------------------------------+
| schedule   | Schedule information                            | **schedule**-scores.txt          |
+------------+-------------------------------------------------+----------------------------------+
| standings  | Standings information                           | **standings**-teams-leader.txt   |
+------------+-------------------------------------------------+----------------------------------+
| complete   | Tournament overview (names, scores)             | standings-**complete**.txt       |
+------------+-------------------------------------------------+----------------------------------+
| combined   | All information of a particular type            | schedule-teams-**combined**.txt  |
+------------+-------------------------------------------------+----------------------------------+
| leader     | Team currently in the lead                      | standings-teams-**leader**.txt   |
+------------+-------------------------------------------------+----------------------------------+
-- SQL script to create and populate the 4 tables used for the Baseball activity with joins.
-- 4 Tables: postion, team, player, coach


-- 'Create and populate the Position table';
DROP TABLE IF EXISTS Position CASCADE;

CREATE TABLE Position (
  posnum SERIAL PRIMARY KEY,
  title TEXT
);
INSERT INTO Position VALUES(1,'Pitcher');
INSERT INTO Position VALUES(2,'Catcher');
INSERT INTO Position VALUES(3,'First Baseman');
INSERT INTO Position VALUES(4,'Second Baseman');
INSERT INTO Position VALUES(5,'Third Baseman');
INSERT INTO Position VALUES(6,'Shortstop');
INSERT INTO Position VALUES(7,'Left Fielder');
INSERT INTO Position VALUES(8,'Center Fielder');
INSERT INTO Position VALUES(9,'Right Fielder');
INSERT INTO Position VALUES(10,'Designated Hitter');

-- 'Create and populate the Team table';
DROP TABLE IF EXISTS Team CASCADE ;

CREATE TABLE Team (
  name TEXT PRIMARY KEY,
  city TEXT,
  ballpark TEXT
) ;
INSERT INTO Team VALUES ('Orioles','Baltimore','Camden Yards');
INSERT INTO Team VALUES ('Red Sox','Boston','Fenway Park');
INSERT INTO Team VALUES ('Blue Jays','Toronto','Rogers Centre');
INSERT INTO Team VALUES ('Yankees','New York','Yankee Stadium');
INSERT INTO Team VALUES ('Rays','Tampa Bay','Tropicana Field');

-- 'Create and populate the Coach table';
DROP TABLE IF EXISTS Coach ;

CREATE TABLE Coach (
  number INTEGER,
  name TEXT PRIMARY KEY, --Key doesn't have to be integer.  Just needs to be unique
  title TEXT,
  team TEXT REFERENCES Team(name)
) ;

INSERT INTO Coach VALUES (53,'John Farrell','Manager','Red Sox');
INSERT INTO Coach VALUES (44,'Chili Davis','Hitting Coach','Red Sox');
INSERT INTO Coach VALUES (57,'Victor Rodriguez','Assistant Hitting Coach','Red Sox');
INSERT INTO Coach VALUES (47,'Juan Nieves','Pitching Coach','Red Sox');
INSERT INTO Coach VALUES (43,'Arnie Beyeler','First Base Coach','Red Sox');
INSERT INTO Coach VALUES (55,'Brian Butterfield','Third Base Coach','Red Sox');
INSERT INTO Coach VALUES (17,'Torey Lovullo','Bench Coach','Red Sox');
INSERT INTO Coach VALUES (58,'Dana LeVangie','Bullpen Coach','Red Sox');
INSERT INTO Coach VALUES (26,'Buck Showalter','Manager','Orioles');
INSERT INTO Coach VALUES (47,'Scott Coolbaugh','Hitting Coach','Orioles');
INSERT INTO Coach VALUES (55,'Einar Diaz','Assistant Hitting Coach','Orioles');
INSERT INTO Coach VALUES (37,'Dave Wallace','Pitching Coach','Orioles');
INSERT INTO Coach VALUES (24,'Wayne Kirby','First Base Coach','Orioles');
INSERT INTO Coach VALUES (11,'Bobby Dickerson','Third Base Coach','Orioles');
INSERT INTO Coach VALUES (77,'John Russell','Bench Coach','Orioles');
INSERT INTO Coach VALUES (54,'Dom Chiti','Bullpen Coach','Orioles');
INSERT INTO Coach VALUES (28,'Joe Girardi','Manager','Yankees');
INSERT INTO Coach VALUES (61,'Jeff Pentland','Hitting Coach','Yankees');
INSERT INTO Coach VALUES (62,'Alan Cockrell','Assistant Hitting Coach','Yankees');
INSERT INTO Coach VALUES (58,'Larry Rothschild','Pitching Coach','Yankees');
INSERT INTO Coach VALUES (56,'Tony Pena','First Base Coach','Yankees');
INSERT INTO Coach VALUES (54,'Joe Espada','Third Base Coach','Yankees');
INSERT INTO Coach VALUES (59,'Rob Thomson','Bench Coach','Yankees');
INSERT INTO Coach VALUES (60,'Gary Tuck','Bullpen Coach','Yankees');
INSERT INTO Coach VALUES (88,'Roman Rodriguez','Bullpen Catcher','Yankees');
INSERT INTO Coach VALUES (16,'Kevin Cash','Manager','Rays');
INSERT INTO Coach VALUES (17,'Derek Shelton','Hitting Coach','Rays');
INSERT INTO Coach VALUES (48,'Jim Hickey','Pitching Coach','Rays');
INSERT INTO Coach VALUES (15,'Rocco Baldelli','First Base Coach','Rays');
INSERT INTO Coach VALUES (24,'Charlie Montoyo','Third Base Coach','Rays');
INSERT INTO Coach VALUES (6,'Tom Foley','Bench Coach','Rays');
INSERT INTO Coach VALUES (41,'Stan Boroski','Bullpen Coach','Rays');
INSERT INTO Coach VALUES (4,'Jamie Nelson','Major League Coach','Rays');
INSERT INTO Coach VALUES (77,'Scott Cursi','Bullpen Catcher','Rays');
INSERT INTO Coach VALUES (5,'John Gibbons','Manager','Blue Jays');
INSERT INTO Coach VALUES (26,'Brook Jacoby','Hitting Coach','Blue Jays');
INSERT INTO Coach VALUES (60,'Eric Owens','Assistant Hitting Coach','Blue Jays');
INSERT INTO Coach VALUES (40,'Pete Walker','Pitching Coach','Blue Jays');
INSERT INTO Coach VALUES (34,'Tim Leiper','First Base Coach','Blue Jays');
INSERT INTO Coach VALUES (2,'Luis Rivera','Third Base Coach','Blue Jays');
INSERT INTO Coach VALUES (16,'DeMarlo Hale','Bench Coach','Blue Jays');
INSERT INTO Coach VALUES (38,'Dane Johnson','Bullpen Coach','Blue Jays');
INSERT INTO Coach VALUES (61,'Alex Andreopoulos','Bullpen Catcher','Blue Jays');

-- 'Create and populate the Player table';
DROP TABLE IF EXISTS Player ;

CREATE TABLE Player(
  name TEXT,
  position INTEGER REFERENCES Position(posnum),
  number INTEGER,
  team TEXT REFERENCES Team(name),
  age INTEGER,
  PRIMARY KEY(team, number) -- combination key
) ;
INSERT INTO Player VALUES ('Craig Breslow',1,32,'Red Sox',34);
INSERT INTO Player VALUES ('Clay Buchholz',1,11,'Red Sox',30);
INSERT INTO Player VALUES ('Joe Kelly',1,56,'Red Sox',26);
INSERT INTO Player VALUES ('Justin Masterson',1,63,'Red Sox',30);
INSERT INTO Player VALUES ('Wade Miley',1,20,'Red Sox',28);
INSERT INTO Player VALUES ('Edward Mujica',1,54,'Red Sox',30);
INSERT INTO Player VALUES ('Alexi Ogando',1,41,'Red Sox',31);
INSERT INTO Player VALUES ('Rick Porcello',1,22,'Red Sox',26);
INSERT INTO Player VALUES ('Robbie Ross Jr.',1,28,'Red Sox',25);
INSERT INTO Player VALUES ('Junichi Tazawa',1,36,'Red Sox',28);
INSERT INTO Player VALUES ('Koji Uehara',1,19,'Red Sox',40);
INSERT INTO Player VALUES ('Anthony Varvaro',1,46,'Red Sox',30);
INSERT INTO Player VALUES ('Ryan Hanigan',2,10,'Red Sox',34);
INSERT INTO Player VALUES ('Sandy Leon',2,3,'Red Sox',26);
INSERT INTO Player VALUES ('Xander Bogaerts',6,2,'Red Sox',22);
INSERT INTO Player VALUES ('Brock Holt',5,26,'Red Sox',26);
INSERT INTO Player VALUES ('Mike Napoli',3,12,'Red Sox',33);
INSERT INTO Player VALUES ('Dustin Pedroia',4,15,'Red Sox',31);
INSERT INTO Player VALUES ('Pablo Sandoval',5,48,'Red Sox',28);
INSERT INTO Player VALUES ('Mookie Betts',7,50,'Red Sox',22);
INSERT INTO Player VALUES ('Jackie Bradley Jr.',8,25,'Red Sox',24);
INSERT INTO Player VALUES ('Allen Craig',9,5,'Red Sox',30);
INSERT INTO Player VALUES ('Daniel Nava',9,29,'Red Sox',32);
INSERT INTO Player VALUES ('Hanley Ramirez',7,13,'Red Sox',31);
INSERT INTO Player VALUES ('David Ortiz',10,34,'Red Sox',39);
INSERT INTO Player VALUES ('Brad Brach',1,35,'Orioles',28);
INSERT INTO Player VALUES ('Zach Britton',1,53,'Orioles',27);
INSERT INTO Player VALUES ('Wei-Yin Chen',1,16,'Orioles',30);
INSERT INTO Player VALUES ('Jason Garcia',1,61,'Orioles',22);
INSERT INTO Player VALUES ('Kevin Gausman',1,39,'Orioles',24);
INSERT INTO Player VALUES ('Miguel Gonzalez',1,50,'Orioles',31);
INSERT INTO Player VALUES ('Tommy Hunter',1,29,'Orioles',29);
INSERT INTO Player VALUES ('Ubaldo Jimenez',1,31,'Orioles',31);
INSERT INTO Player VALUES ('Brian Matusz',1,17,'Orioles',28);
INSERT INTO Player VALUES ('Bud Norris',1,25,'Orioles',30);
INSERT INTO Player VALUES ('Darren ODay',1,56,'Orioles',33);
INSERT INTO Player VALUES ('Chris Tillman',1,30,'Orioles',27);
INSERT INTO Player VALUES ('Caleb Joseph',2,36,'Orioles',28);
INSERT INTO Player VALUES ('Ryan Lavarnway',2,34,'Orioles',27);
INSERT INTO Player VALUES ('Everth Cabrera',6,1,'Orioles',28);
INSERT INTO Player VALUES ('Chris Davis',3,19,'Orioles',29);
INSERT INTO Player VALUES ('Manny Machado',5,13,'Orioles',22);
INSERT INTO Player VALUES ('Rey Navarro',6,43,'Orioles',25);
INSERT INTO Player VALUES ('Jimmy Paredes',5,38,'Orioles',26);
INSERT INTO Player VALUES ('Alejandro De Aza',7,12,'Orioles',30);
INSERT INTO Player VALUES ('Adam Jones',8,10,'Orioles',29);
INSERT INTO Player VALUES ('David Lough',7,9,'Orioles',29);
INSERT INTO Player VALUES ('Steve Pearce',7,28,'Orioles',31);
INSERT INTO Player VALUES ('Travis Snider',9,23,'Orioles',27);
INSERT INTO Player VALUES ('Delmon Young',9,27,'Orioles',29);
INSERT INTO Player VALUES ('Dellin Betances',1,68,'Yankees',27);
INSERT INTO Player VALUES ('David Carpenter',1,29,'Yankees',29);
INSERT INTO Player VALUES ('Nathan Eovaldi',1,30,'Yankees',25);
INSERT INTO Player VALUES ('Chris Martin',1,57,'Yankees',28);
INSERT INTO Player VALUES ('Andrew Miller',1,48,'Yankees',29);
INSERT INTO Player VALUES ('Michael Pineda',1,35,'Yankees',26);
INSERT INTO Player VALUES ('Esmil Rogers',1,53,'Yankees',29);
INSERT INTO Player VALUES ('CC Sabathia',1,52,'Yankees',34);
INSERT INTO Player VALUES ('Chasen Shreve',1,45,'Yankees',24);
INSERT INTO Player VALUES ('Masahiro Tanaka',1,19,'Yankees',26);
INSERT INTO Player VALUES ('Adam Warren',1,43,'Yankees',27);
INSERT INTO Player VALUES ('Chase Whitley',1,39,'Yankees',25);
INSERT INTO Player VALUES ('Justin Wilson',1,41,'Yankees',27);
INSERT INTO Player VALUES ('Brian McCann',2,34,'Yankees',31);
INSERT INTO Player VALUES ('John Ryan Murphy',2,66,'Yankees',23);
INSERT INTO Player VALUES ('Alex Rodriguez',5,13,'Yankees',39);
INSERT INTO Player VALUES ('Brett Gardner',7,11,'Yankees',31);
INSERT INTO Player VALUES ('Carlos Beltran',9,36,'Yankees',37);
INSERT INTO Player VALUES ('Chase Headley',5,12,'Yankees',30);
INSERT INTO Player VALUES ('Chris Young',7,24,'Yankees',31);
INSERT INTO Player VALUES ('Didi Gregorius',6,18,'Yankees',25);
INSERT INTO Player VALUES ('Garrett Jones',3,33,'Yankees',33);
INSERT INTO Player VALUES ('Jacoby Ellsbury',8,22,'Yankees',31);
INSERT INTO Player VALUES ('Mark Teixeira',3,25,'Yankees',34);
INSERT INTO Player VALUES ('Stephen Drew',4,14,'Yankees',32);
INSERT INTO Player VALUES ('Mark Buehrle',1,56,'Blue Jays',36);
INSERT INTO Player VALUES ('Miguel Castro',1,51,'Blue Jays',20);
INSERT INTO Player VALUES ('Brett Cecil',1,27,'Blue Jays',28);
INSERT INTO Player VALUES ('R.A. Dickey',1,43,'Blue Jays',40);
INSERT INTO Player VALUES ('Marco Estrada',1,25,'Blue Jays',31);
INSERT INTO Player VALUES ('Jeff Francis',1,35,'Blue Jays',34);
INSERT INTO Player VALUES ('Liam Hendriks',1,31,'Blue Jays',26);
INSERT INTO Player VALUES ('Drew Hutchison',1,36,'Blue Jays',24);
INSERT INTO Player VALUES ('Aaron Loup',1,62,'Blue Jays',27);
INSERT INTO Player VALUES ('Daniel Norris',1,32,'Blue Jays',21);
INSERT INTO Player VALUES ('Roberto Osuna',1,54,'Blue Jays',20);
INSERT INTO Player VALUES ('Aaron Sanchez',1,41,'Blue Jays',22);
INSERT INTO Player VALUES ('Russell Martin',2,55,'Blue Jays',32);
INSERT INTO Player VALUES ('Josh Thole',2,22,'Blue Jays',28);
INSERT INTO Player VALUES ('Jonathan Diaz',6,1,'Blue Jays',29);
INSERT INTO Player VALUES ('Josh Donaldson',5,20,'Blue Jays',29);
INSERT INTO Player VALUES ('Edwin Encarnacion',3,10,'Blue Jays',32);
INSERT INTO Player VALUES ('Ryan Goins',4,17,'Blue Jays',27);
INSERT INTO Player VALUES ('Justin Smoak',3,14,'Blue Jays',28);
INSERT INTO Player VALUES ('Devon Travis',4,29,'Blue Jays',24);
INSERT INTO Player VALUES ('Danny Valencia',5,23,'Blue Jays',30);
INSERT INTO Player VALUES ('Jose Bautista',9,19,'Blue Jays',34);
INSERT INTO Player VALUES ('Kevin Pillar',7,11,'Blue Jays',26);
INSERT INTO Player VALUES ('Dalton Pompey',8,45,'Blue Jays',22);
INSERT INTO Player VALUES ('Michael Saunders',9,21,'Blue Jays',28);
INSERT INTO Player VALUES ('Matt Andriese',1,35,'Rays',25);
INSERT INTO Player VALUES ('Chris Archer',1,22,'Rays',26);
INSERT INTO Player VALUES ('Brad Boxberger',1,26,'Rays',26);
INSERT INTO Player VALUES ('Xavier Cedeno',1,31,'Rays',28);
INSERT INTO Player VALUES ('Ernesto Frieri',1,43,'Rays',29);
INSERT INTO Player VALUES ('Steve Geltz',1,54,'Rays',27);
INSERT INTO Player VALUES ('Brandon Gomes',1,47,'Rays',30);
INSERT INTO Player VALUES ('Kevin Jepsen',1,40,'Rays',30);
INSERT INTO Player VALUES ('Nathan Karns',1,51,'Rays',27);
INSERT INTO Player VALUES ('Jake Odorizzi',1,23,'Rays',25);
INSERT INTO Player VALUES ('Erasmo Ramirez',1,30,'Rays',24);
INSERT INTO Player VALUES ('Drew Smyly',1,33,'Rays',25);
INSERT INTO Player VALUES ('Rene Rivera',2,44,'Rays',31);
INSERT INTO Player VALUES ('Bobby Wilson',2,46,'Rays',31);
INSERT INTO Player VALUES ('Tim Beckham',4,1,'Rays',25);
INSERT INTO Player VALUES ('Asdrubal Cabrera',6,13,'Rays',29);
INSERT INTO Player VALUES ('Jake Elmore',6,10,'Rays',27);
INSERT INTO Player VALUES ('Logan Forsythe',4,11,'Rays',28);
INSERT INTO Player VALUES ('James Loney',3,21,'Rays',30);
INSERT INTO Player VALUES ('Evan Longoria',5,3,'Rays',29);
INSERT INTO Player VALUES ('David DeJesus',7,7,'Rays',35);
INSERT INTO Player VALUES ('Brandon Guyer',7,5,'Rays',29);
INSERT INTO Player VALUES ('Desmond Jennings',8,8,'Rays',28);
INSERT INTO Player VALUES ('Kevin Kiermaier',9,39,'Rays',24);
INSERT INTO Player VALUES ('Steven Souza  Jr.',9,20,'Rays',25);

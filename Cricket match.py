import random
Team =["India","Srilanka","Australia", "West indies","Pakistan", "New zealand","Southafrica","Bangladesh", "Afghanisthan","Ireland"]
Venue =["Mumbai","delhi","kolkata","Ahemdabad","CHennai","Banglore"]
Random_venue = random.choice(Venue)
Random_team1 = random.choice(Team)
Random_team2 = random.choice(Team)
print(Team)
print(Venue)
print(f"Match will be played between {Random_team1} and {Random_team2} at {Random_venue}")
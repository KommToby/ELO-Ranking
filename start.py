import json
import os
import database
from elosports.elo import Elo

db = database.Database()

beatmaps = db.get_beatmaps()
matchups = db.get_matchups()
beatmap_dict = {}
# Initial ELO values
eloleague = Elo(k=8, homefield=0)
for beatmap in beatmaps:
    beatmap_dict[beatmap[0]] = int(round(float(beatmap[1])*100, 2))
    eloleague.addPlayer(beatmap[0], rating=beatmap_dict[beatmap[0]])

# Matchup data
for i in range(0, len(matchups), 2):
    if matchups[i][3] == '1': # Win
        eloleague.gameOver(winner=matchups[i][1], loser = matchups[i][2], winnerHome=False)
    elif matchups[i][3] == '2': # Loss
        eloleague.gameOver(winner=matchups[i][2], loser = matchups[i][1], winnerHome=False)
    elif matchups[i][3] == '0': # Tie
        pass

# Creating the txt and writing the values
with open('elo_values.txt', 'w') as f:
    for beatmap in beatmaps:
        f.write(f"**{beatmap[0]}:** {beatmap[1]} -> {round(eloleague.ratingDict[beatmap[0]]/100, 2)} : {beatmap[6]} - {beatmap[7]} [{beatmap[8]}]\n")

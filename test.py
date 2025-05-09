from reads import *
from data import config
import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
]

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

spells = getCellValues("https://docs.google.com/spreadsheets/d/1Dl4t-zvwtnFxOUM0fclp3Q6bhfdHhzbIOymJ8369ivI/edit?gid=798829916#gid=798829916", config.COMBAT_SHEET.value, config.SPELLS.value, client)

# clear all empty strings in lists of lists
for i in range(len(spells)):
    spells[i] = [x for x in spells[i] if x != ""]

# remove all empty lists
spells = [x for x in spells if x != []]

spellNotes = getCellNotes("https://docs.google.com/spreadsheets/d/1Dl4t-zvwtnFxOUM0fclp3Q6bhfdHhzbIOymJ8369ivI/edit?gid=798829916#gid=798829916", config.COMBAT_SHEET.value, "H24:H132", client)

# remove all empty lists
spellNotes = [x for x in spellNotes if x != []]

# clear all strings in lists of lists that contain "H24:H132"
for i in range(len(spellNotes)):
    spellNotes[i] = [x for x in spellNotes[i] if x != "H24:H132"]

for idx, spell in enumerate(spells):
    if len(spell) > 6:
        print(f"Name: {spell[1]}")
        if (spell[0] == "C"):
            print("Level: Cantrip")
        else:
            print(f"Level: {spell[0]}")
        print(f"{spellNotes[idx][0]}")

        print("\n\n")
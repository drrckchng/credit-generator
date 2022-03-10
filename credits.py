import pandas as pd
import numpy as np

series = input("Enter series title: ")
season = input("Enter season: ")

with open('excel_path.txt', 'r') as f :
	excel_file_path = f.read()

df_excel = pd.read_excel(excel_file_path)
df_excel.to_csv(r"csv\credits.csv", index=None, header=True)
df = pd.DataFrame(pd.read_csv(r"csv\credits.csv", low_memory=False))
season_match = df[df['Season'] == int(season)].reset_index(drop=True)
row_match = season_match[season_match['Series'].str.match(series)].reset_index(drop=True)
cols = ['Season', 'Episode']
row_match[cols] = row_match[cols].astype(int)
row_match = row_match.fillna("N/A")
txt_file = open(r"credits_txt\credits_"+ series + season + ".txt", "w")
txt_file.write(series + " Season " + str(row_match.iloc[0]['Season']) + "\n \n")

for x in row_match.index:
	episodeCredits = [
		"Episode " + str(row_match.iloc[x]['Episode']),
		"Screenwriter - " + str(row_match.iloc[x]['Screenwriter']),
		"Story Editor - " + str(row_match.iloc[x]['Editor']),
		"Story Producer - " + str(row_match.iloc[x]['Story_Producer']),
		"Translator - " + str(row_match.iloc[x]['Translator']),
		"Editor in Chief - " + str(row_match.iloc[x]['Editor_in_Chief']),
		"Music Producer - " + str(row_match.iloc[x]['Music_Producer']),
		"Lyricist - " + str(row_match.iloc[x]['Lyricist']),
		"Topliner - " + str(row_match.iloc[x]['Topliner']),
		"Rapper - " + str(row_match.iloc[x]['Rapper']),
		"Vocalist - " + str(row_match.iloc[x]['Vocalist']),
		"Voice Actor - " + str(row_match.iloc[x]['Voice_Actor']),
		"Mixing & Mastering - " + str(row_match.iloc[x]['Mix_Master']),
		"Producer - " + str(row_match.iloc[x]['Producer']),
		"Production Manager - " + str(row_match.iloc[x]['Pro_Manager']),
		"Concept Designer - " + str(row_match.iloc[x]['Concept_Design']),
		"Storyboarder - " + str(row_match.iloc[x]['Storyboard']),
		"Asset Designer - " + str(row_match.iloc[x]['Asset_Design']),
		"Animator - " + str(row_match.iloc[x]['Animator']),
		"Video Editor - " + str(row_match.iloc[x]['Video_Editor']),
		"Post Production - " + str(row_match.iloc[x]['Post_Production']),
		"Thumbnail Designer - " + str(row_match.iloc[x]['Thumbnail']),
		"CCO - " + str(row_match.iloc[x]['CCO'] + "\n")
	]

	for i in episodeCredits:
		if i[-3:] != "N/A":
			txt_file.write(i + "\n")

end_text = input("enter to exit")

import UIManager


score = 0
highscore = 0


def add_score(points):
	global score
	score += points
	UIManager.update_score_ui(score)

def try_update_highscore():
	global score, highscore
	if score >= highscore:
		highscore = score
		UIManager.update_high_score_ui(highscore)
		save_high_score()

def load_high_score():
	global highscore
	try: 
		f = open('HighScore', 'r', encoding="utf-8")
		if f.read() != "":
			highscore = int(f.read())
			UIManager.update_high_score_ui(highscore)
		else:
			highscore = 0
		f.close()
	except:
		highscore = 0

def save_high_score():
	global highscore
	f = open('HighScore', 'w', encoding="utf-8")
	f.write(str(highscore))
	f.close()






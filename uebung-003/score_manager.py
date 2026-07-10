import ui_manager


score = 0
highscore = 0


def add_score(points: int):
	global score
	score += points
	ui_manager.update_score_ui(score)

def reset_score():
	global score
	score = 0
	ui_manager.update_score_ui(score)

def try_update_highscore():
	global score, highscore
	if score >= highscore:
		highscore = score
		ui_manager.update_high_score_ui(highscore)
		save_high_score()

def load_high_score():
	global highscore
	try: 
		f = open('HighScore', 'r', encoding="utf-8")
		content = f.read()
		if content != "":
			highscore = int(content)
		else:
			highscore = 0

		ui_manager.update_high_score_ui(highscore)
		f.close()
	except:
		highscore = 0

def save_high_score():
	global highscore
	f = open('HighScore', 'w', encoding="utf-8")
	f.write(str(highscore))
	f.close()






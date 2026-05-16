import ui_manager

money = 0

def add_money(coins):
	global money
	money += coins
	ui_manager.update_money_ui(money)

def remove_money(coins):
	global money
	money -= coins
	ui_manager.update_money_ui(money)

def get_current_money():
   return money
	
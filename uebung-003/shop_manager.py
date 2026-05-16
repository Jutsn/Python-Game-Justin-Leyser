import random
import ui_manager
import money_manager
from shop_offer import Shop_Offer


shop_offer = None
shop_updated = False
upgrade_bought = False
current_player = None


def set_shop_offer(player):
    global shop_updated, current_player, shop_offer
    if shop_updated == True:
        return
    if shop_updated == False:
        shop_updated = True
        current_player = player
        #randomize offer
        general_offer = Shop_Offer()
        shop_offer = general_offer.possible_upgrades
        index = random.randrange(0,4)
        shop_offer.pop(index)

        #randomize price
        card_1 = shop_offer[0]
        card_1["cost"] = 1#random.randrange(20,30)
        card_2 = shop_offer[1]
        card_2["cost"] = 1#random.randrange(25,40)
        card_3 = shop_offer[2]
        card_3["cost"] = 1#random.randrange(20,25)
        #update UI
        ui_manager.update_item_cards_ui(card_1, card_2,card_3)
        

def check_for_interaction(mouse_pos):
    # Check for mouse collision
    for rect in ui_manager.card_rects:
        if rect.collidepoint(mouse_pos):
            #Get equivalent Shop Offer Text to clicked Rect
            rect_index = ui_manager.card_rects.index(rect)
            try_buy_upgrade(shop_offer[rect_index])
    
def try_buy_upgrade(upgrade_type):
    global upgrade_bought
    if money_manager.get_current_money() >= upgrade_type["cost"]:
        upgrade_bought = True
        money_manager.remove_money(upgrade_type["cost"])
        current_player.upgrade_might(upgrade_type)

def reset_shop():
    global upgrade_bought
    upgrade_bought = False

def check_if_upgrade_is_bought():
    return upgrade_bought
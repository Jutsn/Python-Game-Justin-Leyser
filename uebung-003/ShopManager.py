import pygame
import UIManager
import random
from ShopOffer import Shop_Offer

shop_offer = Shop_Offer().item_array
shop_updated = False
current_player = None
upgrade_bought = False

def set_shop_offer(player):
    global shop_updated, current_player, shop_offer
    if shop_updated == True:
        return
    if shop_updated == False:
        current_player = player
        #randomize offer
        general_offer = Shop_Offer()
        shop_offer = general_offer.item_array
        index = random.randrange(0,4)
        shop_offer.pop(index)
        #update UI
        UIManager.update_item_cards_ui(shop_offer[0], shop_offer[1],shop_offer[2])
        shop_updated = True

def check_for_interaction(mouse_pos):
    # Check for mouse collision
    for rect in UIManager.card_rects:
        if rect.collidepoint(mouse_pos):
            #Get equivalent Shop Offer Text to clicked Rect
            rect_index = UIManager.card_rects.index(rect)
            buy_upgrade(shop_offer[rect_index])
    
def buy_upgrade(upgrade_type):
    global upgrade_bought
    upgrade_bought = True
    current_player.upgrade_might(upgrade_type)
    

def check_if_upgrade_is_bought():
    return upgrade_bought

def reset_shop():
    upgrade_bought == False
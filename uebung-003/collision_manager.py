import ui_manager
from space_ship_enemy import SpaceShip
from space_ship_boss import SpaceShipBoss
from comet_boss import CometBoss


def check_for_collisions(level, player):
    # Collision of obstacles with...
    for obs in level.obstacles:
        # ...player
        if (obs.collision_with_player(player.get_rect())):
            collect_power_up(obs, level, player)
        # ...enemies
        for enemy in level.enemies:
            if (obs.collision_with_enemy(enemy.get_rect())):
                remove_enemy_without_points(level, enemy)

    # Collision of enemies with...
    for enemy in level.enemies:
        # ...player
        if enemy.collision_with_player(player.get_rect()):
            if enemy.boss == 0:
                remove_enemy_without_points(level, enemy)
            deal_damage_to_player(player, enemy)
        # ...shots
        for shot in player.shots:
            if enemy.collision_with_shot(shot.get_rect()):
                enemy.get_damage(player.dmg)
                shot.life = 0
        if isinstance(enemy, SpaceShip):
            for shot in enemy.shots:
                if player.collision_with_shot(shot.get_rect()):
                    deal_damage_to_player(player, enemy)
                    shot.life = 0


def collect_power_up(obs, level, player):
    level.obstacles.remove(obs)
    player.power_up_might(obs.length)
    ui_manager.show_pop_up_UI("Temporary Stat Boost")

def remove_enemy_without_points(level, enemy):
    level.enemies.remove(enemy)

def deal_damage_to_player(player, enemy):
    player.get_damage(enemy.damage)
    ui_manager.update_player_health_ui(player.hp)
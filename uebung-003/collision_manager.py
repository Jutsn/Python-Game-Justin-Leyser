import ui_manager
from space_ship_enemy import SpaceShip


def check_for_collisions(level, player):
    # Collision of obstacles with...
    for obs in level.obstacles:
        # ...player
        if (obs.collision_with_player(player.get_rect())):
            level.obstacles.remove(obs)
            player.power_up_might(obs.length)
            ui_manager.show_pop_up_UI("Temporary Stat Boost")
        # ...enemies
        for enemy in level.enemies:
            if (obs.collision_with_enemy(enemy.get_rect())):
                level.enemies.remove(enemy)

    # Collision of enemies with...
    for enemy in level.enemies:
        # ...player
        if enemy.collision_with_player(player.get_rect()):
            level.enemies.remove(enemy)
            player.get_damage(enemy.damage)
            ui_manager.update_player_health_ui(player.hp)
        # ...shots
        for shot in player.shots:
            if enemy.collision_with_shot(shot.get_rect()):
                enemy.get_damage(1)
                shot.life = 0
        if enemy is SpaceShip:
            for shot in enemy.shots:
                if player.collision_with_shot(shot.get_rect()):
                    player.get_damage(1)
                    shot.life = 0
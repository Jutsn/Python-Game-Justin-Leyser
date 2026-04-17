import pygame
import Projectiles
import ScoreManager
import Enemies

def handle_collisions():
	for bullet in Projectiles.bullets:
		for enemy in Enemies.enemies:
			if bullet.rect.colliderect(enemy.rect):
				enemy.die()
				ScoreManager.adjustScore()
				Projectiles.bullets.remove(bullet)
				break

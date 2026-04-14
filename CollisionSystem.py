import pygame
import Projectiles
from Enemies import Enemy


def handle_collisions(enemy):
	for bullet in Projectiles.bullets:
		if bullet.rect.colliderect(enemy.rect):
			enemy.die()
			Projectiles.bullets.remove(bullet)
			break
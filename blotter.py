import sys
from time import sleep
from settings import Settings

import pygame



class Blotter:

	"""The game Blotter, Welcome!"""


	def __init__(self):
		"""Initalize game and create game resources"""

		# Call pygame constructor to initialize background settings
		pygame.init()
		self.settings = Settings()
		
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Blotter")


		#set background color.
		self.bg_color = (230, 0, 0)

	def run(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()

			self._update_screen()


	def _check_events(self):
		"""respond to keypresses and mouse events"""
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self.check_keydown_events(event)


	def _check_play_button(self, mouse_pos):
		"""Start a new game when the player clicks Play."""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			# Reset the game settings.
			self.settings.initialize_dynamic_settings()

			# Reset the game statistics.
			self.stats.reset_stats()
			self.stats.game_active = True
			self.sb.prep_score()
			self.sb.prep_level()
			self.sb.prep_ships()

			# Get rid of any remaining aliens and bullets
			self.aliens.empty()
			self.bullets.empty()

			# Create a new fleet and center the ship.
			self._create_fleet()
			self.ship.center_ship()

			# Hide the mouse cursor.
			pygame.mouse.set_visible(False)


	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)

		#make the mose recently drawn screen visible.
		pygame.display.flip()	


	def check_keydown_events(self, event):

		if event.key == pygame.K_q:
			sys.exit()


if __name__ == '__main__':
	bt = Blotter()
	bt.run()
class TextDrawer:
	def __init__(self, surface):
		self.surface = surface

	def draw_text(self, text, font, color, rect):
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect(center=rect.center)
		self.surface.blit(text_surface, text_rect)
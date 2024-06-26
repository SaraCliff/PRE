class TextDrawer2:
	@staticmethod
	def draw_text(screen, text, font, color, rect):
		font_surface = font.render(text, True, color)
		font_rect = font_surface.get_rect(center=rect.center)

		words = text.split()
		lines = []
		line = ""
		width, _ = rect.size

		for word in words:
			test_line = line + word + " "
			test_line_width, _ = font.size(test_line)

			if test_line_width <= width:
				line = test_line
			else:
				lines.append(line)
				line = word + " "

		lines.append(line)  # Agregar la última línea

		font_height = font.size("Tg")[1]  # Altura de una línea de texto
		y_offset = font_rect.centery - (len(lines) * font_height) / 2

		for line in lines:
			text_surface = font.render(line, True, color)
			text_rect = text_surface.get_rect(center=(font_rect.centerx, y_offset))
			screen.blit(text_surface, text_rect)
			y_offset += font_height

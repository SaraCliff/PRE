def spawn_arrow(direction):
    if direction == "derecha":
        x_position = REFERENCE_POSITIONS[0]
        arrow_image = arrow_right_image
    elif direction == "izquierda":
        x_position = REFERENCE_POSITIONS[3]
        arrow_image = arrow_left_image
    elif direction == "arriba":
        x_position = REFERENCE_POSITIONS[2]
        arrow_image = arrow_up_image
    elif direction == "abajo":
        x_position = REFERENCE_POSITIONS[1]
        arrow_image = arrow_down_image
    y_position = SCREEN_HEIGHT
    arrow = Arrow(x_position, y_position, direction, arrow_image)
    all_sprites.add(arrow)
    arrows.add(arrow)
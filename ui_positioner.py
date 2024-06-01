def generate_positions_column(x_position: int, y_position: int, button_width: int, button_height: int, button_gap: int, button_count: int) -> list[tuple[int, int, int, int]]:
    positions = []
    for i in range(button_count):
        positions.append((x_position, y_position + i * (button_height + button_gap), button_width, button_height))
        
    return positions
    
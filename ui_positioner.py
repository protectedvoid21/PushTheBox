from pygame import Vector2

from button import Button


def generate_positions_column(x_position: int, y_position: int, button_width: int, button_height: int, button_gap: int, button_count: int) \
        -> list[tuple[int, int, int, int]]:
    return [(x_position, y_position + i * (button_height + button_gap), button_width, button_height) for i in range(button_count)]


def center_buttons_x(buttons: list[Button], screen_size: tuple[int, int]) -> None:
    button_width = buttons[0].rect.width

    x = (screen_size[0] - button_width) // 2
    
    for i, button in enumerate(buttons):
        button.rect.x = x
        
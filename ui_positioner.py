from pygame import Rect


def generate_positions_column(x_position: int, y_position: int, button_width: int, button_height: int, button_gap: int,
                              button_count: int) \
        -> list[tuple[int, int, int, int]]:
    """
    Generate a list of positions for a column of buttons.

    Args:
        x_position (int): The x position of the first button.
        y_position (int): The y position of the first button.
        button_width (int): The width of the buttons.
        button_height (int): The height of the buttons.
        button_gap (int): The gap between the buttons.
        button_count (int): The number of buttons.

    Returns:
        list[tuple[int, int, int, int]]: A list of tuples representing the positions and sizes of the buttons.
    """
    return [(x_position, y_position + i * (button_height + button_gap), button_width, button_height) for i in
            range(button_count)]


def center_objects_x(rects: list[Rect], screen_size: tuple[int, int]) -> None:
    """
    Center a list of rectangles horizontally on the screen.

    Args:
        rects (list[Rect]): The list of rectangles to center.
        screen_size (tuple[int, int]): The size of the screen.
    """
    button_width = rects[0].width

    x = (screen_size[0] - button_width) // 2

    for i, rect in enumerate(rects):
        rect.x = x
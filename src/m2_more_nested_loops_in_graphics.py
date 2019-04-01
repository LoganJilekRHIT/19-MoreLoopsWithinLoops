"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Logan Jilek.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------
    upper_right = rectangle.get_upper_right_corner()
    lower_left = rectangle.get_lower_left_corner()

    x_factor = rectangle.get_width()
    y_factor = rectangle.get_height()

    for k in range(n):
        for j in range(k + 1):
            new_rectangle = rg.Rectangle(upper_right, lower_left)
            new_rectangle.attach_to(window)
            window.render(.1)

            upper_right.x = upper_right.x - x_factor
            lower_left.x = lower_left.x - x_factor

        upper_right.y = upper_right.y - y_factor
        lower_left.y = lower_left.y - y_factor

        upper_right.x = upper_right.x + ((3/2 + k) * x_factor)
        lower_left.x = lower_left.x + ((3/2 + k) * x_factor)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()

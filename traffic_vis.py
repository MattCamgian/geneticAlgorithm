from PIL import Image, ImageDraw
import IPython.display


def draw_intersection(intersection):
    for i in range(0, 4):
        draw_traffic_arrows(intersection[0] == i, intersection[1] == i, intersection[2] == i, intersection[3] == i)

def draw_traffic_arrows(north_to_south=True, south_to_north=True, east_to_west=True, west_to_east=True):
    # Open the image and create the drawing agent.

    im = Image.open("geneticAlgorithm/intersection.png")
    draw = ImageDraw.Draw(im)

    # Get some structural information.
    im_width = im.size[0]
    im_height = im.size[1]
    middle_x = im_width / 2
    middle_y = im_height / 2
    offset = im_width / 15
    arrow_offset = im_width / 30

    # Draw the traffic arrow from the north to the south.
    if north_to_south:
        line = (middle_x - offset, 0, middle_x - offset, 0.75*im_height)
        triangle = [(middle_x - offset - arrow_offset, 0.75*im_height),
                    (middle_x - offset + arrow_offset, 0.75*im_height),
                    (middle_x - offset, 0.75*im_height + arrow_offset)]
        draw.line(line, fill="red", width=10)
        draw.polygon(triangle, fill="red", outline=None)

    # Draw the traffic arrow from the south to the north.
    if south_to_north:
        line = (middle_x + offset, im_height, middle_x + offset, 0.25*im_height)
        triangle = [(middle_x + offset - arrow_offset, 0.25*im_height),
                    (middle_x + offset + arrow_offset, 0.25*im_height),
                    (middle_x + offset, 0.25*im_height - arrow_offset)]
        draw.line(line, fill="red", width=10)
        draw.polygon(triangle, fill="red", outline=None)

    # Draw the traffic arrow from the west to the east.
    if west_to_east:
        line = (0, middle_y + offset, 0.75*im_width, middle_y + offset)
        triangle = [(0.75*im_width, middle_y + offset - arrow_offset),
                    (0.75*im_width, middle_y + offset + arrow_offset),
                    (0.75*im_width + arrow_offset, middle_y + offset)]
        draw.line(line, fill="blue", width=10)
        draw.polygon(triangle, fill="blue", outline=None)

    # Draw the traffic arrow from the east to the west.
    if east_to_west:
        line = (im_width, middle_y - offset, 0.25*im_width, middle_y - offset)
        triangle = [(0.25*im_width, middle_y - offset - arrow_offset),
                    (0.25*im_width, middle_y - offset + arrow_offset),
                    (0.25*im_width - arrow_offset, middle_y - offset)]
        draw.line(line, fill="blue", width=10)
        draw.polygon(triangle, fill="blue", outline=None)

    im.thumbnail([128,128])
    # Show (or save) the image.
    display(im)
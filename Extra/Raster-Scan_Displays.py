import matplotlib.pyplot as plt
import numpy as np

# Initialize a black raster
SIZE = 100
raster = np.zeros((SIZE, SIZE))

def draw_line(x1, y1, x2, y2, pixel_mask, line_width):
    dx = x2 - x1
    dy = y2 - y1

    x = x1
    y = y1

    # Pixel mask index
    mask_index = 0

    # If the absolute value of dy is less than dx
    if abs(dy) < abs(dx):
        # If x1 is greater than x2
        if x1 > x2:
            draw_line(x2, y2, x1, y1, pixel_mask, line_width)
        else:
            # Calculate the error
            p = 2 * dy - dx

            while x < x2:
                if pixel_mask[mask_index % len(pixel_mask)] == 1:
                    if line_width % 2 == 0:
                        raster[max(0, y-line_width//2):min(100, y+line_width//2), x] = 1
                    else:
                        raster[max(0, y-line_width//2):min(100, y+line_width//2 + 1), x] = 1
                x += 1
                mask_index += 1

                if p < 0:
                    p = p + 2 * dy
                else:
                    y += 1
                    p = p + 2 * dy - 2 * dx
    else:
        # If y1 is greater than y2
        if y1 > y2:
            draw_line(x2, y2, x1, y1, pixel_mask, line_width)
        else:
            # Calculate the error
            p = 2 * dx - dy

            while y < y2:
                if pixel_mask[mask_index % len(pixel_mask)] == 1:
                    if line_width % 2 == 0:
                        raster[y, max(0, x-line_width//2):min(100, x+line_width//2)] = 1
                    else:
                        raster[y, max(0, x-line_width//2):min(100, x+line_width//2 + 1)] = 1
                y += 1
                mask_index += 1

                if p < 0:
                    p = p + 2 * dx
                else:
                    x += 1
                    p = p + 2 * dx - 2 * dy

def main():
    x1, y1 = map(int, input("Enter the start coordinates (x1, y1): ").split())
    x2, y2 = map(int, input("Enter the end coordinates (x2, y2): ").split())

    line_width = int(input("Enter the line width: "))

    # Line types mask presets
    SOLID_LINE = [1]
    DOT_LINE = [1, 0]
    DASH_LINE = [1, 1, 1, 0, 0]

    line_type = int(input("Enter the line type (1 - Solid, 2 - Dot, 3 - Dash, 4 - Custom): "))

    if line_type == 1:
        mask = SOLID_LINE
    elif line_type == 2:
        mask = DOT_LINE
    elif line_type == 3:
        mask = DASH_LINE
    else:
        mask = list(map(int, input("Enter the custom mask: ").split()))

    draw_line(x1, y1, x2, y2, mask, line_width)

    # Display the raster
    plt.imshow(raster, cmap='gray')
    plt.title(f"Raster Scan Display start = {x1, y1} end = {x2, y2} width = {line_width} mask = {mask}")
    plt.show()


if __name__ 
from typing import List, Tuple

def pack_boxes(boxes: List[Tuple[int, int, int]]):
    """
    Returns a list with the lengths of the sides of the box
    """
    output_box = (0, 0, 0)
    for box in boxes:
        height, length, width = sorted(box)

        out_length = max(width, max(output_box[:-1]))
        out_height = max(length, min(output_box[:-1]))
        output_box = (out_length, out_height, output_box[2] + height)

    return output_box

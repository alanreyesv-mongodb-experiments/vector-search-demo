import sys
import colorsys
import math
import random


def to_html_hex(vector):
    return "".join(["%02x" % it for it in vector])


def to_normalized_rgb(vector):
    return [it / 255 for it in vector]


def to_normalized_hls(vector):
    return colorsys.rgb_to_hls(*to_normalized_rgb(vector))


def to_normalized_hsv(vector):
    return colorsys.rgb_to_hsv(*to_normalized_rgb(vector))


def euclidean_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        raise Exception("vectors must be of same size")

    total_sum = 0
    for i in range(len(vector1)):
        total_sum += math.pow(vector2[i] - vector1[i], 2)

    return math.sqrt(total_sum)


colors = [
    ("AliceBlue", (240, 248, 255)),
    ("AntiqueWhite", (250, 235, 215)),
    ("Aqua", (0, 255, 255)),
    ("Aquamarine", (127, 255, 212)),
    ("Azure", (240, 255, 255)),
    ("Beige", (245, 245, 220)),
    ("Bisque", (255, 228, 196)),
    ("Black", (0, 0, 0)),
    ("BlanchedAlmond", (255, 235, 205)),
    ("Blue", (0, 0, 255)),
    ("BlueViolet", (138, 43, 226)),
    ("Brown", (165, 42, 42)),
    ("BurlyWood", (222, 184, 135)),
    ("CadetBlue", (95, 158, 160)),
    ("Chartreuse", (127, 255, 0)),
    ("Chocolate", (210, 105, 30)),
    ("Coral", (255, 127, 80)),
    ("CornflowerBlue", (100, 149, 237)),
    ("Cornsilk", (255, 248, 220)),
    ("Crimson", (220, 20, 60)),
    ("Cyan", (0, 255, 255)),
    ("DarkBlue", (0, 0, 139)),
    ("DarkCyan", (0, 139, 139)),
    ("DarkGoldenrod", (184, 134, 11)),
    ("DarkGray", (169, 169, 169)),
    ("DarkGreen", (0, 100, 0)),
    ("DarkKhaki", (189, 183, 107)),
    ("DarkMagenta", (139, 0, 139)),
    ("DarkOliveGreen", (85, 107, 47)),
    ("DarkOrange", (255, 140, 0)),
    ("DarkOrchid", (153, 50, 204)),
    ("DarkRed", (139, 0, 0)),
    ("DarkSalmon", (233, 150, 122)),
    ("DarkSeaGreen", (143, 188, 139)),
    ("DarkSlateBlue", (72, 61, 139)),
    ("DarkSlateGray", (47, 79, 79)),
    ("DarkTurquoise", (0, 206, 209)),
    ("DarkViolet", (148, 0, 211)),
    ("DeepPink", (255, 20, 147)),
    ("DeepSkyBlue", (0, 191, 255)),
    ("DimGray", (105, 105, 105)),
    ("DodgerBlue", (30, 144, 255)),
    ("FireBrick", (178, 34, 34)),
    ("FloralWhite", (255, 250, 240)),
    ("ForestGreen", (34, 139, 34)),
    ("Fuchsia", (255, 0, 255)),
    ("Gainsboro", (220, 220, 220)),
    ("GhostWhite", (248, 248, 255)),
    ("Gold", (255, 215, 0)),
    ("Goldenrod", (218, 165, 32)),
    ("Gray", (128, 128, 128)),
    ("Green", (0, 128, 0)),
    ("GreenYellow", (173, 255, 47)),
    ("HoneyDew", (240, 255, 240)),
    ("HotPink", (255, 105, 180)),
    ("IndianRed", (205, 92, 92)),
    ("Indigo", (75, 0, 130)),
    ("Ivory", (255, 255, 240)),
    ("Khaki", (240, 230, 140)),
    ("Lavender", (230, 230, 250)),
    ("LavenderBlush", (255, 240, 245)),
    ("LawnGreen", (124, 252, 0)),
    ("LemonChiffon", (255, 250, 205)),
    ("LightBlue", (173, 216, 230)),
    ("LightCoral", (240, 128, 128)),
    ("LightCyan", (224, 255, 255)),
    ("LightGoldenrodYellow", (250, 250, 210)),
    ("LightGray", (211, 211, 211)),
    ("LightGreen", (144, 238, 144)),
    ("LightPink", (255, 182, 193)),
    ("LightSalmon", (255, 160, 122)),
    ("LightSeaGreen", (32, 178, 170)),
    ("LightSkyBlue", (135, 206, 250)),
    ("LightSlateGray", (119, 136, 153)),
    ("LightSteelBlue", (176, 196, 222)),
    ("LightYellow", (255, 255, 224)),
    ("Lime", (0, 255, 0)),
    ("LimeGreen", (50, 205, 50)),
    ("Linen", (250, 240, 230)),
    ("Magenta", (255, 0, 255)),
    ("Maroon", (128, 0, 0)),
    ("MediumAquamarine", (102, 205, 170)),
    ("MediumBlue", (0, 0, 205)),
    ("MediumOrchid", (186, 85, 211)),
    ("MediumPurple", (147, 112, 219)),
    ("MediumSeaGreen", (60, 179, 113)),
    ("MediumSlateBlue", (123, 104, 238)),
    ("MediumSpringGreen", (0, 250, 154)),
    ("MediumTurquoise", (72, 209, 204)),
    ("MediumVioletRed", (199, 21, 133)),
    ("MidnightBlue", (25, 25, 112)),
    ("MintCream", (245, 255, 250)),
    ("MistyRose", (255, 228, 225)),
    ("Moccasin", (255, 228, 181)),
    ("NavajoWhite", (255, 222, 173)),
    ("Navy", (0, 0, 128)),
    ("OldLace", (253, 245, 230)),
    ("Olive", (128, 128, 0)),
    ("OliveDrab", (107, 142, 35)),
    ("Orange", (255, 165, 0)),
    ("OrangeRed", (255, 69, 0)),
    ("Orchid", (218, 112, 214)),
    ("PaleGoldenrod", (238, 232, 170)),
    ("PaleGreen", (152, 251, 152)),
    ("PaleTurquoise", (175, 238, 238)),
    ("PaleVioletRed", (219, 112, 147)),
    ("PapayaWhip", (255, 239, 213)),
    ("PeachPuff", (255, 218, 185)),
    ("Peru", (205, 133, 63)),
    ("Pink", (255, 192, 203)),
    ("Plum", (221, 160, 221)),
    ("PowderBlue", (176, 224, 230)),
    ("Purple", (128, 0, 128)),
    ("RebeccaPurple", (102, 51, 153)),
    ("Red", (255, 0, 0)),
    ("RosyBrown", (188, 143, 143)),
    ("RoyalBlue", (65, 105, 225)),
    ("SaddleBrown", (139, 69, 19)),
    ("Salmon", (250, 128, 114)),
    ("SandyBrown", (244, 164, 96)),
    ("SeaGreen", (46, 139, 87)),
    ("SeaShell", (255, 245, 238)),
    ("Sienna", (160, 82, 45)),
    ("Silver", (192, 192, 192)),
    ("SkyBlue", (135, 206, 235)),
    ("SlateBlue", (106, 90, 205)),
    ("SlateGray", (112, 128, 144)),
    ("Snow", (255, 250, 250)),
    ("SpringGreen", (0, 255, 127)),
    ("SteelBlue", (70, 130, 180)),
    ("Tan", (210, 180, 140)),
    ("Teal", (0, 128, 128)),
    ("Thistle", (216, 191, 216)),
    ("Tomato", (255, 99, 71)),
    ("Turquoise", (64, 224, 208)),
    ("Violet", (238, 130, 238)),
    ("Wheat", (245, 222, 179)),
    ("White", (255, 255, 255)),
    ("WhiteSmoke", (245, 245, 245)),
    ("Yellow", (255, 255, 0)),
    ("YellowGreen", (154, 205, 50)),
]

search_color = (
    int(sys.argv[1]) if len(sys.argv) > 1 else random.randint(0, 255),
    int(sys.argv[2]) if len(sys.argv) > 1 else random.randint(0, 255),
    int(sys.argv[3]) if len(sys.argv) > 1 else random.randint(0, 255),
)

search_rgb = to_normalized_rgb(search_color)
matches_rgb = [
    (
        euclidean_distance(search_rgb, to_normalized_rgb(it[1])),
        it,
    )
    for it in colors
]

matches_rgb.sort(key=lambda it: it[0])

search_hls = to_normalized_hls(search_color)
matches_hls = [
    (
        euclidean_distance(search_hls, to_normalized_hls(it[1])),
        it,
    )
    for it in colors
]

matches_hls.sort(key=lambda it: it[0])

search_hsv = to_normalized_hsv(search_color)
matches_hsv = [
    (
        euclidean_distance(search_hsv, to_normalized_hsv(it[1])),
        it,
    )
    for it in colors
]

matches_hsv.sort(key=lambda it: it[0])

with open("colors.html", mode="w", encoding="utf-8") as fp:
    rgb_string = [f"{it:.4f}" for it in search_rgb]
    hls_string = [f"{it:.4f}" for it in search_hls]
    hsv_string = [f"{it:.4f}" for it in search_hsv]

    fp.write("<html><head><style>")
    fp.write(
        """
        table td {
            vertical-align: top;
            border: 0;
        }
    """
    )
    fp.write("</style></head>")
    fp.write("<body>")

    fp.write("<table style='width: 100%;'><tr><td></td><td>")

    fp.write(
        f"""<table style='width: 100%;'>
        <tr><td><b>Search color</b></td></tr>
        <tr>
            <td>RGB</td>
            <td>HTML</td>
            <td>RGB (normalized)</td>
            <td>HLS (normalized)</td>
            <td>HSV (normalized)</td>
            <td></td>
        </tr>
        <tr>
            <td>{search_color}</td>
            <td>#{to_html_hex(search_color)}</td>
            <td>{rgb_string}</td>
            <td>{hls_string}</td>
            <td>{hsv_string}</td>
            <td style='width: 3em; background-color: #{to_html_hex(search_color)}';>&nbsp;</td>
        </tr>
    </table>"""
    )

    fp.write("</td></tr><tr><td>")

    fp.write(f"<table style='width: 100%;'>")
    fp.write(f"<tr><td><b>RGB</b></td></tr>")
    fp.write(f"<tr><td>Color</td><td>Vector</td><td>Distance</td></tr>")

    for match in matches_rgb:
        distance = match[0]
        color_name = match[1][0]
        rgb_normalized = [f"{it:.4f}" for it in to_normalized_rgb(match[1][1])]

        fp.write(
            f"""<tr>
            <td>{color_name}</td>
            <td>{rgb_normalized}</td>
            <td>{distance:.4f}</td>
            <td style='width: 3em; background-color: {color_name};'>&nbsp;</td>
        </tr>"""
        )

    fp.write(f"</table></td>")
    fp.write(f"<td><table style='width: 100%;'>")

    fp.write(f"<tr><td><b>HLS</b></td></tr>")
    fp.write(f"<tr><td>Color</td><td>Vector</td><td>Distance</td></tr>")

    for match in matches_hls:
        distance = match[0]
        color_name = match[1][0]
        hls_normalized = [f"{it:.4f}" for it in to_normalized_hls(match[1][1])]

        fp.write(
            f"""<tr>
            <td>{color_name}</td>
            <td>{hls_normalized}</td>
            <td>{distance:.4f}</td>
            <td style='width: 3em; background-color: {color_name};'>&nbsp;</td>
        </tr>"""
        )

    fp.write(f"</table></td>")
    fp.write(f"<td><table style='width: 100%;'>")

    fp.write(f"<tr><td><b>HSV</b></td></tr>")
    fp.write(f"<tr><td>Color</td><td>Vector</td><td>Distance</td></tr>")

    for match in matches_hsv:
        distance = match[0]
        color_name = match[1][0]
        hsv_normalized = [f"{it:.4f}" for it in to_normalized_hsv(match[1][1])]

        fp.write(
            f"""<tr>
            <td>{color_name}</td>
            <td>{hsv_normalized}</td>
            <td>{distance:.4f}</td>
            <td style='width: 3em; background-color: {color_name};'>&nbsp;</td>
        </tr>"""
        )

    fp.write(f"</table></td>")
    fp.write(f"</tr>")

    fp.write("</table>")
    fp.write("</body></html>")

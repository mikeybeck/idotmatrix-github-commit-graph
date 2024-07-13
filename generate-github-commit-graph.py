import requests
import datetime
import sys

def get_github_contributions(username, year):
    url = f"https://github-contributions-api.jogruber.de/v4/{username}?y={year}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def map_color_to_rgb(intensity):
    color_map = {
        0: (0, 0, 0),
        1: (0, 50, 0),
        2: (0, 100, 0),
        3: (0, 175, 0),
        4: (0, 255, 0)
    }
    return color_map.get(intensity, (0, 0, 0))

def generate_contribution_graph(username, year, is_previous_year = False):
    data = get_github_contributions(username, year)
    contributions = data['contributions']

    output = []

    start_y_1 = 1
    start_y_2 = 9
    if is_previous_year:
        start_y_1 = 17
        start_y_2 = 25

        # Display a row of blue squares to separate the two halves
        for x in range(32):
            y = start_y_1 - 1
            r, g, b = 0, 0, 255
            output.append(f"{x}-{y}-{r}-{g}-{b}")

    contribution_index = 0
    for x in range(6, 32):
        for y in range(start_y_2, start_y_2 + 7):
            r, g, b = 0, 0, 0
            intensity = 0
            if contribution_index < len(contributions):
                intensity = contributions[contribution_index]['level']
                r, g, b = map_color_to_rgb(intensity)
                contribution_index += 1
            if intensity != 0:
                output.append(f"{x}-{y}-{r}-{g}-{b}")

    # Display a row of blue squares to separate the two halves
    for x in range(6, 32):
        y = start_y_1 + 7
        r, g, b = 0, 0, 255
        output.append(f"{x}-{y}-{r}-{g}-{b}")

    for x in range(6, 32):
        for y in range(start_y_1, start_y_1 + 7):
            r, g, b = 0, 0, 0
            intensity = 0
            if contribution_index < len(contributions):
                intensity = contributions[contribution_index]['level']
                r, g, b = map_color_to_rgb(intensity)
                contribution_index += 1
            if intensity != 0:
                output.append(f"{x}-{y}-{r}-{g}-{b}")

    # Print vertical row of blue squares to show start of year
    for y in range(32):
        x = 5
        r, g, b = 0, 0, 255
        output.append(f"{x}-{y}-{r}-{g}-{b}")

    # Print row of pixels at top to show start of year. Stop at current week
    current_week = datetime.datetime.now().isocalendar()[1]
    if current_week > 26:
        current_week = current_week - 26

    for x in range (6, 32):
        y = 0
        if x <= current_week + 5:
            r, g, b = 0, 0, 255
        else:
            r, g, b = 0, 0, 50

        output.append(f"{x}-{y}-{r}-{g}-{b}")

    return " ".join(output)

def display_numbers(number, last_year = False):
    digit_patterns = {
        '0': ['###', '# #', '# #', '# #', '###'],
        '1': [' # ', '## ', ' # ', ' # ', '###'],
        '2': ['###', '  #', '###', '#  ', '###'],
        '3': ['###', '  #', '###', '  #', '###'],
        '4': ['# #', '# #', '###', '  #', '  #'],
        '5': ['###', '#  ', '###', '  #', '###'],
        '6': ['###', '#  ', '###', '# #', '###'],
        '7': ['###', '  #', ' # ', ' # ', ' # '],
        '8': ['###', '# #', '###', '# #', '###'],
        '9': ['###', '# #', '###', '  #', '###']
    }

    number_str = str(number)

    filled_pixels = []

    y_offset = 0
    if last_year:
        y_offset = 16

    for digit_index, digit in enumerate(number_str):
        for row in range(5):
            for col in range(3):
                if digit_patterns[digit][row][col] == '#':
                    x = col + 1
                    y = digit_index * 6 + row + y_offset + 3

                    filled_pixels.append(f"{x}-{y}-255-0-0")

    return " ".join(filled_pixels)


if len(sys.argv) < 2:
    print("Usage: python generate-github-commit-graph.py <username> [year]")
    sys.exit(1)

username = sys.argv[1]
if len(sys.argv) > 2:
    try:
        year = int(sys.argv[2])
    except ValueError:
        print("Year must be a number.")
        sys.exit(1)
else:
    year = datetime.datetime.now().year

try:
    this_year = (display_numbers(year - 2000))
    last_year = (display_numbers(year - 2001, True))

    result = generate_contribution_graph(username, year)
    resultPreviousYear = generate_contribution_graph(username, year - 1, True)
    print(f"{this_year} {last_year} {result} {resultPreviousYear}")

except Exception as e:
    print(f"An error occurred: {str(e)}")

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
        0: (235, 237, 240),  # lightest
        1: (155, 233, 168),
        2: (64, 196, 99),
        3: (48, 161, 78),
        4: (33, 110, 57)     # darkest
    }
    return color_map.get(intensity, (0, 0, 0))

def generate_contribution_graph(username, year):
    data = get_github_contributions(username, year)
    contributions = data['contributions']

    output = []
    contribution_index = 0
    for x in range(32):
        for y in range(8):
            r, g, b = 0, 0, 0  # Initialize with default values
            if y < 7 and contribution_index < len(contributions):
                intensity = contributions[contribution_index]['level']
                r, g, b = map_color_to_rgb(intensity)
                contribution_index += 1
            # dont add to output if intensity is 0
            if intensity != 0:
                output.append(f"{x}-{y}-{r}-{g}-{b}")

    for x in range(32):
        for y in range(8, 16):
            r, g, b = 0, 0, 0
            if y < 16 and contribution_index < len(contributions):
                intensity = contributions[contribution_index]['level']
                r, g, b = map_color_to_rgb(intensity)
                contribution_index += 1
            if intensity != 0:
                output.append(f"{x}-{y}-{r}-{g}-{b}")

    return " ".join(output)

if len(sys.argv) < 2:
    print("Usage: python generate-github-commit-graph.py <username>")
    sys.exit(1)

username = sys.argv[1]
year = datetime.datetime.now().year

try:
    result = generate_contribution_graph(username, year)
    print(result)
except Exception as e:
    print(f"An error occurred: {str(e)}")

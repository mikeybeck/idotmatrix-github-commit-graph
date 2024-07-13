
# Github Commit Graph Generator for 32x32 Idotmatrix display

## How to use:

Execute the script to get output for the idotmatrix display:
`python generate-github-commit-graph.py <username>`

This will output a list of pixel coordinates and rgb colours in a format usable by the iDotmatrix client (https://github.com/derkalle4/python3-idotmatrix-client)

Run the iDotmatrix client with the output from this script:
`./run_in_venv.sh --address <mac address> --pixel-color <script output>`

e.g.
`./run_in_venv.sh --address 19:2B:59:A2:13:65 --pixel-color 3-1-155-233-168 3-2-155-233-168 3-3-64-196-99 5-2-155-233-168 5-3-155-233-168 5-5-155-233-168 5-6-155-233-168 5-7-0-0-0 6-0-64-196-99 6-1-155-233-168 6-2-155-233-168 6-3-155-233-168 6-4-48-161-78 7-0-48-161-78 7-1-64-196-99 7-2-48-161-78 7-3-64-196-99 7-4-155-233-168 8-0-48-161-78 8-1-64-196-99 8-2-48-161-78 8-3-33-110-57 8-4-155-233-168 9-4-155-233-168 10-0-33-110-57 10-1-48-161-78 10-2-155-233-168 10-3-64-196-99 11-0-155-233-168 11-1-155-233-168 11-2-155-233-168 11-3-155-233-168 11-4-155-233-168 12-1-155-233-168 12-2-155-233-168 13-1-155-233-168 13-2-155-233-168 14-3-155-233-168 14-4-155-233-168 15-0-155-233-168 15-1-155-233-168 15-4-64-196-99 16-0-33-110-57 16-1-64-196-99 16-2-155-233-168 17-0-64-196-99 17-2-155-233-168 17-5-155-233-168 18-0-155-233-168 18-1-155-233-168 18-3-155-233-168 19-1-155-233-168 19-2-64-196-99 20-0-155-233-168 20-1-155-233-168 20-3-155-233-168 20-4-155-233-168 21-3-155-233-168 21-4-155-233-168 23-1-155-233-168 23-2-155-233-168 23-3-155-233-168 25-1-155-233-168 26-3-155-233-168 26-4-155-233-168 26-6-155-233-168 26-7-0-0-0 27-0-155-233-168 27-3-155-233-168 27-5-155-233-168`

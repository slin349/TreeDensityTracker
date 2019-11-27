import requests
import json

import csv

response = requests.get("https://opendata.arcgis.com/datasets/005a0ce264154ff884c34eaf5472cd90_0.geojson")

responseJson = response.json()

blocks = [[0] * 50] * 30
for k in responseJson["features"]:
    a = k["geometry"]
    for i, row in enumerate(blocks, 1):
        for j, column in enumerate(row, 1):
            if (a["coordinates"][0] >= -81.30378333991494 + (i - 1) * 0.00182417088 and 
                a["coordinates"][0] <= -81.30378333991494 + i * 0.00182417088 and
                a["coordinates"][1] >= 43.00668853641974 + (j - 1) * 0.000454497309 and
                a["coordinates"][1] <= 43.00668853641974 + j * 0.000454497309):
                blocks[i-1][j-1] += 1

with open('trees.csv', 'w', newline='') as csvfile:
    fieldnames = ['X', 'Y', 'tree_density']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i, row in enumerate(blocks, 1):
        for j, column in enumerate(row, 1):
            writer.writerow({'X': ((43.00668853641974 + j * 0.000454497309) + (43.00668853641974 + (j - 1) * 0.000454497309)) / 2, 
            'Y': ((-81.30378333991494 + i * 0.00182417088) + (-81.30378333991494 + (i - 1) * 0.00182417088)) / 2, 'tree_density': blocks[i-1][j-1]})


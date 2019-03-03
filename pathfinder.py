# elevations = [ ]
# with open('elevation_small.txt') as file:
#     for line in file:
#         elevations.append([int(e) for e in line.split(" ")])
# len(elevations)
# len(elevations[0])


# class ElevationMap:
#     def __init__(self, filename):
#         self.elevations =[]
#         with open(elevation_) as file:
#             for line in file:
#                 self.elevations.append([int(e) for e in line.split()])

# elevation_graph = []
# with open ("elevation_large.txt") as file

# row_one = file.readline()
# row_one_split = row_one.split()

# # row,col = im.size
# data=[] #r,g,b,i,j
# pixels=im.load()
# for i in range(row):
#   for j in range(col):
#     # data.append(pixels[i,j]+(i,j))

from PIL import Image

with open("elevation_large.txt") as file: 
    elevation_list = []
    row_one = file.readline()
    row_one_split = row_one.split()
    max_elevation = 0
    minimum_elevation = 10000
    
    for elevations in row_one.split():
        elevation_list.append([int(elevations)])
        if int(elevations) > max_elevation:
            max_elevation = int(elevations)
        if int(elevations) < minimum_elevation:
            minimum_elevation = int(elevations)
         

    for line in file.readline():
        x = 0
        row_split = line.split()

    for elevations in row_split:
        elevation_list[x].append(int(elevations))
        if int(elevations) > max_elevation:
            max_elevation = int(elevations)
        if int(elevations) < minimum_elevation:
            minimum_elevation = int(elevations)
            x+=1   

aarons_mountain = Image.new('RGB', (len(elevation_list), len(elevation_list[0])), (255,255,255))
range_elevations = max_elevation - minimum_elevation

for y in range(len(elevation_list)):
    for x in range(len(elevation_list)):
        color_type = (int(elevation_list[x][y] - minimum_elevation) / range_elevations
        rgb_number = int(color_type*255)
        aarons_mountain.putpixel((x, y), (rgb_number, rgb_number, rgb_number))

aarons_mountain.save('mountainpass.jpg')

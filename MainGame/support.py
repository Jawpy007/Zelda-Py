from csv import reader
from os import listdir
import pygame


def import_csv_layout(path):
    terrain_map =[]
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
    
def import_folder(path):
    surfacelist = []
    for img_file in listdir(path):
        full_path = path + '/' + img_file
        image_surf= pygame.image.load(full_path).convert_alpha()
        surfacelist.append(image_surf)
    return(surfacelist)
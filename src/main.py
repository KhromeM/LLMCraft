import sys
import os

sys.path.insert(0, os.path.abspath("anvil-parser"))

import anvil

filePath = "worlds/Ferrara/FerraraWorld/region/r.0.0.mca"
region = anvil.Region.from_file(filePath)

for x in range(32):
    for z in range(32):
        try:
            chunk = anvil.Chunk.from_region(region, x, z)
            print(f"Chunk at {x}, {z} is accessible")
            break
        except KeyError:
            continue


# If `section` is not provided, will get it from the y coords
# and assume it's global
# block = chunk.get_block(0, 0, 0)

# print(block) # <Block(minecraft:air)>
# print(block.id) # air
# print(block.properties) # {}
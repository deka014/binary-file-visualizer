import sys , png

# Decoded - split array into chunks of n elements having values 0 to 255 

def pixel_chunks(l, n = 3):
    return list(zip(*[iter(l)]*n))

# not decoded - split array into chunks of n elements having hex values 


def pixel_chunks_hex(l, n = 3):
    return [l[i:i+n] for i in range(0, len(l), n)]



if __name__ == "__main__":

    # Read the file 
    with open(sys.argv[1], "rb") as f:
        data = f.read()
    
    # Convert the data to a list of pixels
    pixelsValues = pixel_chunks(data)
    #creating the rows and columns for the image

    image_size = int(len(pixelsValues)**0.5)

    pixelArray = [pixelsValues[i:i+image_size] for i in range(0, len(pixelsValues), image_size)]

    # remove last pixel for square image if needed
    if len(pixelArray[-1]) != image_size:
        pixelArray = pixelArray[:-1]
    

        

    # Write the image
    png.from_array(pixelArray, "RGB").save("./output/"+sys.argv[2])



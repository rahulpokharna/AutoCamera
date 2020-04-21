from PIL import Image
import time

# Function to compare and get the image with the brightest or darkest pixels out of the input values
def pixelComp(file1="pic1.JPG", file2="pic2.JPG", bright=True, filename="output.JPG"):
    try:
        # Open images into program
        img1 = Image.open(file1)
        img2 = Image.open(file2) 

        # Get pixels from images
        im1 = img1.load()
        im2 = img2.load()
        width, height = img1.size

        # Initialize final image
        finalImg = Image.new('RGB', (width, height))
        finalPixels = finalImg.load()

        # Iterate and compare to find brightest or darkest pixel
        for i in range(width):
            for j in range(height):

                # Convert RGB to luminosity measurement
                lum1 = calcLum(im1[i, j])
                lum2 = calcLum(im2[i, j])

                # Compare brightness of pixels
                # Changed from direct comparison of pixels
                # Compare, want to be true if brighter when night, darker when day etc
                if (lum1 > lum2) == bright:
                    finalPixels[i, j] = im1[i, j]
                else:
                    finalPixels[i, j] = im2[i, j]
        finalImg.save(filename)  # show()
        print("completed")
    except IOError:
        print("It broke")
        pass

# Function to compare and get the brightest or darkest image of the two
def imageComp(file1="pic1.JPG", file2="pic2.JPG", bright=True, filename="output.JPG"):
    try:
        # Open images into program
        img1 = Image.open(file1)
        img2 = Image.open(file2)

        # Get pixels from images
        im1 = img1.load()
        im2 = img2.load()
        width, height = img1.size

        # Initialize luminosity sum for overall brightness
        lum1 = 0
        lum2 = 0

        # Iterate and compare to find brightest or darkest pixel
        for i in range(width):
            for j in range(height):
                # Convert RGB to perceived luminosity measurement
                lum1 += calcLum(im1[i, j])
                lum2 += calcLum(im2[i, j])

        # See which image has the greatest total luminosity
        if (lum1 > lum2) == bright:
            img1.save(filename)  # show()
        else:
            img2.save(filename)
        print("completed")
    except IOError:
        print("It broke")
        pass


# Def color shift prototype to see the dealio
def colorShift(file="pic1.jpg", shift=5):
    # image shift add pixel
    # iterate thru image and set value of pixel xyz to xyz+5 for r, and mins for b
    # Function to get the image with the greatest variety/range of colors

    try:
        # Open images into program
        img = Image.open("Image\\" + file)

        # Get pixels from images
        im = img.load()
        width, height = img.size
        print("Height: ", height, "\nWidth: ", width)

        # Output image
        finalImg = Image.new('RGB', (width, height))
        finalPixels = finalImg.load()

        for i in range(width):
            for j in range(height):

                # Convert the pixels into smaller gaps, so close colors are
                # not double counted, to try to get a larger difference in color
                # r1, g1, b1 = (im[i, j])
                
                r, g, b = (im[i, j])
                r2, g2, b2 = finalPixels[i, j]
                
                # Shift along the width
                iShiftPlus = min((i+shift) % width, i+shift)
                iShiftMinus = max((i-shift) % width, i-shift)

                # This is done incorrectly, we need to access the old data from each new place we place it, the current data in the final image and all other data
                # So we don't override it, but this effect is cool. 
                # Assign New Photo image
                finalPixels[i, j] = r2, b, g2
                finalPixels[iShiftPlus, j] = r2, b2, g
                finalPixels[iShiftMinus, j] = r, b2, g2
        
        finalImg.save("Output\\JaLEN\\output_" + str(shift) + file)
        # finalImg.save("output.jpg")


    except IOError:
        print("It broke")
        pass




# Function to get the image with the greatest variety/range of colors
def colorComp(file1="pic1.JPG", file2="pic2.jpg", filename="output.jpg"):
    # Initialize the RGB list for large sizes of lists
    # rgbRange = [[[0 for i in range(32)], [0 for j in range(32)], [0 for k in range(32)]] for x in range(2)]
    
    # Create two lists to store the range of pixels with flags of 1 being present, 0 else
    # Done incorrectly, aslso make it groups of 16, and nested
    rgbRange1 = [[[0 for i in range(16)] for j in range(16)] for k in range(16)]
    rgbRange2 = [[[0 for i in range(16)] for j in range(16)] for k in range(16)] # [[0 for i in range(32)], [0 for j in range(32)], [0 for k in range(32)]]

    try:
        # Open images into program
        img1 = Image.open(file1)
        img2 = Image.open(file2)

        # Get pixels from images
        im1 = img1.load()
        im2 = img2.load()
        width, height = img1.size

        for i in range(width):
            for j in range(height):

                # Convert the pixels into smaller gaps, so close colors are
                # not double counted, to try to get a larger difference in color
                r1, g1, b1 = (im1[i, j])
                r1 = r1 // 16
                b1 = b1 // 16
                g1 = g1 // 16
                r2, g2, b2 = (im2[i, j])
                r2 = r2 // 16
                b2 = b2 // 16
                g2 = g2 // 16
                rgbRange1[r1][g1][b1] = 1
                rgbRange2[r2][g2][b2] = 1
        
        # Iterate through the rgb list to see which has a larger number
        rgbSum1 = 0
        rgbSum2 = 0
        for i in range(16):
            for j in range(16):
                for k in range(16):
                    rgbSum1 += rgbRange1[i][j][k]
                    rgbSum2 += rgbRange2[i][j][k]

        if rgbSum1 > rgbSum2:
            img1.save(filename)
        else:
            img2.save(filename)
        print("completed")

    except IOError:
        print("It broke")
        pass


# Function to calculate luminosity based upon human sight perception
def calcLum(color):
    red, green, blue = color
    return ((red * 0.2126 + green * 0.7152 + blue * 0.0722) / 255)


if __name__ == '__main__':
    #pixelComp(file1="img1.JPG", file2="img2.JPG", bright=False, filename="darkest.JPG")
    # colorComp(file1="img1.JPG", file2="img2.JPG", filename="darkest.JPG")
    start_time = time.time()

    for i in range(0,11):
        
        run_time = time.time()
        colorShift("DSC_0063.jpg", shift=i*5)
        print("Run length with " + str(i) + " shift: ", time.time() - run_time)

    print("Total Time Elapsed: ", time.time() - start_time)

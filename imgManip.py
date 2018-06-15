from PIL import Image


def imgComp(file1="pic1.JPG", file2="pic2.JPG", bright=True, filename="output.JPG"):
    
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

# Function to calculate luminosity based upon human sight perception
def calcLum(color):
    red, green, blue = color
    return ((red * 0.2126 + green * 0.7152 + blue * 0.0722) / 255)

if __name__ == '__main__':
    imgComp(file1="img1.JPG", file2="img2.JPG", bright=False, filename="darkest.JPG")

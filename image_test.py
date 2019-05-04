import image
image.initialize()

def curry(func, arg1):
    # Curry a two-place function
    def anon(arg2):
        return func(arg1, arg2)
    return anon

def one_to_one(filter, img):
    # Filter type: each new pixel is a function
    # of an old pixel in the same position.
    # Parameters: a filter function and an image
    width, height = img.get_width(), img.get_height()
    new_img = image.Image(img.name, False, width, height)
    for w in range(width):
        for h in range(height):
            pix = img.get_pixel(w, h)
            new_pix = filter(pix)
            new_img.set_pixel(new_pix, w, h)
    return new_img

def remove_red(pix):
    new_red = 0
    new_green = pix.green 
    new_blue = pix.blue 
    new_pix = image.Pixel(new_red, new_green, new_blue)
    return new_pix

def _remove_red(img):
    width, height = img.get_width(), img.get_height()
    new_img = image.Image(img.name, False, width, height)
    for w in range(width):
        for h in range(height):
            pix = img.get_pixel(w, h)
            new_red = 0
            new_green = pix.green 
            new_blue = pix.blue 
            new_pix = image.Pixel(new_red, new_green, new_blue)
            new_img.set_pixel(new_pix, w, h)
    return new_img

def remove_green(img):
    width, height = img.get_width(), img.get_height()
    new_img = image.Image(img.name, False, width, height)
    for w in range(width):
        for h in range(height):
            pix = img.get_pixel(w, h)
            new_red = pix.red
            new_green = 0 
            new_blue = pix.blue 
            new_pix = image.Pixel(new_red, new_green, new_blue)
            new_img.set_pixel(new_pix, w, h)
    return new_img

def remove_blue(img):
    width, height = img.get_width(), img.get_height()
    new_img = image.Image(img.name, False, width, height)
    for w in range(width):
        for h in range(height):
            pix = img.get_pixel(w, h)
            new_red = pix.red
            new_green = pix.green 
            new_blue = 0
            new_pix = image.Pixel(new_red, new_green, new_blue)
            new_img.set_pixel(new_pix, w, h)
    return new_img

def greyscale(img):
    width, height = img.get_width(), img.get_height()
    new_img = image.Image(img.name, False, width, height)
    for w in range(width):
        for h in range(height):
            pix = img.get_pixel(w, h)
            r, g, b = pix.red, pix.green, pix.blue
            avg = r // 3 + g // 3 + b // 3
            new_pix = image.Pixel(avg, avg, avg)
            new_img.set_pixel(new_pix, w, h)
    return new_img

def black_and_white(img):
    width, height = img.get_width(), img.get_height()
    new_img = image.Image(img.name, False, width, height)
    for w in range(width):
        for h in range(height):
            pix = img.get_pixel(w, h)
            r, g, b = pix.red, pix.green, pix.blue
            avg = r // 3 + g // 3 + b // 3
            if avg < 128:
                new_red, new_green, new_blue = 0, 0, 9
            else:
                new_red, new_green, new_blue = 255, 255, 255
            new_pix = image.Pixel(new_red,new_green, new_blue)
            new_img.set_pixel(new_pix, w, h)
    return new_img

def double(img):
    new_width, new_height = img.get_width() * 2, img.get_height() * 2
    new_img = image.Image(img.name, False, new_width, new_height)
    for w in range(img.get_width()):
        for h in range(img.get_height()):
            pix = img.get_pixel(w, h)
            for i in range(2):
                for j in range(2):
                    new_img.set_pixel(pix, 2 * w + i, 2 * h + j)
    return new_img

def halve(img):
    # Drop final row or column if width or height is odd
    width, height = (img.get_width() // 2) * 2, (img.get_height() // 2) * 2
    new_width, new_height = img.get_width() // 2, img.get_height() // 2
    new_img = image.Image(img.name, False, new_width, new_height)
    for w in range(0, width, 2):
        for h in range(0, height, 2):
            sum_red, sum_green, sum_blue = 0, 0, 0
            for i in range(2):
                for j in range(2):
                    pix = img.get_pixel(w + i, h + j)
                    sum_red += pix.red
                    sum_green += pix.green
                    sum_blue += pix.blue
            avg_red, avg_green, avg_blue = sum_red // 4, sum_green // 4, sum_blue // 4
            new_pix = image.Pixel(avg_red, avg_green, avg_blue)
            new_img.set_pixel(new_pix, w // 2, h // 2)
    return new_img

filters = {
    "rr": curry(one_to_one, remove_red),
    "rg": remove_green,
    "rb": remove_blue,
    "g": greyscale,
    "bw": black_and_white,
    "d": double,
    "h": halve}

name = input("Enter image name with extension: ")
cur_img = image.Image(name, load = True)
cur_img.draw()
img_saved = True

history = [cur_img]

# See filters dictionary above for filter choices
# Commands: 'l' - load
#           's' - save
#           'sa' - save as
#           'q' - quit
#           'u' - undo

while True:
    choice = input("Command or filter: ")
    if choice in filters.keys():
        cur_img = filters[choice](cur_img)
        cur_img.draw()
        if len(history) < 12:
            history.append(cur_img)
        else:
            history.pop(1)
            history.append(cur_img)
        img_saved = False
    elif choice == "u":
        if len(history) > 1:
            history.pop()
            cur_img = history[-1]
            cur_img.draw()
        else:
            print("History empty.")
    elif choice == "l":
        name = input("Enter image name with extension: ")
        cur_img  =  image.Image(name, load = True)
        cur_img.draw()
        history = [cur_img]
        img_saved = True
    elif choice == "s":
        if input("Will overwrite. Carry on (y or n)? ") == "y":
            cur_img.save()
            img_saved = True
    elif choice == "sa":
        new_name = input("Enter image name with extension or x to exit: ")
        if new_name != "x":
            cur_img.save_as(new_name)
            img_saved = True
    elif choice == "q":
        if img_saved:
            image.quit()
            break
        else:
            print("Image not saved. Really quit (y or n)? ", end = "")
            if input() == "y":
                image.quit()
                break
    else:
        print("Command not recognized.")
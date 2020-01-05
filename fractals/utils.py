import cv2

def show_image(image):
    while True:
        cv2.imshow('', image)

        key = cv2.waitKey(1000)
        if key == 27: # Esc
            cv2.destroyAllWindows()
            break

def load_base(size = 'normal'):
    if size == 'normal':
        return cv2.imread('base.png')
    else:
        return cv2.imread('bigbase.png')

import cv2

frame=cv2.imread('base.png')
colour=(0,255,255)

def mid_point(a,b):
    return int((a[0]+b[0])/2),int((a[1]+b[1])/2)

def sierpinski(a,b,c,d):
    # mid point of side legth
    # draw line between midpoints
    # repeat starting in lower left hand corner triangle

    cv2.line(frame,a,b,colour)
    cv2.line(frame,b,c,colour)
    cv2.line(frame,c,a,colour)

    if d>0:
        m_a_b=mid_point(a,b)
        m_b_c=mid_point(b,c)
        m_c_a=mid_point(c,a)

        sierpinski(a[:],m_a_b[:],m_c_a[:],d-1)
        sierpinski(b[:],m_a_b[:],m_b_c[:],d-1)
        sierpinski(c[:],m_c_a[:],m_b_c[:],d-1)

        
        cv2.imshow('tri',frame)

        key=cv2.waitKey(1) & 0xFF
        if key==ord('q'):
            cv2.destroyAllWindows()
            raise SystemExit


sierpinski((0,932),(499,67),(999,932),10)

while True:
    cv2.imshow('tri',frame)

    key=cv2.waitKey(1000) & 0xFF
    if key==ord('q'):
        cv2.destroyAllWindows()
        raise SystemExit



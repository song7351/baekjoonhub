from math import gcd
def solution(w, h):
    answer = w*h
    g = gcd(w,h)
    ww,hh = w//g, h//g
    
    x = ww*hh - (ww-1)*(hh-1)
    
    answer = answer - x*g
    
    return answer
import numpy as np
import os



__ALL_KEYS       = "Q,W,E,R,T,Y,U,I,O,P,Open Bracket,Close Bracket,A,S,D,F,G,H,J,K,L,Semicolon,Quote,Back Slash,Z,X,C,V,B,N,M,Period,Slash,Left Shift,Left Control,Left Alt,Caps Lock,Tab,Space,Right,Left,Up,Down".split(',')
__ALL_ROBOT_KEYS = "q,w,e,r,t,y,u,i,o,p,[,],a,s,d,f,g,h,j,k,l,;,',\\,z,x,c,v,b,n,m,.,/,shiftleft, ctrlleftm,altleft,capslock, tab, ,right,left,up,down".split(',')
__CTYPE_KEYS = [ 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B,
                 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x2B,
                 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x2A, 0x1D, 
                 0x38, 0x3A, 0x0F, 0xCD, 0xCB, 0xC8, 0xD0]

assert(len(__ALL_KEYS) == len(__ALL_ROBOT_KEYS))
assert(len(__CTYPE_KEYS) == len(__ALL_ROBOT_KEYS))

KEY_S = __ALL_KEYS.index('S')
KEY_D = __ALL_KEYS.index('D')
KEY_A = __ALL_KEYS.index('A')
KEY_W = __ALL_KEYS.index('W')

KEYS       = [KEY_A, KEY_D]
ROBOT_KEYS = __ALL_ROBOT_KEYS
CTYPE_KEYS = __CTYPE_KEYS
NUMBER_OF_KEYS = len(ROBOT_KEYS)

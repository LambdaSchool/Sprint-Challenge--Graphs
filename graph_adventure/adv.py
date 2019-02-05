from room import Room
from player import Player
from world import World
from collections import deque

import random

# Load world
# DO NOT MODIFY
world = World()
roomGraph={496: [(5, 23), {'e': 457}], 457: [(6, 23), {'e': 361, 'w': 496}], 449: [(7, 20), {'e': 402}], 482: [(7, 21), {'e': 285}], 357: [(7, 22), {'n': 361, 'e': 270}], 361: [(7, 23), {'s': 357, 'w': 457}], 287: [(7, 24), {'e': 276}], 484: [(8, 14), {'e': 448}], 487: [(8, 15), {'e': 311}], 402: [(8, 20), {'e': 245, 'w': 449}], 285: [(8, 21), {'e': 176, 'w': 482}], 270: [(8, 22), {'e': 252, 'w': 357}], 341: [(8, 23), {'n': 276}], 276: [(8, 24), {'n': 322, 's': 341, 'e': 273, 'w': 287}], 322: [(8, 25), {'n': 332, 's': 276}], 332: [(8, 26), {'s': 322}], 448: [(9, 14), {'e': 352, 'w': 484}], 311: [(9, 15), {'e': 296, 'w': 487}], 368: [(9, 16), {'e': 359}], 395: [(9, 17), {'e': 326}], 342: [(9, 18), {'e': 266}], 336: [(9, 19), {'e': 251}], 245: [(9, 20), {'n': 176, 'w': 402}], 176: [(9, 21), {'s': 245, 'e': 128, 'w': 285}], 252: [(9, 22), {'e': 156, 'w': 270}], 289: [(9, 23), {'e': 225}], 273: [(9, 24), {'n': 292, 'e': 227, 'w': 276}], 292: [(9, 25), {'n': 381, 's': 273}], 381: [(9, 26), {'n': 440, 's': 292}], 440: [(9, 27), {'n': 471, 's': 381}], 471: [(9, 28), {'s': 440}], 352: [(10, 14), {'n': 296, 'e': 378, 'w': 448}], 296: [(10, 15), {'s': 352, 'e': 263, 'w': 311}], 359: [(10, 16), {'e': 217, 'w': 368}], 326: [(10, 17), {'e': 280, 'w': 395}], 266: [(10, 18), {'e': 233, 'w': 342}], 251: [(10, 19), {'e': 205, 'w': 336}], 267: [(10, 20), {'e': 166}], 128: [(10, 21), {'e': 116, 'w': 176}], 156: [(10, 22), {'e': 129, 'w': 252}], 225: [(10, 23), {'n': 227, 'e': 218, 'w': 289}], 227: [(10, 24), {'n': 286, 's': 225, 'w': 273}], 286: [(10, 25), {'n': 397, 's': 227}], 397: [(10, 26), {'s': 286, 'e': 427}], 499: [(10, 27), {'e': 465}], 423: [(11, 13), {'n': 378}], 378: [(11, 14), {'s': 423, 'w': 352}], 263: [(11, 15), {'n': 217, 'w': 296}], 217: [(11, 16), {'s': 263, 'e': 193, 'w': 359}], 280: [(11, 17), {'e': 184, 'w': 326}], 233: [(11, 18), {'n': 205, 'w': 266}], 205: [(11, 19), {'n': 166, 's': 233, 'w': 251}], 166: [(11, 20), {'s': 205, 'e': 165, 'w': 267}], 116: [(11, 21), {'n': 129, 'e': 111, 'w': 128}], 129: [(11, 22), {'n': 218, 's': 116, 'w': 156}], 218: [(11, 23), {'n': 221, 's': 129, 'w': 225}], 221: [(11, 24), {'n': 380, 's': 218, 'e': 235}], 380: [(11, 25), {'s': 221}], 427: [(11, 26), {'n': 465, 'e': 451, 'w': 397}], 465: [(11, 27), {'s': 427, 'w': 499}], 407: [(12, 13), {'e': 291}], 299: [(12, 14), {'e': 265}], 197: [(12, 15), {'n': 193}], 193: [(12, 16), {'n': 184, 's': 197, 'w': 217}], 184: [(12, 17), {'s': 193, 'e': 144, 'w': 280}], 223: [(12, 18), {'e': 105}], 147: [(12, 19), {'e': 142}], 165: [(12, 20), {'n': 111, 'w': 166}], 111: [(12, 21), {'n': 137, 's': 165, 'e': 110, 'w': 116}], 137: [(12, 22), {'n': 180, 's': 111, 'e': 171}], 180: [(12, 23), {'s': 137}], 235: [(12, 24), {'n': 272, 'w': 221}], 272: [(12, 25), {'s': 235}], 451: [(12, 26), {'w': 427}], 422: [(13, 12), {'n': 291}], 291: [(13, 13), {'n': 265, 's': 422, 'w': 407}], 265: [(13, 14), {'s': 291, 'e': 208, 'w': 299}], 229: [(13, 15), {'e': 160}], 228: [(13, 16), {'e': 136}], 144: [(13, 17), {'e': 119, 'w': 184}], 105: [(13, 18), {'n': 142, 'e': 72, 'w': 223}], 142: [(13, 19), {'s': 105, 'w': 147}], 185: [(13, 20), {'n': 110}], 110: [(13, 21), {'s': 185, 'e': 102, 'w': 111}], 171: [(13, 22), {'w': 137}], 210: [(13, 23), {'n': 239, 'e': 159}], 239: [(13, 24), {'n': 356, 's': 210}], 356: [(13, 25), {'s': 239}], 492: [(14, 10), {'n': 404}], 404: [(14, 11), {'n': 334, 's': 492}], 334: [(14, 12), {'n': 232, 's': 404}], 232: [(14, 13), {'n': 208, 's': 334}], 208: [(14, 14), {'n': 160, 's': 232, 'w': 265}], 160: [(14, 15), {'s': 208, 'e': 152, 'w': 229}], 136: [(14, 16), {'n': 119, 'w': 228}], 119: [(14, 17), {'n': 72, 's': 136, 'w': 144}], 72: [(14, 18), {'n': 60, 's': 119, 'w': 105}], 60: [(14, 19), {'n': 88, 's': 72, 'e': 57}], 88: [(14, 20), {'s': 60}], 102: [(14, 21), {'n': 140, 'e': 87, 'w': 110}], 140: [(14, 22), {'s': 102}], 159: [(14, 23), {'n': 199, 'e': 138, 'w': 210}], 199: [(14, 24), {'n': 278, 's': 159}], 278: [(14, 25), {'s': 199}], 485: [(14, 26), {'e': 369}], 410: [(15, 10), {'n': 350}], 350: [(15, 11), {'s': 410, 'e': 250}], 303: [(15, 12), {'n': 240}], 240: [(15, 13), {'s': 303, 'e': 195}], 162: [(15, 14), {'e': 154}], 152: [(15, 15), {'n': 150, 'w': 160}], 150: [(15, 16), {'s': 152, 'e': 118}], 109: [(15, 17), {'e': 95}], 65: [(15, 18), {'e': 62}], 57: [(15, 19), {'n': 70, 'e': 45, 'w': 60}], 70: [(15, 20), {'s': 57}], 87: [(15, 21), {'e': 71, 'w': 102}], 127: [(15, 22), {'n': 138, 'e': 79}], 138: [(15, 23), {'n': 271, 's': 127, 'w': 159}], 271: [(15, 24), {'n': 354, 's': 138}], 354: [(15, 25), {'s': 271}], 369: [(15, 26), {'e': 330, 'w': 485}], 444: [(15, 27), {'n': 477, 'e': 347}], 477: [(15, 28), {'s': 444}], 441: [(15, 29), {'e': 373}], 393: [(16, 10), {'n': 250, 'e': 466}], 250: [(16, 11), {'n': 236, 's': 393, 'w': 350}], 236: [(16, 12), {'n': 195, 's': 250}], 195: [(16, 13), {'n': 154, 's': 236, 'w': 240}], 154: [(16, 14), {'s': 195, 'e': 149, 'w': 162}], 151: [(16, 15), {'e': 115}], 118: [(16, 16), {'n': 95, 'w': 150}], 95: [(16, 17), {'n': 62, 's': 118, 'w': 109}], 62: [(16, 18), {'n': 45, 's': 95, 'w': 65}], 45: [(16, 19), {'s': 62, 'e': 28, 'w': 57}], 49: [(16, 20), {'n': 71, 'e': 35}], 71: [(16, 21), {'s': 49, 'w': 87}], 79: [(16, 22), {'n': 135, 'e': 56, 'w': 127}], 135: [(16, 23), {'n': 179, 's': 79}], 179: [(16, 24), {'n': 238, 's': 135}], 238: [(16, 25), {'n': 330, 's': 179}], 330: [(16, 26), {'s': 238, 'w': 369}], 347: [(16, 27), {'n': 349, 'e': 237, 'w': 444}], 349: [(16, 28), {'n': 373, 's': 347}], 373: [(16, 29), {'s': 349, 'w': 441}], 428: [(16, 30), {'n': 420}], 420: [(16, 31), {'n': 468, 's': 428, 'e': 331}], 468: [(16, 32), {'n': 470, 's': 420}], 470: [(16, 33), {'s': 468, 'e': 473}], 495: [(17, 9), {'n': 466}], 466: [(17, 10), {'s': 495, 'w': 393}], 269: [(17, 11), {'n': 246, 'e': 338}], 246: [(17, 12), {'n': 230, 's': 269}], 230: [(17, 13), {'n': 149, 's': 246}], 149: [(17, 14), {'n': 115, 's': 230, 'e': 196, 'w': 154}], 115: [(17, 15), {'n': 112, 's': 149, 'w': 151}], 112: [(17, 16), {'n': 41, 's': 115}], 41: [(17, 17), {'s': 112, 'e': 37}], 34: [(17, 18), {'n': 28}], 28: [(17, 19), {'s': 34, 'e': 27, 'w': 45}], 35: [(17, 20), {'e': 11, 'w': 49}], 67: [(17, 21), {'e': 7}], 56: [(17, 22), {'n': 69, 'e': 47, 'w': 79}], 69: [(17, 23), {'s': 56}], 125: [(17, 24), {'n': 206, 'e': 64}], 206: [(17, 25), {'s': 125}], 188: [(17, 26), {'e': 158}], 237: [(17, 27), {'n': 261, 'e': 207, 'w': 347}], 261: [(17, 28), {'n': 315, 's': 237, 'e': 277}], 315: [(17, 29), {'n': 318, 's': 261}], 318: [(17, 30), {'n': 331, 's': 315}], 331: [(17, 31), {'n': 467, 's': 318, 'w': 420}], 467: [(17, 32), {'s': 331}], 473: [(17, 33), {'n': 475, 'w': 470}], 475: [(17, 34), {'s': 473}], 338: [(18, 11), {'w': 269, 'e': 403}], 241: [(18, 12), {'n': 222, 'e': 374}], 222: [(18, 13), {'n': 196, 's': 241}], 196: [(18, 14), {'s': 222, 'w': 149}], 141: [(18, 15), {'e': 114}], 55: [(18, 16), {'n': 37}], 37: [(18, 17), {'n': 24, 's': 55, 'w': 41}], 24: [(18, 18), {'s': 37, 'e': 19}], 27: [(18, 19), {'n': 11, 'w': 28}], 11: [(18, 20), {'s': 27, 'e': 3, 'w': 35}], 7: [(18, 21), {'n': 47, 'e': 6, 'w': 67}], 47: [(18, 22), {'n': 52, 's': 7, 'w': 56}], 52: [(18, 23), {'n': 64, 's': 47}], 64: [(18, 24), {'s': 52, 'w': 125}], 104: [(18, 25), {'n': 158, 'e': 91}], 158: [(18, 26), {'n': 207, 's': 104, 'w': 188}], 207: [(18, 27), {'s': 158, 'w': 237}], 277: [(18, 28), {'n': 329, 'w': 261}], 329: [(18, 29), {'n': 372, 's': 277}], 372: [(18, 30), {'n': 418, 's': 329, 'e': 382}], 418: [(18, 31), {'n': 455, 's': 372}], 455: [(18, 32), {'n': 464, 's': 418}], 464: [(18, 33), {'n': 483, 's': 455, 'e': 493}], 483: [(18, 34), {'s': 464}], 403: [(19, 11), {'e': 367, 'w': 338}], 374: [(19, 12), {'w': 241}], 256: [(19, 13), {'n': 163}], 163: [(19, 14), {'n': 114, 's': 256, 'e': 168}], 114: [(19, 15), {'n': 54, 's': 163, 'e': 130, 'w': 141}], 54: [(19, 16), {'n': 46, 's': 114}], 46: [(19, 17), {'s': 54, 'e': 31}], 19: [(19, 18), {'n': 15, 'w': 24}], 15: [(19, 19), {'n': 3, 's': 19}], 3: [(19, 20), {'s': 15, 'e': 0, 'w': 11}], 6: [(19, 21), {'n': 9, 'e': 2, 'w': 7}], 9: [(19, 22), {'n': 61, 's': 6}], 61: [(19, 23), {'s': 9}], 84: [(19, 24), {'n': 91, 'e': 30}], 91: [(19, 25), {'n': 120, 's': 84, 'w': 104}], 120: [(19, 26), {'s': 91}], 175: [(19, 27), {'e': 121}], 312: [(19, 28), {'n': 370, 'e': 219}], 370: [(19, 29), {'s': 312}], 382: [(19, 30), {'n': 474, 'w': 372, 'e': 408}], 474: [(19, 31), {'n': 491, 's': 382}], 491: [(19, 32), {'s': 474}], 493: [(19, 33), {'n': 497, 'w': 464}], 497: [(19, 34), {'s': 493}], 367: [(20, 11), {'e': 324, 'w': 403}], 388: [(20, 12), {'n': 279}], 279: [(20, 13), {'s': 388, 'e': 247}], 168: [(20, 14), {'w': 163}], 130: [(20, 15), {'e': 167, 'w': 114}], 85: [(20, 16), {'n': 31}], 31: [(20, 17), {'n': 12, 's': 85, 'w': 46}], 12: [(20, 18), {'n': 5, 's': 31}], 5: [(20, 19), {'n': 0, 's': 12, 'e': 10}], 0: [(20, 20), {'n': 2, 's': 5, 'e': 1, 'w': 3}], 2: [(20, 21), {'n': 8, 's': 0, 'e': 4, 'w': 6}], 8: [(20, 22), {'n': 14, 's': 2, 'e': 17}], 14: [(20, 23), {'n': 30, 's': 8, 'e': 18}], 30: [(20, 24), {'n': 98, 's': 14, 'w': 84}], 98: [(20, 25), {'n': 113, 's': 30}], 113: [(20, 26), {'n': 121, 's': 98}], 121: [(20, 27), {'n': 219, 's': 113, 'w': 175}], 219: [(20, 28), {'s': 121, 'w': 312}], 293: [(20, 29), {'e': 259}], 408: [(20, 30), {'e': 268, 'w': 382}], 498: [(21, 10), {'e': 459}], 324: [(21, 11), {'n': 288, 'w': 367}], 288: [(21, 12), {'n': 247, 's': 324}], 247: [(21, 13), {'n': 202, 's': 288, 'w': 279}], 202: [(21, 14), {'n': 167, 's': 247}], 167: [(21, 15), {'s': 202, 'e': 200, 'w': 130}], 82: [(21, 16), {'n': 32}], 32: [(21, 17), {'n': 13, 's': 82, 'e': 86}], 13: [(21, 18), {'n': 10, 's': 32, 'e': 26}], 10: [(21, 19), {'s': 13, 'e': 16, 'w': 5}], 1: [(21, 20), {'e': 21, 'w': 0}], 4: [(21, 21), {'e': 38, 'w': 2}], 17: [(21, 22), {'e': 20, 'w': 8}], 18: [(21, 23), {'n': 23, 'e': 22, 'w': 14}], 23: [(21, 24), {'n': 40, 's': 18, 'e': 36}], 40: [(21, 25), {'n': 83, 's': 23}], 83: [(21, 26), {'n': 126, 's': 40}], 126: [(21, 27), {'n': 203, 's': 83}], 203: [(21, 28), {'n': 259, 's': 126}], 259: [(21, 29), {'n': 268, 's': 203, 'e': 301, 'w': 293}], 268: [(21, 30), {'n': 438, 's': 259, 'w': 408}], 438: [(21, 31), {'n': 443, 's': 268}], 443: [(21, 32), {'s': 438}], 489: [(22, 9), {'n': 459}], 459: [(22, 10), {'s': 489, 'e': 447, 'w': 498}], 300: [(22, 11), {'n': 295, 'e': 364}], 295: [(22, 12), {'n': 281, 's': 300}], 281: [(22, 13), {'n': 255, 's': 295}], 255: [(22, 14), {'n': 200, 's': 281, 'e': 260}], 200: [(22, 15), {'s': 255, 'w': 167}], 96: [(22, 16), {'n': 86}], 86: [(22, 17), {'s': 96, 'w': 32}], 26: [(22, 18), {'e': 58, 'w': 13}], 16: [(22, 19), {'e': 25, 'w': 10}], 21: [(22, 20), {'w': 1}], 38: [(22, 21), {'e': 43, 'w': 4}], 20: [(22, 22), {'w': 17}], 22: [(22, 23), {'e': 50, 'w': 18}], 36: [(22, 24), {'n': 39, 'w': 23}], 39: [(22, 25), {'n': 107, 's': 36}], 107: [(22, 26), {'s': 39}], 157: [(22, 27), {'e': 133}], 153: [(22, 28), {'e': 139}], 301: [(22, 29), {'n': 333, 'w': 259}], 333: [(22, 30), {'n': 415, 's': 301}], 415: [(22, 31), {'s': 333}], 447: [(23, 10), {'n': 364, 'w': 459}], 364: [(23, 11), {'s': 447, 'w': 300}], 363: [(23, 12), {'n': 284}], 284: [(23, 13), {'n': 260, 's': 363, 'e': 345}], 260: [(23, 14), {'s': 284, 'w': 255}], 244: [(23, 15), {'e': 187}], 146: [(23, 16), {'n': 100, 'e': 161}], 100: [(23, 17), {'n': 58, 's': 146}], 58: [(23, 18), {'s': 100, 'e': 75, 'w': 26}], 25: [(23, 19), {'n': 29, 'w': 16}], 29: [(23, 20), {'s': 25, 'e': 33}], 43: [(23, 21), {'n': 48, 'e': 53, 'w': 38}], 48: [(23, 22), {'s': 43}], 50: [(23, 23), {'n': 51, 'w': 22}], 51: [(23, 24), {'n': 74, 's': 50, 'e': 63}], 74: [(23, 25), {'n': 117, 's': 51}], 117: [(23, 26), {'n': 133, 's': 74}], 133: [(23, 27), {'s': 117, 'w': 157}], 139: [(23, 28), {'n': 174, 'e': 124, 'w': 153}], 174: [(23, 29), {'n': 351, 's': 139}], 351: [(23, 30), {'n': 384, 's': 174}], 384: [(23, 31), {'s': 351}], 406: [(23, 32), {'e': 391}], 494: [(24, 11), {'n': 358}], 358: [(24, 12), {'n': 345, 's': 494}], 345: [(24, 13), {'s': 358, 'w': 284}], 213: [(24, 14), {'n': 187}], 187: [(24, 15), {'n': 161, 's': 213, 'w': 244}], 161: [(24, 16), {'s': 187, 'w': 146}], 123: [(24, 17), {'n': 75}], 75: [(24, 18), {'s': 123, 'e': 80, 'w': 58}], 44: [(24, 19), {'n': 33, 'e': 73}], 33: [(24, 20), {'s': 44, 'e': 42, 'w': 29}], 53: [(24, 21), {'n': 66, 'e': 68, 'w': 43}], 66: [(24, 22), {'s': 53, 'e': 92}], 76: [(24, 23), {'n': 63, 'e': 77}], 63: [(24, 24), {'n': 81, 's': 76, 'e': 78, 'w': 51}], 81: [(24, 25), {'n': 89, 's': 63, 'e': 90}], 89: [(24, 26), {'n': 93, 's': 81, 'e': 131}], 93: [(24, 27), {'n': 124, 's': 89, 'e': 143}], 124: [(24, 28), {'n': 231, 's': 93, 'w': 139}], 231: [(24, 29), {'s': 124}], 307: [(24, 30), {'e': 204}], 327: [(24, 31), {'n': 391, 'e': 320}], 391: [(24, 32), {'s': 327, 'w': 406}], 452: [(25, 12), {'e': 353}], 283: [(25, 13), {'n': 262}], 262: [(25, 14), {'n': 183, 's': 283, 'e': 282}], 183: [(25, 15), {'n': 164, 's': 262, 'e': 216}], 164: [(25, 16), {'s': 183, 'e': 155}], 134: [(25, 17), {'n': 80}], 80: [(25, 18), {'s': 134, 'e': 99, 'w': 75}], 73: [(25, 19), {'e': 97, 'w': 44}], 42: [(25, 20), {'e': 59, 'w': 33}], 68: [(25, 21), {'e': 103, 'w': 53}], 92: [(25, 22), {'w': 66}], 77: [(25, 23), {'e': 106, 'w': 76}], 78: [(25, 24), {'e': 101, 'w': 63}], 90: [(25, 25), {'e': 94, 'w': 81}], 131: [(25, 26), {'e': 148, 'w': 89}], 143: [(25, 27), {'n': 178, 'w': 93}], 178: [(25, 28), {'n': 186, 's': 143}], 186: [(25, 29), {'n': 204, 's': 178}], 204: [(25, 30), {'n': 320, 's': 186, 'w': 307}], 320: [(25, 31), {'s': 204, 'w': 327}], 387: [(25, 32), {'n': 386}], 386: [(25, 33), {'n': 439, 's': 387, 'e': 360}], 439: [(25, 34), {'s': 386}], 353: [(26, 12), {'n': 305, 'w': 452}], 305: [(26, 13), {'n': 282, 's': 353, 'e': 343}], 282: [(26, 14), {'s': 305, 'e': 314, 'w': 262}], 216: [(26, 15), {'e': 319, 'w': 183}], 155: [(26, 16), {'n': 122, 'w': 164}], 122: [(26, 17), {'n': 99, 's': 155, 'e': 145}], 99: [(26, 18), {'s': 122, 'e': 172, 'w': 80}], 97: [(26, 19), {'w': 73}], 59: [(26, 20), {'e': 132, 'w': 42}], 103: [(26, 21), {'n': 190, 'w': 68}], 190: [(26, 22), {'s': 103, 'e': 191}], 106: [(26, 23), {'w': 77}], 101: [(26, 24), {'e': 108, 'w': 78}], 94: [(26, 25), {'w': 90}], 148: [(26, 26), {'n': 170, 'e': 189, 'w': 131}], 170: [(26, 27), {'n': 177, 's': 148, 'e': 198}], 177: [(26, 28), {'n': 181, 's': 170}], 181: [(26, 29), {'s': 177, 'e': 201}], 226: [(26, 30), {'n': 242, 'e': 214}], 242: [(26, 31), {'n': 328, 's': 226}], 328: [(26, 32), {'n': 360, 's': 242, 'e': 362}], 360: [(26, 33), {'n': 426, 's': 328, 'w': 386}], 426: [(26, 34), {'s': 360}], 421: [(27, 11), {'n': 401}], 401: [(27, 12), {'n': 343, 's': 421}], 343: [(27, 13), {'s': 401, 'e': 431, 'w': 305}], 314: [(27, 14), {'w': 282}], 319: [(27, 15), {'e': 344, 'w': 216}], 339: [(27, 16), {'n': 145}], 145: [(27, 17), {'s': 339, 'e': 215, 'w': 122}], 172: [(27, 18), {'w': 99}], 173: [(27, 19), {'n': 132, 'e': 182}], 132: [(27, 20), {'n': 169, 's': 173, 'e': 212, 'w': 59}], 169: [(27, 21), {'s': 132}], 191: [(27, 22), {'n': 192, 'e': 194, 'w': 190}], 192: [(27, 23), {'s': 191, 'e': 294}], 108: [(27, 24), {'n': 209, 'e': 249, 'w': 101}], 209: [(27, 25), {'s': 108, 'e': 248}], 189: [(27, 26), {'w': 148}], 198: [(27, 27), {'n': 234, 'w': 170}], 234: [(27, 28), {'s': 198, 'e': 297}], 201: [(27, 29), {'n': 214, 'w': 181}], 214: [(27, 30), {'n': 313, 's': 201, 'e': 220, 'w': 226}], 313: [(27, 31), {'s': 214, 'e': 321}], 362: [(27, 32), {'n': 409, 'w': 328}], 409: [(27, 33), {'n': 425, 's': 362}], 425: [(27, 34), {'n': 450, 's': 409}], 450: [(27, 35), {'s': 425}], 479: [(28, 12), {'n': 431}], 431: [(28, 13), {'s': 479, 'w': 343}], 414: [(28, 14), {'n': 344}], 344: [(28, 15), {'s': 414, 'e': 392, 'w': 319}], 316: [(28, 16), {'n': 215, 'e': 355}], 215: [(28, 17), {'s': 316, 'e': 243, 'w': 145}], 308: [(28, 18), {'n': 182}], 182: [(28, 19), {'s': 308, 'w': 173}], 212: [(28, 20), {'e': 253, 'w': 132}], 224: [(28, 21), {'n': 194}], 194: [(28, 22), {'s': 224, 'e': 211, 'w': 191}], 294: [(28, 23), {'w': 192}], 249: [(28, 24), {'e': 264, 'w': 108}], 248: [(28, 25), {'e': 335, 'w': 209}], 379: [(28, 26), {'n': 304}], 304: [(28, 27), {'n': 297, 's': 379, 'e': 337}], 297: [(28, 28), {'s': 304, 'w': 234}], 257: [(28, 29), {'n': 220, 'e': 298}], 220: [(28, 30), {'s': 257, 'w': 214}], 321: [(28, 31), {'n': 323, 'e': 394, 'w': 313}], 323: [(28, 32), {'n': 383, 's': 321, 'e': 405}], 383: [(28, 33), {'n': 478, 's': 323}], 478: [(28, 34), {'s': 383}], 461: [(29, 13), {'n': 430, 'e': 481}], 430: [(29, 14), {'n': 392, 's': 461, 'e': 458}], 392: [(29, 15), {'s': 430, 'w': 344}], 355: [(29, 16), {'e': 365, 'w': 316}], 243: [(29, 17), {'n': 274, 'w': 215}], 274: [(29, 18), {'s': 243, 'e': 340}], 306: [(29, 19), {'n': 253, 'e': 366}], 253: [(29, 20), {'n': 254, 's': 306, 'e': 310, 'w': 212}], 254: [(29, 21), {'s': 253, 'e': 275}], 211: [(29, 22), {'n': 290, 'e': 258, 'w': 194}], 290: [(29, 23), {'s': 211, 'e': 302}], 264: [(29, 24), {'e': 309, 'w': 249}], 335: [(29, 25), {'n': 371, 'w': 248}], 371: [(29, 26), {'s': 335, 'e': 411}], 337: [(29, 27), {'e': 389, 'w': 304}], 377: [(29, 28), {'n': 298, 'e': 412}], 298: [(29, 29), {'n': 399, 's': 377, 'w': 257}], 399: [(29, 30), {'s': 298}], 394: [(29, 31), {'e': 416, 'w': 321}], 405: [(29, 32), {'n': 419, 'w': 323}], 419: [(29, 33), {'s': 405}], 481: [(30, 13), {'w': 461}], 458: [(30, 14), {'w': 430}], 365: [(30, 16), {'w': 355}], 346: [(30, 17), {'n': 340, 'e': 390}], 340: [(30, 18), {'s': 346, 'e': 445, 'w': 274}], 366: [(30, 19), {'e': 375, 'w': 306}], 310: [(30, 20), {'e': 424, 'w': 253}], 275: [(30, 21), {'e': 453, 'w': 254}], 258: [(30, 22), {'w': 211}], 302: [(30, 23), {'e': 317, 'w': 290}], 309: [(30, 24), {'n': 376, 'w': 264}], 376: [(30, 25), {'s': 309}], 411: [(30, 26), {'e': 417, 'w': 371}], 389: [(30, 27), {'e': 396, 'w': 337}], 412: [(30, 28), {'w': 377}], 454: [(30, 29), {'e': 435}], 429: [(30, 30), {'n': 416, 'e': 442}], 416: [(30, 31), {'n': 476, 's': 429, 'w': 394}], 476: [(30, 32), {'s': 416}], 486: [(31, 16), {'n': 390}], 390: [(31, 17), {'s': 486, 'e': 456, 'w': 346}], 445: [(31, 18), {'e': 462, 'w': 340}], 375: [(31, 19), {'w': 366}], 424: [(31, 20), {'w': 310}], 453: [(31, 21), {'w': 275}], 348: [(31, 22), {'n': 317}], 317: [(31, 23), {'n': 325, 's': 348, 'e': 385, 'w': 302}], 325: [(31, 24), {'n': 400, 's': 317, 'e': 398}], 400: [(31, 25), {'s': 325}], 417: [(31, 26), {'w': 411}], 396: [(31, 27), {'n': 432, 'e': 413, 'w': 389}], 432: [(31, 28), {'n': 435, 's': 396, 'e': 433}], 435: [(31, 29), {'s': 432, 'e': 488, 'w': 454}], 442: [(31, 30), {'w': 429}], 456: [(32, 17), {'w': 390}], 462: [(32, 18), {'w': 445}], 480: [(32, 22), {'n': 385}], 385: [(32, 23), {'s': 480, 'e': 460, 'w': 317}], 398: [(32, 24), {'n': 472, 'e': 437, 'w': 325}], 472: [(32, 25), {'s': 398}], 469: [(32, 26), {'n': 413}], 413: [(32, 27), {'s': 469, 'e': 436, 'w': 396}], 433: [(32, 28), {'e': 434, 'w': 432}], 488: [(32, 29), {'w': 435}], 463: [(33, 22), {'n': 460}], 460: [(33, 23), {'s': 463, 'w': 385}], 437: [(33, 24), {'n': 490, 'w': 398}], 490: [(33, 25), {'s': 437}], 436: [(33, 27), {'w': 413}], 434: [(33, 28), {'e': 446, 'w': 433}], 446: [(34, 28), {'w': 434}]}
world.loadGraph(roomGraph)
player = Player("Name", world.startingRoom)
all_ends = []
for room in roomGraph:
    if len(roomGraph[room][1]) == 1:
        all_ends.append(room)
# all_ends = sorted(all_ends)
# all_ends = all_ends[::-1]
# print(all_ends)
# traversalPath = []
# unexploredExits = []
misc = []
do_not_enter_0 = []
do_not_enter_1 = []
# room_path = []
graph = {0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}}
# dirs = ['n', 'e', 'w', 's']
print('*' * 10)
inverse_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
def generateDirection(graph, curr_rm):
    for poss_exits in graph[curr_rm]:
        if graph[curr_rm][poss_exits] == '?':
            return poss_exits

def canTravel(direction):
    directions = player.currentRoom.getExits()
    if direction in directions:
        return True
    else:
        return False

def inverse(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'

#  starting_vertex = player.currentRoom.id
#  target = 

def bfs(self, starting_vertex, target): 
    visited = []
    queue = deque()
    queue.append([starting_vertex])
    
    while queue:    
        print('STARTING QUEUE')
        path = queue.popleft()
        print('PATH', path)
        last_node = path[-1:][0]
        print(last_node)
        if last_node not in visited:
            visited.append(last_node)
            print(last_node, path)
            # if last_node == target:
            #     return path
            # visited.append(last_node)
            for an_exit in graph[last_node]:
                print('AN EXIT', an_exit)
                if graph[last_node][an_exit] == target:
                    print('BFS path', path)
                    return path
                else: 
                    new_list = list(path)
                    new_list.append(an_exit)
                    queue.append(new_list)
    print('You are lost!!!!')
    return []

def room_to_directions(room_list):
    current_room = room_list[0]
    direction_list = []
    for room in room_list[1:]:
        for another_exit in graph[current_room]:
            print(graph[current_room])
            print(another_exit)
            if graph[current_room][another_exit] == room:
                direction_list.append(another_exit)
                current_room = room
                break
    return direction_list
    # return False


traversalPath = []
room_path = []
alt_path = []
unexploredExits = []
def travel(graph, currentPos, traversalPath, unexploredExits):
    while len(graph) < 13:
        print('Curr Room', player.currentRoom.id)
        # alt_path = traversalPath[:]

        # room_path.append(player.currentRoom.id)
        currentRoomExits = graph[player.currentRoom.id]
        print('Curr Exits', currentRoomExits, 'Actual', roomGraph[player.currentRoom.id][1])
        poss_directions = []
        for direction in currentRoomExits:
            if currentRoomExits[direction] == '?':
                unexploredExits.append(direction)
                poss_directions.append(direction)
        print(unexploredExits)
        print(poss_directions)
        if len(unexploredExits) > 0:
            if 'n' in poss_directions:
                move = 'n'
            elif 'e' in poss_directions:
                move = 'e'
            elif 'w' in poss_directions:
                move = 'w'
            elif 's' in poss_directions:
                move = 's'
            else:
                room_list = bfs(graph, player.currentRoom.id, '?')
                if not len(room_list):
                    return False
                print(room_to_directions(room_list))
                for next_direction in room_to_directions(room_list):
                    player.travel(next_direction)
                    traversalPath.append(next_direction)
            print(move)
            print(traversalPath)
            print(player.currentRoom.id)
                # break
            traversalPath.extend(move)
            previous_room_id = player.currentRoom.id
            player.travel(move)
            exitDictionary = {}
            for possible_exits in player.currentRoom.getExits():
                if possible_exits not in exitDictionary:
                    exitDictionary[possible_exits] = '?'
                    print('EXXXXIT', exitDictionary)
                elif possible_exits in exitDictionary:
                    print('*' * 30)

            print('SINGLE MOVE', move)
            graph[previous_room_id][move] = player.currentRoom.id
            print('RM', player.currentRoom.id, 'Curr Exits', currentRoomExits, 'Actual', roomGraph[player.currentRoom.id][1])
            
            print('EXIT DICT', exitDictionary)
            print(move)
            print(previous_room_id)

            opposite_way = inverse_directions[move]

            exitDictionary[opposite_way] = previous_room_id
            graph[player.currentRoom.id] = exitDictionary
            print(graph)
            print('ROOMS:', room_path)
            print('EXIT DICT', exitDictionary)
        else:
            print('HEEEEEERRRRRRRREEEEEEE')
    print(room_path)
    return traversalPath
travel(graph, 0, traversalPath, unexploredExits)















    # while len(graph) < 500:
    #     currentRoomExits = graph[player.currentRoom.id]
    #     print('Curr', player.currentRoom.id, roomGraph[player.currentRoom.id], currentRoomExits)
    #     poss_dirs = []
    #     for direction in currentRoomExits:
    #         if currentRoomExits[direction] == '?':
    #             unexploredExits.append(direction)
    #             poss_dirs.append(direction)
    #     if len(unexploredExits) > 0:    
    #         if len(poss_dirs) == 0 and len(currentRoomExits) == 1:
    #                 print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP', poss_dirs)
    #                 print(player.currentRoom.id, currentRoomExits, traversalPath)
    #                 randomExit = inverse_directions[traversalPath[-1:][0]]
    #                 print(randomExit)
    #                 traversalPath.append(randomExit)
    #                 previous_room_id = player.currentRoom.id
                    
    #                 exitDictionary = {}
    #                 for poss_exit in player.currentRoom.getExits():
    #                     print('XXXXXX', poss_exit, player.currentRoom.getExits())
    #                     exitDictionary[poss_exit] = '?'
    #                 player.travel(randomExit)
    #                 print('e', exitDictionary)
    #                 graph[previous_room_id][randomExit] = player.currentRoom.id
    #                 print('g', graph)
    #                 exitDictionary[inverse_directions[randomExit]] = previous_room_id
    #                 print('E', exitDictionary, previous_room_id, player.currentRoom.id)
    #                 graph[player.currentRoom.id] = exitDictionary
    #                 print('G', graph)
    #                 print(graph)
    #                 break
    #         else: 
 
    #             length = len(currentRoomExits)
    #             randomExit = random.choice(unexploredExits[-length + 1:])
    #             print('TRAVELED', randomExit)
    #             traversalPath.append(randomExit)
    #             print(traversalPath[-3:])
    #             previous_room_id = player.currentRoom.id
    #             print(previous_room_id)
    #             player.travel(randomExit)
    #             print(player.currentRoom.id)
    #             exitDictionary = {}
    #             for poss_exit in player.currentRoom.getExits():
    #                 print('XXXXXX', poss_exit)
    #                 exitDictionary[poss_exit] = '??'
    #             print('e', exitDictionary)
    #             graph[previous_room_id][randomExit] = player.currentRoom.id
    #             print('g', graph)
    #             exitDictionary[inverse_directions[randomExit]] = previous_room_id
    #             print('E', exitDictionary, previous_room_id, player.currentRoom.id)
    #             graph[player.currentRoom.id] = exitDictionary
    #             print('G', graph)
    #             # break
    #     # else:
    #     #     print('ELSE')
    #     #     while len(player.currentRoom.getExits()) < 2:
    #     #         player.travel(inverse_directions[randomExit])
    #     #     print('RRRRRRRRRRRRRRRRRRRRR', randomExit)
    #     #     return travel(graph, player.currentRoom, traversalPath, unexploredExits)
    # # print(sorted(misc))
    # # print(misc)
    # print(graph)
    # return traversalPath
# traversalPath = travel(graph, 0, traversalPath, unexploredExits)

# while len(graph) < 11:
#     # print('Curr Room', player.currentRoom.id)
#     direction = generateDirection(graph, player.currentRoom.id)
#     print(direction)
#     previous_room_id = player.currentRoom.id
#     # currentRoomExits = graph[player.currentRoom.id]
#     unexploredExits.append(player.currentRoom.id)
#     player.travel(direction)

#     if player.currentRoom.id not in graph:
#         exitmap = {}
#         for possible_exit in player.currentRoom.getExits():
#             exitmap[possible_exit] = '?'
#         graph[player.currentRoom.id] = exitmap

#     graph[player.currentRoom.id][inverse(direction)] = previous_room_id
#     graph[previous_room_id][direction] = player.currentRoom.id
#     # print(graph)
#     if canTravel(direction) == False:
#         print(graph)
#         print(direction)
#         break
#     break

print('*' * 10)
print(traversalPath)

# FILL THIS IN

# for d in dirs:
# temp_path = dfs(roomGraph, 0, 499)
# rooms_visited = (dfs2(roomGraph, 0, 499))
# print('T', temp_path)
# print(rooms_visited) # [0, 3, 11, 35, 49, 71, 87, 102, 110, 111, 116, 129, 218, 225, 227, 286,397, 427, 465, 499]
# traversalPath = ['n', 's', 'w', 'e', 'w', 'e', 'w', 's', 'w', 'e', 's', 'w', 'e', 'w', 'e', 'n', 'e', 's', 'w', 'w', 'e', 'n', 'w','e', 's', 'w', 'e', 'n', 's', 'w', 'e', 'n', 'w', 'e', 'w', 'e', 's', 'w', 'e', 'w', 'e', 'e', 'n', 'w', 'w', 'e', 'e', 'n', 's', 'w', 'w', 'e', 'w', 'e', 'w', 'e', 'n', 'e', 's', 'w', 'w', 'e', 'e', 'n', 's', 'w', 'n', 'w', 'e', 'e', 'n', 's', 'w', 'n', 'w', 'e', 'n', 's', 'w', 'e', 'e', 'n', 'n', 's', 's', 'n', 's', 'n', 's', 'n', 's', 's', 'n', 's', 's', 'e', 'n', 'w', 'e', 'w', 's', 'w']



# print('C', c)
# print(traversalPath)
# traversalPath = dfs(roomGraph, 0, 499)
# You may find the commands player.currentRoom.id, player.currentRoom.getExits() and player.travel(direction) useful.


# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    print('MOVE', move)
    player.travel(move)
    print('TRAVEL', player.travel)
    visited_rooms.add(player.currentRoom.id)
    print('VISITED', visited_rooms)

if len(visited_rooms) == 500:
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{500 - len(visited_rooms)} unvisited rooms")
    print(f"TESTS Failed: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")




#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")

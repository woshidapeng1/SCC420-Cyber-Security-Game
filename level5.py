import pygame
import re
import sys
from define import *
from classes import *

jjjjj = 0
placeholder_rects_L = []

blanks = ["phishing website", "antivirus software", "malware", 
          "intrusion detection system", "security awareness training", 
          "impersonation", "social engineering attacks"]


sentence = "    One day, you're working in the office and receive an email claiming to be from your IT department. \
The email contains a link and claims that you need to click to download an important software update. \
You notice that the email address doesn't look the same as your company's IT department, which might indicate \
that it's a ____________. You decide to contact the IT department directly to confirm whether \
this update is legitimate. You decide to first run a ____________ scan to ensure that your \
computer hasn't been infected by any potential ____________. You plan to recommend that the company invests \
in an ____________ to more effectively identify and prevent any future threats. \
You also plan to enhance the ____________ for your colleagues. During the training, \
you emphasize that if there are any doubts or uncertainty about the origin of an email, the sender should be \
contacted directly for confirmation. This is a key strategy to prevent ____________ and \
____________."

    
s1 = Level_5(20,450, blanks[0],False,False)
s2 = Level_5(200,450, blanks[1],False,False)
s3 = Level_5(20,475, blanks[2],False,False)
s4 = Level_5(200,475, blanks[3],False,False)
s5 = Level_5(20,500, blanks[4],False,False)
s6 = Level_5(200,500, blanks[5],False,False)
s7 = Level_5(20,525, blanks[6],False,False)
Level_5S_L = [s1,s2,s3,s4,s5,s6,s7]


sentence_parts = sentence.split("_____")

pattern = r"_{12}"


matches = re.finditer(pattern, sentence)
match_d = {}

placeholder_rects = []
xy = [[69,95],[236,134],[75,167],[155,188],[121,221],[130,293],[2,315]]
s = 0
for match in matches:
    start_index = match.start()
    end_index = match.end()
    

    text_surface = font.render(match.group(), True, BLACK)
    text_rect = text_surface.get_rect(width = 80,height = 10)
    match_d[s] = [text_rect,Level_5S_L[s].L_rect]
    text_rect.x = xy[s][0]
    text_rect.y = xy[s][1]
    s+=1
    

    placeholder_rects.append(text_rect)
print('djksjssssssssss',placeholder_rects)

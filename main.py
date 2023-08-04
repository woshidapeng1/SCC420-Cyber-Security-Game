import pygame
import sys
from define import *
from classes import *
from level1 import *
from level2 import *
from level3 import *
from level4 import *
from level5 import *
from level_hint import *

game_state = 'start5'
running = True
clock = pygame.time.Clock()
fps = 15
while running:
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
           
            
            if game_state == "menu":
                if check_button_click(mouse_pos, play_button_rect):
                    game_state = "level_selection"

                elif check_button_click(mouse_pos, hint_button_rect):
                    game_state = "hint"

                elif check_button_click(mouse_pos, about_button_rect):
                    game_state = "about"

            elif game_state == "level_selection":
                if check_button_click(mouse_pos,back_button_rect):
                    game_state = 'menu'
                for i in range(len(levels)):     
                    if check_button_click(mouse_pos,level_buttons_rect[i]) and level_pass[levels[i]]:
                        game_state = game_states[i]
                        # game_states.append(game_state)

                        break
                # print('game_state',game_states)
            elif game_state == "hint" or game_state == "about":
                if check_button_click(mouse_pos,back_button_rect):
                    game_state = 'menu'

            elif game_state == 'start1':

                for ball in balls:
                    if check_button_click(mouse_pos,ball.rect):
                        ball.ball_dragging = True
            elif game_state == 'start2':
                Level2_S.op_2(mouse_pos)
                if Level2_S.op_2(mouse_pos):
                    show_password_input()

                    level_pass['Level 3'] = True
                    print (level_pass)
                    over_message_box()
                    pygame.time.delay(2000)
                    pygame.display.flip()
                    game_state = 'level_selection'
            elif game_state == "start3":
                Level_3S_2.level3(mouse_pos)
                level_pass['Level 4'] = True
                print (level_pass)
                over_message_box()
                pygame.time.delay(2000)
                pygame.display.flip()
                game_state = 'level_selection'
            elif game_state == 'start4':
                Level4_S.op_4(mouse_pos)
                if Level4_S.op_4(mouse_pos):
                    game_state = 'start_level4_2'

            elif game_state == 'start_level4_2':
                Level4_S2.op(mouse_pos)
                if Level4_S2.op(mouse_pos):
                    level_pass['Level 5'] = True
                    print (level_pass)
                    over_message_box()
                    pygame.time.delay(2000)
                    pygame.display.flip()
                    game_state = 'level_selection'

            elif game_state == 'start5':
                for word_datas in Level_5S_L:
                    if check_button_click(mouse_pos,word_datas.L_rect):
                        word_datas.w_dragging = True
            
            elif game_state in game_states:
                if check_button_click(mouse_pos,start_button_rect):
                    
                    game_state = 'start%s'%(game_state[-1])

        elif event.type == pygame.MOUSEBUTTONUP:
            for ball in balls:
                if ball.ball_dragging:
                    ball.ball_dragging = False
                    break
            if game_state == 'start1':
                for ball in balls:
                    if not ball.ball_in:
                        for basket in baskets:
                            if ball.rect.colliderect(basket.rect):
                                ball.ball_in = True
                                num += 1
                                level1_dy[basket.category].append(ball.category)
                                print(level1_dy)
                                break
                if num == 8:
                    n = 0
                    print('num',num)
                    for basket in level1_dy:
                        for ball in level1_dy[basket]:
                            if ball in level1_d[basket]:
                                n += 1
                    if n == 8:
                        level_pass['Level 2'] = True
                        print (level_pass)
                        over_message_box()
                        pygame.time.delay(2000)
                        pygame.display.flip()
                        game_state = 'level_selection'

                    else:
                        ball1 = Ball(10, 150, "Trojans",25,False,False)
                        ball2 = Ball(110, 150, "Ddos",25,False,False)
                        ball3 = Ball(210, 150, "Phishing",25,False,False)
                        ball4 = Ball(310, 150, "Spyware",25,False,False)
                        ball5 = Ball(10, 300, "Spoofing",25,False,False)
                        ball6 = Ball(110, 300, "Viruses",25,False,False)
                        ball7 = Ball(210, 300, "Vishing",25,False,False)
                        ball8 = Ball(310, 300, "SQLi",25,False,False)
                       
                        balls = [ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8]
                        num = 0
                        level1_dy = {}
                        for basket in baskets:
                            level1_dy[basket.category] = []

                        game_state = 'start1'

                    pass_num[0] += 1
            for word_datas in Level_5S_L:
                if word_datas.w_dragging:
                    word_datas.w_dragging = False
                    break
            if game_state == 'start5':
                
                for i in range(len(placeholder_rects)):
                    for j in range(len(placeholder_rects)):
                        if not Level_5S_L[i].text_in:
                            # print('sdsssssssssssssss',Level_5S_L[i].L_rect)
                            # print('1222222222222222222',placeholder_rects)
                            if Level_5S_L[i].L_rect.colliderect(placeholder_rects[j]):
                                placeholder_rects_L.append(placeholder_rects[j])
                                print('placeholder_rects_L',placeholder_rects_L)
                                # if i == j:
                                Level_5S_L[i].text_in = True
                                # print('deiiiiiiiiiiiiiiiiiii')
                                
                                # print('jjjjjjjjjjjjjjjjjjjjj',Level_5S_L[i].text_in)
                                jjjjj+=1
                                break
                if jjjjj == 7:
                    y = 0
                    print('match_d',match_d)
                    for match in match_d:
                        if placeholder_rects_L[match] in match_d[match]:
                            y += 1
                    if y == 7:
                        over_message_box()
                        pygame.time.delay(2000)
                        pygame.display.flip()
                        game_state = 'winner'
                        print('Win！') 
                    else:
                        s1 = Level_5(20,450, blanks[0],False,False)
                        s2 = Level_5(200,450, blanks[1],False,False)
                        s3 = Level_5(20,475, blanks[2],False,False)
                        s4 = Level_5(200,475, blanks[3],False,False)
                        s5 = Level_5(20,500, blanks[4],False,False)
                        s6 = Level_5(200,500, blanks[5],False,False)
                        s7 = Level_5(20,525, blanks[6],False,False)
                        Level_5S_L = [s1,s2,s3,s4,s5,s6,s7]
                        jjjjj = 0
                        print('One more time')
                        game_state = 'start5'
            elif game_state == "start3":
                Level_3S_2.level3(mouse_pos)
                level_pass['Level 4'] = True
                print (level_pass)
                game_state = 'level_selection'    
    if game_state in game_states:
            
        bg_screen.draw(background_img)
            
        Le_Hint(Level1_hint_text_L[int(game_state[-1])-1])
            # Text
        text1_rect = pygame.Rect(115,280, re_img_width-20,re_img_height-50)

            # Text
        draw_text(screen, font, Level1_hint_text_L[int(game_state[-1])-1], (0,0,0), text1_rect)
        screen.blit(start_button_img,start_button_rect)
    elif game_state == "menu":
        # Draw Background and Button
        BUTTON_WIDTH = 220
        BUTTON_HEIGHT = 80
        BUTTON_MARGIN = 20
        bg_screen.draw_bg(background_img)
        # Text on Buttons
        bg_screen.draw_char()
        
    elif game_state == "level_selection":
        BUTTON_WIDTH = 220
        BUTTON_HEIGHT = 10
        BUTTON_MARGIN = 80
        
        screen.fill((255, 255, 255))
        screen.blit(background_img, (0, 0))
        for i in range(len(levels)):
            screen.blit(play_button_img, level_buttons_rect[i])
            if level_pass[levels[i]] == True:
                level_text = font.render(levels[i], True, (255,255,255))
            else:
                level_text = font.render(levels[i], True, (169,169,169))
            screen.blit(level_text, level_buttons_rect[i].move((BUTTON_WIDTH - level_text.get_width()) // 2, (BUTTON_HEIGHT + level_text.get_height()//2)))
        screen.blit(back_button_img,back_button_rect)
    elif game_state == "hint":
        bg_screen.draw(background_img)
        screen.blit(back_button_img,back_button_rect)
        draw_text(screen, font2, hint_text, WHITE, hint_text_rect)
    elif game_state == "about":
        bg_screen.draw(background_img)
        screen.blit(back_button_img,back_button_rect)
        draw_text(screen, font2, about_text, WHITE, hint_text_rect)
        
    
    elif game_state == 'start1':
        bg_screen.draw(background_img)
        basket1.draw()
        basket2.draw()
        basket3.draw()
        # 
        for ball in balls:
            if ball.ball_dragging:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                ball.rect.x = mouse_x
                ball.rect.y = mouse_y

        # # 
        for ball in balls:
            ball.draw()
    elif game_state == 'start2':
        bg_screen.draw(bg_2)
        sel = Level2_S.q()
        Level2_S.draw_op()
    elif game_state == "start3":
        bg_screen.draw(bg_3)
        Level_3S_2.draw_level3()
    elif game_state == 'start4':
        bg_screen.draw(bg_4)
        Level4_S.q()
        Level4_S.draw_op()
    elif game_state == 'start_level4_2':
        bg_screen.draw(bg_4)
        Level4_S2.q()
        Level4_S2.draw_op()
    elif game_state == 'start5':
        bg_screen.draw(bg_5)
        # Text 
        text_rect = pygame.Rect(10, 35, SCREEN_WIDTH-10, SCREEN_HEIGHT-40)

        # Draw Text
        draw_text(screen, font, sentence, (0,0,0), text_rect)
        for word_datas in Level_5S_L:
            if word_datas.w_dragging:
                
                mouse_x, mouse_y = pygame.mouse.get_pos()
                word_datas.L_rect.x = mouse_x
                word_datas.L_rect.y = mouse_y
                # print(mouse_x, mouse_y)
        for word_datas in Level_5S_L:
            word_datas.draw_op()
    elif game_state == 'winner':
        bg_screen.draw(bg_5)
        screen.blit(over_name,over_name_rect)
    clock.tick(fps)
    pygame.display.flip()

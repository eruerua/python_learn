import sys
import pygame

def check_events():
    #相应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship):
    #更新屏幕上的图像，并切换到新屏幕
    #每次循环重绘图像
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #最近绘制的图像可见
    pygame.display.flip()
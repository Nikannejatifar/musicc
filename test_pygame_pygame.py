import pygame  
import sys  

def create_black_key(screen, x, y):  
    # رنگ سیاه  
    black_color = (50, 55, 49)  # معادل رنگ "#323731"  
    
    # ابعاد کلید  
    key_width = 50  # عرض کلید  
    key_height = 180  # ارتفاع کلید  

    # رسم مستطیل (کلید سیاه)  
    pygame.draw.rect(screen, black_color, pygame.Rect(x, y, key_width, key_height))  

# راه‌اندازی Pygame  
pygame.init()  

# تنظیم ابعاد پنجره  
width, height = 400, 400  
screen = pygame.display.set_mode((width, height))  
pygame.display.set_caption("کلید سیاه با Pygame")  

# حلقه اصلی  
running = True  
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  

    # پر کردن پس‌زمینه با رنگ سفید  
    screen.fill((255, 255, 255))  

    # ایجاد و رسم کلید سیاه  
    create_black_key(screen, 175, 100)  # موقعیت دلخواه کلید  

    # به‌روزرسانی صفحه  
    pygame.display.flip()  

# بستن Pygame  
pygame.quit()  
sys.exit()  
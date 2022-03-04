from typing import Any, Union
import pygame as pg

pg.font.init()
font = pg.font.Font(None, 32)

# Text for info and instructions
text_weight = font.render('Peso:', False, (255, 255, 255))
text_height = font.render('Altura:', False, (255, 255, 255))
text_gender = font.render('Género:', False, (255, 255, 255))
text_instruction1 = font.render('Entrad 1 para chico y 0 para chica,', False, (255, 255, 255))
text_instruction2 = font.render('entonces su altura y peso.', False, (255, 255, 255))
text_cycle = font.render('Altura futura:', False, (255, 255, 255))          

screen = pg.display.set_mode((650, 750))
clock = pg.time.Clock()
input_box = pg.Rect(100, 100, 140, 32)
coverup = pg.Rect(650, 350, 100, 40)


def main():
    weight = 0
    height = 0
    gender = 0
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        if 220 > int(text) > 120:                           # assuming that everything above 120 is height
                            height = text
                        if 120 >= int(text) > 35:                           # assuming everything under 120 is weight
                            weight = text
                        if int(text) == 1:
                            gender = 'chico'
                        elif int(text) == 0:
                            gender = 'chica'
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        # Blit the instructions
        screen.blit(text_instruction1, (10, 20))
        screen.blit(text_instruction2, (10, 50))

        if weight != 0:
            screen.blit(text_weight, (230, 230))
            # Turn variable to str to be able to blit
            number_weight = font.render(str(weight), False, (255, 255, 255))
            screen.blit(number_weight, (320, 230))

        if height != 0:
            screen.blit(text_height, (230, 260))
            # Turn variable to str to be able to blit
            number_height = font.render(str(height), False, (255, 255, 255))
            screen.blit(number_height, (320, 260))

        if gender == 'chico':
            screen.blit(text_gender, (230, 290))
            kind_gender = font.render(gender, False, (255, 255, 255))
            screen.blit(kind_gender, (320, 290))

        if gender == 'chica':
            screen.blit(text_gender, (230, 290))
            kind_gender = font.render(gender, False, (255, 255, 255))
            screen.blit(kind_gender, (320, 290))

        guess = algo(weight, height, gender)

        if gender == 'chico':
            pg.draw.rect(screen, (30, 30, 30), coverup, 0)                          # cover up value to prevent overlap
            screen.blit(text_cycle, (230, 350))
            number_cycle = font.render(str(guess), False, (255, 255, 255))
            screen.blit(number_cycle, (400, 350))
        elif gender == 'chica':
            pg.draw.rect(screen, (30, 30, 30), coverup, 0)                          # cover up value to prevent overlap
            screen.blit(text_cycle, (230, 350))
            number_cycle = font.render(str(guess), False, (255, 255, 255))
            screen.blit(number_cycle, (400, 350))

        pg.display.flip()
        clock.tick(30)


def algo(weight, height, gender):
    # Algorithms don´t make sense, they just seem to do so
    # Algorithm for boys
    if gender == 'chico' and 20 < int(weight) <= 120 < int(height) < 220:
        guess = int(height)*(int(weight)/(int(weight)-6.5))
        if guess < int(height):
            guess = height + 5
        guess = round(guess, 2)
        return guess

    # Algorithm for girls
    if gender == 'chica' and 20 < int(weight) <= 120 < int(height) < 220:
        guess = int(height)*(int(weight)/(int(weight)-6))
        if guess < int(height):
            guess = height + 5
        guess = round(guess, 2)
        return guess


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()

import pygame

# create the pygame window
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Minigame Car")
# create a game where a car is moving
# create a car
car = pygame.image.load("car.png")
# create an obstacle
obstacle = pygame.image.load("rock.webp")
obstacle = pygame.transform.scale(obstacle, (100, 100))
# add a street background
street = pygame.image.load("street.png")
# set it as the background of the entire game

# set the car to the middle of the screen
car_x = 300
car_y = 300
car_x_change = 0
car_y_change = 0
# set the obstacle to the middle of the screen
obstacle_x = 150
obstacle_y = 150
obstacle_x_change = 0
obstacle_y_change = 0

# create a loop
running = True
while running:
    screen.blit(street, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                car_x_change = 0.5
            if event.key == pygame.K_UP:
                car_y_change = -0.5
            if event.key == pygame.K_DOWN:
                car_y_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                car_y_change = 0
            # if the car hits the obstacle do a game over
            if car_x == obstacle_x and car_y == obstacle_y:
                game_over = True
                print("Game Over")
            # if the car is not on the screen do a game over
            if car_x < 0 or car_x > 600 or car_y < 0 or car_y > 600:
                game_over = True
                print("Game Over")
        #add an obstacle to the game
    car_x += car_x_change
    car_y += car_y_change
    obstacle_x += obstacle_x_change
    obstacle_y += obstacle_y_change
    screen.blit(car, (car_x, car_y))
    screen.blit(obstacle, (obstacle_x, obstacle_y))
    pygame.display.update()
pygame.quit()
quit()



import numpy as np
import code_for_hw3_part2 as hw3

mnist_data_all = hw3.load_mnist_data(range(10))
print('mnist_data_all loaded. shape of single images is', mnist_data_all[0]["images"][0].shape)

def raw_mnist_features(x):
    """
    @param x (n_samples,m,n) array with values in (0,1)
    @return (m*n,n_samples) reshaped array where each entry is preserved
    """
    (t, m, n) = np.shape(x)
    return x.reshape(t, -1).T

def row_differential(x):
    """
    @param x (n_samples,m,n) array with values in (0,1)
    @return (m(n-1),n_samples) array
    """
    (t, m, n) = np.shape(x)
    d = np.zeros((t, m, n - 1))
    for i in range(t):
        for j in range(m):
            for k in range(n - 1):
                d[i][j][k] = x[i][j][k + 1] - x[i][j][k]
    return raw_mnist_features(d)

def get_classifier(a, b):
    d0 = mnist_data_all[a]["images"]
    d1 = mnist_data_all[b]["images"]
    y0 = np.repeat(-1, len(d0)).reshape(1,-1)
    y1 = np.repeat(1, len(d1)).reshape(1,-1)

    data = row_differential(np.vstack((d0, d1)))
    labels = np.vstack((y0.T, y1.T)).T
    
    acc = hw3.xval_learning_alg(hw3.perceptron, data, labels, 10, {'T': 50})
    print(a, b, " accuracy ", acc)
    th, th0 = hw3.perceptron(data, labels, {'T': 50})
    return (th, th0)

A = 9
B = 0
th, th0 = get_classifier(A, B)



# for i in range(10):
#     th.append(0)
#     th0.append(0)
#     print("train classifier of digit {0} ...".format(i), end='', flush=True)
#     th[i], th0[i] = get_classifier(i)
#     print("  done")

#-------------------------------------------------------------------------------
# Interactive Window
#------------------------------------------------------------------------------- 

import pygame.event, pygame.draw

pygame.init()

width, height = 1500, 500
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Perceptron")
timer = pygame.time.Clock() 

# defining colours 
WHITE = (255, 255, 255) 
GREY = (192, 192, 192) 
BLACK = (0, 0, 0)

bg_active_color = WHITE 
screen.fill(WHITE) 

BOX_EVENT = pygame.USEREVENT + 1

# create canvas
N = 28
box_width = 15
box_margin = 10
box_thickness = 2
box = []
empty_canvas = [[0 for i in range(N)] for j in range(N)]
canvas = mnist_data_all[A]["images"][0][:,:]


for i in range(N):
    box.append([])
    for j in range(N):
        x = box_margin + i * box_width
        y = box_margin + j * box_width
        r = box_width + box_thickness
        box[i].append(pygame.draw.rect(screen, BLACK, (x, y, r, r), box_thickness))

# create clear and classify button
font = pygame.font.SysFont('Ubuntu Mono', 28)

clear_text = font.render('Clear Grid', True, BLACK, GREY)
clear_rect = clear_text.get_rect()
clear_rect.center = (450 + clear_rect.width / 2, 10 + clear_rect.height / 2)

classify_text = font.render('Classify', True, BLACK, GREY)
classify_rect = classify_text.get_rect()
classify_rect.center = (450 + classify_rect.width / 2, 100 + classify_rect.height / 2)

prediction = ''
result_text = font.render(prediction, True, BLACK, WHITE)
result_rect = result_text.get_rect()
result_rect.center = (450 + result_rect.width / 2, 200 + result_rect.height / 2)

running = True
while running: 
    
    screen.fill(WHITE)
    screen.blit(clear_text, clear_rect)
    screen.blit(classify_text, classify_rect)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            (x, y) = pygame.mouse.get_pos()
            if clear_rect.collidepoint(mouseX, mouseY):
                canvas = [row[:] for row in empty_canvas]
                prediction = ''

            if classify_rect.collidepoint(mouseX, mouseY):
                x = np.array([canvas])
                x = row_differential(1 - x)
                win = [0 for i in range(10)]

                if ((np.dot(th.T, x) + th0) / np.dot(th.T, th)) <= 0:
                    digit = A
                else:
                    digit = B
                prediction = "{} ({} or {})".format(digit, A, B)
        if not pygame.mouse.get_pressed()[0]:
            continue

        if BOX_EVENT <= event.type and event.type < BOX_EVENT + N * N: 
            offset = event.type - BOX_EVENT
            i = offset // N
            j = offset % N
            canvas[i][j] = 1

    result_text = font.render(prediction, True, BLACK, WHITE)
    result_rect = result_text.get_rect()
    result_rect.center = (450 + result_rect.width / 2, 200 + result_rect.height / 2)
    screen.blit(result_text, result_rect)


    mouseX, mouseY = pygame.mouse.get_pos()
    for i in range(N):
        for j in range(N):
            if canvas[i][j] == 1:
                pygame.draw.rect(screen, BLACK, box[i][j])
            else:
                pygame.draw.rect(screen, BLACK, box[i][j], box_thickness)
            r = box_width + box_thickness
            centerX = box_margin + i * box_width + r // 2
            centerY = box_margin + j * box_width + r // 2
            # enough near
            if (centerX - mouseX) * (centerX - mouseX) + (centerY - mouseY) * (centerY - mouseY) <= 1.3 * 1.3 * box_width * box_width:
                pygame.event.post(pygame.event.Event(BOX_EVENT + i * N + j))

    pygame.display.update() 
    timer.tick(120) 

pygame.quit() 

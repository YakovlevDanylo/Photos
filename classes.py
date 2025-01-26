class Sprite(sprite.Sprite):
    def __init__(self, filename, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player1(Sprite):
    def update(self, screen):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 640:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 440:
            self.rect.y += self.speed
        super().update(screen)

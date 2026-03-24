
import streamlit as st
import pygame
import random
import time
import numpy as np
from PIL import Image

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class SnakeGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (GRID_SIZE, 0)
        self.food = self._place_food()
        self.score = 0
        self.game_over = False

    def _place_food(self):
        while True:
            food = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                    random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
            if food not in self.snake:
                return food

    def step(self, action=None):
        if action:
            self.direction = action

        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

        # Check collisions
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in self.snake):
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self._place_food()
        else:
            self.snake.pop()

    def get_frame(self):
        surface = pygame.Surface((WIDTH, HEIGHT))
        surface.fill(BLACK)
        
        # Draw snake
        for segment in self.snake:
            pygame.draw.rect(surface, GREEN, (*segment, GRID_SIZE - 2, GRID_SIZE - 2))
            
        # Draw food
        pygame.draw.rect(surface, RED, (*self.food, GRID_SIZE - 2, GRID_SIZE - 2))
        
        # Convert to image
        img_str = pygame.image.tostring(surface, "RGB")
        return Image.frombytes("RGB", (WIDTH, HEIGHT), img_str)

# Streamlit App
st.set_page_config(page_title="Streamlit Snake Game", page_icon="🐍")

st.title("🐍 Snake Game Stream")
st.write("Control the snake using the buttons below!")

if 'game' not in st.session_state:
    st.session_state.game = SnakeGame()
    st.session_state.running = False

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("Start / Reset"):
        st.session_state.game.reset()
        st.session_state.running = True

with col2:
    if st.button("Stop"):
        st.session_state.running = False

# Game loop placeholder
frame_placeholder = st.empty()
score_placeholder = st.empty()

# Controls
st.markdown("### Controls")
c1, c2, c3 = st.columns(3)
with c2:
    if st.button("⬆️"): st.session_state.game.direction = (0, -GRID_SIZE)
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("⬅️"): st.session_state.game.direction = (-GRID_SIZE, 0)
with c3:
    if st.button("➡️"): st.session_state.game.direction = (GRID_SIZE, 0)
c1, c2, c3 = st.columns(3)
with c2:
    if st.button("⬇️"): st.session_state.game.direction = (0, GRID_SIZE)

# Main Loop
if st.session_state.running:
    while not st.session_state.game.game_over:
        st.session_state.game.step()
        frame = st.session_state.game.get_frame()
        frame_placeholder.image(frame, use_container_width=True)
        score_placeholder.write(f"Score: {st.session_state.game.score}")
        time.sleep(1/FPS)
        
        if st.session_state.game.game_over:
            st.error(f"Game Over! Final Score: {st.session_state.game.score}")
            st.session_state.running = False
            break
else:
    frame = st.session_state.game.get_frame()
    frame_placeholder.image(frame, use_container_width=True)
    score_placeholder.write(f"Score: {st.session_state.game.score}")

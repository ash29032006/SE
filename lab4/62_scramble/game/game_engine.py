import random
import pygame
from game.text_box import TextBox


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.words = ["PYTHON", "PYGAME", "PLANET", "ROCKET", "GALAXY", "STREAM", "PUZZLE", "ALGORITHM"]
        self.secret_word = ""
        self.scrambled_word = ""

        self.score = 0
        self.feedback_msg = "Unscramble the letters above!"
        self.feedback_color = (210, 215, 225)

        # Task 2: Hint System variables
        self.revealed_hints = 0

        # Task 3: Countdown Timer (20 seconds)
        self.round_duration = 20.0
        self.round_start_ticks = 0
        self.time_left = 20.0
        self.times_up = False
        self.times_up_timer = 0

        # Task 4: Letter Tiles Rack & Drag-and-Drop / Click sorting
        self.tile_letters = []
        self.selected_tile_idx = None
        self.dragging_tile_idx = None
        self.drag_mouse_offset = (0, 0)
        self.drag_current_pos = (0, 0)
        self.tile_size = 52
        self.tile_gap = 12
        self.tile_rack_y = 120

        # Controls & Buttons
        self.input_box = TextBox(width // 2 - 180, 270, 160, 44)
        self.submit_btn = pygame.Rect(width // 2 - 5, 270, 95, 44)
        self.hint_btn = pygame.Rect(width // 2 + 105, 270, 85, 44)

        # Fonts
        self.font_title = pygame.font.SysFont(None, 40)
        self.font_word = pygame.font.SysFont(None, 38)
        self.font_hint = pygame.font.SysFont(None, 34)
        self.font_msg = pygame.font.SysFont(None, 26)
        self.font_btn = pygame.font.SysFont(None, 24)
        self.font_timer = pygame.font.SysFont(None, 22)
        self.font_small = pygame.font.SysFont(None, 20)

        self.next_round()

    def scramble_string(self, word):
        letters = list(word)
        while True:
            random.shuffle(letters)
            shuffled = "".join(letters)
            if shuffled != word or len(word) <= 1:
                return shuffled

    def get_tile_rect(self, index, total_tiles):
        total_w = total_tiles * self.tile_size + (total_tiles - 1) * self.tile_gap
        start_x = (self.width - total_w) // 2
        tile_x = start_x + index * (self.tile_size + self.tile_gap)
        return pygame.Rect(tile_x, self.tile_rack_y, self.tile_size, self.tile_size)

    def next_round(self):
        self.secret_word = random.choice(self.words)
        self.scrambled_word = self.scramble_string(self.secret_word)
        self.input_box.clear()

        # Reset hints
        self.revealed_hints = 0

        # Reset timer
        self.round_start_ticks = pygame.time.get_ticks()
        self.time_left = self.round_duration
        self.times_up = False
        self.times_up_timer = 0

        # Reset tile letters for Task 4
        self.tile_letters = list(self.scrambled_word)
        self.selected_tile_idx = None
        self.dragging_tile_idx = None

    def trigger_hint(self):
        if self.times_up:
            return

        if self.revealed_hints < len(self.secret_word):
            self.revealed_hints += 1
            self.score = max(0, self.score - 1)
            self.feedback_msg = f"Hint revealed! (-1 point penalty)"
            self.feedback_color = (255, 200, 80)
        else:
            self.feedback_msg = "All letters already revealed!"
            self.feedback_color = (240, 170, 50)

    def submit_guess(self):
        if self.times_up:
            return

        guess = self.input_box.text.strip().upper()
        if not guess:
            self.feedback_msg = "Type a word before submitting!"
            self.feedback_color = (240, 170, 50)
            return

        # Task 1: Fix guess comparison validation bug
        is_correct = (guess == self.secret_word)

        if is_correct:
            self.score += 1
            self.feedback_msg = f"CORRECT! '{self.secret_word}' is right."
            self.feedback_color = (80, 230, 110)
            self.next_round()
        else:
            self.feedback_msg = "WRONG GUESS! Try again."
            self.feedback_color = (240, 80, 80)
            self.input_box.clear()

    def handle_event(self, event):
        self.input_box.handle_event(event)

        # Keyboard shortcuts
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.submit_guess()

        # Mouse clicks and drag-and-drop for tiles & buttons
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check submit button
            if self.submit_btn.collidepoint(event.pos):
                self.submit_guess()
                return

            # Check hint button (Task 2)
            if self.hint_btn.collidepoint(event.pos):
                self.trigger_hint()
                return

            # Check tile clicks / drag initiation (Task 4)
            if not self.times_up:
                total_tiles = len(self.tile_letters)
                clicked_tile = None
                for i in range(total_tiles):
                    rect = self.get_tile_rect(i, total_tiles)
                    if rect.collidepoint(event.pos):
                        clicked_tile = i
                        break

                if clicked_tile is not None:
                    # If clicking another tile while one is selected -> swap immediately
                    if self.selected_tile_idx is not None and self.selected_tile_idx != clicked_tile:
                        self.tile_letters[self.selected_tile_idx], self.tile_letters[clicked_tile] = (
                            self.tile_letters[clicked_tile],
                            self.tile_letters[self.selected_tile_idx],
                        )
                        self.selected_tile_idx = None
                    else:
                        # Start dragging or toggle selection
                        self.dragging_tile_idx = clicked_tile
                        rect = self.get_tile_rect(clicked_tile, total_tiles)
                        self.drag_mouse_offset = (event.pos[0] - rect.x, event.pos[1] - rect.y)
                        self.drag_current_pos = event.pos
                        self.selected_tile_idx = clicked_tile

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging_tile_idx is not None:
                self.drag_current_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.dragging_tile_idx is not None:
                total_tiles = len(self.tile_letters)
                # Check where it was dropped
                target_idx = None
                for i in range(total_tiles):
                    rect = self.get_tile_rect(i, total_tiles)
                    if rect.collidepoint(event.pos):
                        target_idx = i
                        break

                if target_idx is not None and target_idx != self.dragging_tile_idx:
                    # Move tile to target position
                    moved_letter = self.tile_letters.pop(self.dragging_tile_idx)
                    self.tile_letters.insert(target_idx, moved_letter)
                    self.selected_tile_idx = None
                self.dragging_tile_idx = None

    def update(self):
        # Task 3: Countdown Timer update logic
        if self.times_up:
            # Pause 2 seconds to let the player read the revelation before moving to next round
            if pygame.time.get_ticks() - self.times_up_timer >= 2000:
                self.next_round()
            return

        elapsed = (pygame.time.get_ticks() - self.round_start_ticks) / 1000.0
        self.time_left = max(0.0, self.round_duration - elapsed)

        if self.time_left <= 0:
            self.times_up = True
            self.times_up_timer = pygame.time.get_ticks()
            self.feedback_msg = f"TIME'S UP! The word was '{self.secret_word}'."
            self.feedback_color = (240, 80, 80)

    def render(self, screen):
        screen.fill((26, 30, 38))

        # Title
        title_surf = self.font_title.render("Word Scramble Arena", True, (245, 245, 245))
        screen.blit(title_surf, (self.width // 2 - title_surf.get_width() // 2, 18))

        # Score
        score_surf = self.font_msg.render(f"Score: {self.score}", True, (255, 220, 80))
        screen.blit(score_surf, (self.width // 2 - score_surf.get_width() // 2, 58))

        # Task 3: Countdown Timer Bar
        bar_w, bar_h = 240, 10
        bar_x = self.width // 2 - bar_w // 2
        bar_y = 88
        timer_ratio = self.time_left / self.round_duration
        current_fill_w = int(bar_w * timer_ratio)

        # Bar color changes green -> yellow -> red
        if timer_ratio > 0.5:
            bar_color = (80, 210, 110)
        elif timer_ratio > 0.25:
            bar_color = (240, 180, 50)
        else:
            bar_color = (240, 70, 70)

        pygame.draw.rect(screen, (55, 60, 75), (bar_x, bar_y, bar_w, bar_h), border_radius=5)
        if current_fill_w > 0:
            pygame.draw.rect(screen, bar_color, (bar_x, bar_y, current_fill_w, bar_h), border_radius=5)

        timer_txt = self.font_timer.render(f"{int(self.time_left)}s", True, bar_color)
        screen.blit(timer_txt, (bar_x + bar_w + 10, bar_y - 2))

        # Task 4: Interactive Letter Tiles Rack
        total_tiles = len(self.tile_letters)
        for i, letter in enumerate(self.tile_letters):
            slot_rect = self.get_tile_rect(i, total_tiles)
            # Slot placeholder background
            pygame.draw.rect(screen, (38, 44, 56), slot_rect, border_radius=8)
            pygame.draw.rect(screen, (60, 70, 90), slot_rect, width=1, border_radius=8)

            # Skip drawing normal tile if it's currently being dragged (drawn on top later)
            if self.dragging_tile_idx == i:
                continue

            # Highlight selected tile
            is_selected = (self.selected_tile_idx == i)
            tile_bg = (55, 75, 110) if is_selected else (45, 55, 72)
            tile_border = (100, 200, 255) if is_selected else (110, 130, 160)
            border_w = 3 if is_selected else 2

            pygame.draw.rect(screen, tile_bg, slot_rect, border_radius=8)
            pygame.draw.rect(screen, tile_border, slot_rect, width=border_w, border_radius=8)

            letter_surf = self.font_word.render(letter, True, (240, 245, 255))
            screen.blit(
                letter_surf,
                (slot_rect.centerx - letter_surf.get_width() // 2, slot_rect.centery - letter_surf.get_height() // 2),
            )

        # Draw dragged tile on top
        if self.dragging_tile_idx is not None and self.dragging_tile_idx < len(self.tile_letters):
            drag_x = self.drag_current_pos[0] - self.drag_mouse_offset[0]
            drag_y = self.drag_current_pos[1] - self.drag_mouse_offset[1]
            drag_rect = pygame.Rect(drag_x, drag_y, self.tile_size, self.tile_size)

            # Shadow
            shadow_rect = pygame.Rect(drag_x + 3, drag_y + 4, self.tile_size, self.tile_size)
            pygame.draw.rect(screen, (15, 18, 24), shadow_rect, border_radius=8)

            pygame.draw.rect(screen, (70, 95, 145), drag_rect, border_radius=8)
            pygame.draw.rect(screen, (130, 220, 255), drag_rect, width=3, border_radius=8)

            letter = self.tile_letters[self.dragging_tile_idx]
            letter_surf = self.font_word.render(letter, True, (255, 255, 255))
            screen.blit(
                letter_surf,
                (drag_rect.centerx - letter_surf.get_width() // 2, drag_rect.centery - letter_surf.get_height() // 2),
            )

        # Instruction subtitle
        sub_text = self.font_small.render("Drag or click tiles to rearrange anagram", True, (140, 150, 170))
        screen.blit(sub_text, (self.width // 2 - sub_text.get_width() // 2, 182))

        # Task 2: Hint Revealed Letters Display
        hint_chars = []
        for idx, char in enumerate(self.secret_word):
            if idx < self.revealed_hints:
                hint_chars.append(char)
            else:
                hint_chars.append("_")
        hint_str = "  ".join(hint_chars)
        hint_surf = self.font_hint.render(hint_str, True, (255, 215, 100))
        screen.blit(hint_surf, (self.width // 2 - hint_surf.get_width() // 2, 215))

        # Text input box
        self.input_box.render(screen)

        # Submit Button
        pygame.draw.rect(screen, (40, 145, 75), self.submit_btn, border_radius=6)
        pygame.draw.rect(screen, (180, 230, 195), self.submit_btn, width=2, border_radius=6)
        submit_text = self.font_btn.render("SUBMIT", True, (255, 255, 255))
        screen.blit(
            submit_text,
            (
                self.submit_btn.centerx - submit_text.get_width() // 2,
                self.submit_btn.centery - submit_text.get_height() // 2,
            ),
        )

        # Task 2: Hint Button
        pygame.draw.rect(screen, (185, 125, 25), self.hint_btn, border_radius=6)
        pygame.draw.rect(screen, (245, 210, 140), self.hint_btn, width=2, border_radius=6)
        hint_text = self.font_btn.render("HINT", True, (255, 255, 255))
        screen.blit(
            hint_text,
            (
                self.hint_btn.centerx - hint_text.get_width() // 2,
                self.hint_btn.centery - hint_text.get_height() // 2,
            ),
        )

        # Feedback Message
        feedback_surf = self.font_msg.render(self.feedback_msg, True, self.feedback_color)
        screen.blit(feedback_surf, (self.width // 2 - feedback_surf.get_width() // 2, 335))
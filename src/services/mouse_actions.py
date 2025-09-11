from __future__ import annotations
import math
import random
import time
from typing import Tuple, List
try:
    import pyautogui  # type: ignore
except ImportError:  # pragma: no cover
    pyautogui = None  # type: ignore

class MouseActions:
    def __init__(self):
        if pyautogui:
            pyautogui.FAILSAFE = True
            pyautogui.PAUSE = 0

    def get_mouse_position(self) -> tuple[int, int]:
        if not pyautogui:
            return
        pos = pyautogui.position()
        return pos.x, pos.y

    def move_mouse_human(self, x: int, y: int,
                         duration_range: Tuple[float, float] = (0.7, 1.8),
                         jitter: int = 2,
                         overshoot: bool = True) -> None:
        if not pyautogui:
            return
        start_x, start_y = pyautogui.position()
        distance = math.dist((start_x, start_y), (x, y))
        base_duration = random.uniform(*duration_range)
        duration = base_duration + (distance / 800.0) * random.uniform(0.2, 0.6)
        points = self._generate_curve((start_x, start_y), (x, y), overshoot=overshoot)
        total = len(points)
        last_time = time.perf_counter()
        for i, (px, py) in enumerate(points):
            t = i / total
            if random.random() < 0.015:
                time.sleep(random.uniform(0.015, 0.04))
            target_elapsed = t * duration
            while (time.perf_counter() - last_time) < target_elapsed:
                time.sleep(0.001)
            jx = px + random.randint(-jitter, jitter)
            jy = py + random.randint(-jitter, jitter)
            pyautogui.moveTo(jx, jy, duration=0)
        pyautogui.moveTo(x, y, duration=0)
        if overshoot and random.random() < 0.6:
            ox = x + random.randint(-4, 4)
            oy = y + random.randint(-4, 4)
            time.sleep(random.uniform(0.03, 0.09))
            pyautogui.moveTo(ox, oy, duration=0.06)
            pyautogui.moveTo(x, y, duration=0.04)

    def click(self, x: int, y: int, button: str = 'left', clicks: int = 1) -> None:
        if not pyautogui:
            return
        self.move_mouse_human(x, y)
        time.sleep(random.uniform(0.05, 0.18))
        pyautogui.click(x, y, clicks=clicks, button=button)

    def double_click(self, x: int, y: int) -> None:
        if not pyautogui:
            return
        self.move_mouse_human(x, y)
        time.sleep(random.uniform(0.04, 0.12))
        pyautogui.doubleClick(x, y)

    def right_click(self, x: int, y: int) -> None:
        if not pyautogui:
            return
        self.move_mouse_human(x, y)
        time.sleep(random.uniform(0.04, 0.12))
        pyautogui.click(x, y, button='right')

    def scroll_human(self, clicks: int) -> None:
        if not pyautogui:
            return
        remaining = clicks
        while remaining != 0:
            step = random.randint(1, min(4, abs(remaining))) * (1 if remaining > 0 else -1)
            pyautogui.scroll(step)
            remaining -= step
            time.sleep(random.uniform(0.04, 0.12))

    def move_relative(self, dx: int, dy: int, **kw) -> None:
        if not pyautogui:
            return
        pos = pyautogui.position()
        self.move_mouse_human(pos.x + dx, pos.y + dy, **kw)

    def move_left(self, pixels: int, **kw) -> None:
        self.move_relative(-abs(pixels), 0, **kw)

    def move_right(self, pixels: int, **kw) -> None:
        self.move_relative(abs(pixels), 0, **kw)

    def move_up(self, pixels: int, **kw) -> None:
        self.move_relative(0, -abs(pixels), **kw)

    def move_down(self, pixels: int, **kw) -> None:
        self.move_relative(0, abs(pixels), **kw)

    def _generate_curve(self, start: Tuple[int, int], end: Tuple[int, int], overshoot: bool) -> List[Tuple[int, int]]:
        (x1, y1), (x4, y4) = start, end
        distance = math.dist(start, end)
        spread = max(40, min(300, distance * 0.6))
        angle = math.atan2(y4 - y1, x4 - x1)
        def control_point(base_x, base_y):
            r = spread * random.uniform(0.2, 0.8)
            theta = angle + random.uniform(-1.2, 1.2)
            return (int(base_x + math.cos(theta) * r), int(base_y + math.sin(theta) * r))
        x2, y2 = control_point(x1, y1)
        x3, y3 = control_point(x4, y4)
        if overshoot and distance > 120 and random.random() < 0.7:
            overshoot_dist = min(80, 12 + distance * 0.15)
            ox = int(x4 + math.cos(angle) * random.uniform(5, overshoot_dist))
            oy = int(y4 + math.sin(angle) * random.uniform(5, overshoot_dist))
            x3, y3 = (ox, oy)
        steps = max(25, int(distance / 4))
        pts = []
        for i in range(steps + 1):
            t = i / steps
            t_ease = t * t * (3 - 2 * t)
            xt = self._cubic_bezier(x1, x2, x3, x4, t_ease)
            yt = self._cubic_bezier(y1, y2, y3, y4, t_ease)
            pts.append((int(xt), int(yt)))
        return pts

    @staticmethod
    def _cubic_bezier(p0, p1, p2, p3, t: float) -> float:
        return ((1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3)
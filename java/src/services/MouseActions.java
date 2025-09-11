import java.awt.*;
import java.awt.event.InputEvent;
import java.util.Random;

public class MouseActions {
    private final Random rnd = new Random();

    public Point getMousePosition() {
        return MouseInfo.getPointerInfo().getLocation();
    }

    public void moveMouseHuman(int x, int y) {
        Point start = getMousePosition();
        int steps = Math.max(25, (int)start.distance(x, y) / 8);
        for (int i = 1; i <= steps; i++) {
            double t = i / (double) steps;
            double ease = t * t * (3 - 2 * t);
            int nx = (int)(start.x + (x - start.x) * ease + rnd.nextInt(3) - 1);
            int ny = (int)(start.y + (y - start.y) * ease + rnd.nextInt(3) - 1);
            RobotUtils.robot().mouseMove(nx, ny);
            RobotUtils.sleep(5);
            if (rnd.nextDouble() < 0.015) RobotUtils.sleep(15 + rnd.nextInt(30));
        }
        RobotUtils.robot().mouseMove(x, y);
    }

    public void click(int x, int y) {
        moveMouseHuman(x, y);
        Robot r = RobotUtils.robot();
        RobotUtils.sleep(40 + rnd.nextInt(120));
        r.mousePress(InputEvent.BUTTON1_DOWN_MASK);
        r.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
    }

    public void doubleClick(int x, int y) {
        moveMouseHuman(x, y);
        Robot r = RobotUtils.robot();
        RobotUtils.sleep(40 + rnd.nextInt(120));
        for (int i = 0; i < 2; i++) {
            r.mousePress(InputEvent.BUTTON1_DOWN_MASK);
            r.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
            RobotUtils.sleep(60 + rnd.nextInt(120));
        }
    }

    public void rightClick(int x, int y) {
        moveMouseHuman(x, y);
        Robot r = RobotUtils.robot();
        RobotUtils.sleep(40 + rnd.nextInt(120));
        r.mousePress(InputEvent.BUTTON3_DOWN_MASK);
        r.mouseRelease(InputEvent.BUTTON3_DOWN_MASK);
    }

    public void scrollHuman(int clicks) {
        int remaining = clicks;
        while (remaining != 0) {
            int step = Math.min(4, Math.max(-4, remaining > 0 ? 1 : -1));
            RobotUtils.robot().mouseWheel(step);
            remaining -= step;
            RobotUtils.sleep(40 + rnd.nextInt(80));
        }
    }

    public void moveRelative(int dx, int dy) {
        Point p = getMousePosition();
        moveMouseHuman(p.x + dx, p.y + dy);
    }

    public void moveLeft(int pixels) { moveRelative(-Math.abs(pixels), 0); }
    public void moveRight(int pixels) { moveRelative(Math.abs(pixels), 0); }
    public void moveUp(int pixels) { moveRelative(0, -Math.abs(pixels)); }
    public void moveDown(int pixels) { moveRelative(0, Math.abs(pixels)); }
}

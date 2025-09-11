package utils;

import java.awt.*;
import java.awt.datatransfer.StringSelection;
import java.awt.event.KeyEvent;

public final class RobotUtils {
    private static Robot ROBOT;
    public static final boolean IS_MAC = System.getProperty("os.name").toLowerCase().contains("mac");
    public static final boolean IS_WIN = System.getProperty("os.name").toLowerCase().contains("win");

    private RobotUtils() {}

    public static Robot robot() {
        if (ROBOT == null) {
            try {
                ROBOT = new Robot();
                ROBOT.setAutoDelay(2);
            } catch (AWTException e) {
                throw new RuntimeException(e);
            }
        }
        return ROBOT;
    }

    public static void sleep(long ms) {
        try { Thread.sleep(ms); } catch (InterruptedException ignored) {}
    }

    public static void pressKey(int keyCode) {
        Robot r = robot();
        r.keyPress(keyCode);
        r.keyRelease(keyCode);
    }

    public static void keyCombo(int... keys) {
        Robot r = robot();
        for (int k : keys) r.keyPress(k);
        for (int i = keys.length - 1; i >= 0; i--) r.keyRelease(keys[i]);
    }

    public static void pasteText(String text) {
        Toolkit.getDefaultToolkit().getSystemClipboard().setContents(new StringSelection(text), null);
        if (IS_MAC) keyCombo(KeyEvent.VK_META, KeyEvent.VK_V); else keyCombo(KeyEvent.VK_CONTROL, KeyEvent.VK_V);
    }
}

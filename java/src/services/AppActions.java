import utils.RobotUtils;
import java.awt.event.KeyEvent;

public class AppActions {
    public void openApplication(String nameOrPath) {
        try {
            if (RobotUtils.IS_MAC) {
                if (nameOrPath.endsWith(".app") || nameOrPath.contains("/"))
                    new ProcessBuilder("open", nameOrPath).start();
                else
                    new ProcessBuilder("open", "-a", nameOrPath).start();
            } else if (RobotUtils.IS_WIN) {
                new ProcessBuilder("cmd", "/c", "start", "", nameOrPath).start();
            } else {
                new ProcessBuilder(nameOrPath).start();
            }
        } catch (Exception ignored) {}
    }

    public String defaultTextEditor() {
        if (RobotUtils.IS_MAC) return "TextEdit";
        if (RobotUtils.IS_WIN) return "notepad";
        return "gedit";
    }

    public void openDefaultTextEditor() {
        openApplication(defaultTextEditor());
    }

    public void closeActiveApplication() {
        if (RobotUtils.IS_MAC) RobotUtils.keyCombo(KeyEvent.VK_META, KeyEvent.VK_Q);
        else RobotUtils.keyCombo(KeyEvent.VK_ALT, KeyEvent.VK_F4);
    }

    public void openVSCode() {
        try {
            if (RobotUtils.IS_MAC) new ProcessBuilder("open", "-a", "Visual Studio Code").start();
            else if (RobotUtils.IS_WIN) new ProcessBuilder("cmd", "/c", "start", "", "code").start();
            else new ProcessBuilder("code").start();
        } catch (Exception ignored) {}
    }

    public void openVSCodeNewTab() {
        openVSCode();
        RobotUtils.sleep(3000);
        if (RobotUtils.IS_MAC) RobotUtils.keyCombo(KeyEvent.VK_META, KeyEvent.VK_N);
        else RobotUtils.keyCombo(KeyEvent.VK_CONTROL, KeyEvent.VK_N);
    }

    public void openTeams() {
        if (RobotUtils.IS_MAC) openApplication("Microsoft Teams");
        else if (RobotUtils.IS_WIN) {
            try { new ProcessBuilder("cmd", "/c", "start", "", "msteams:").start(); } catch (Exception ignored) {}
        } else openApplication("teams");
    }

    public void openOneNote() {
        if (RobotUtils.IS_MAC) openApplication("Microsoft OneNote");
        else if (RobotUtils.IS_WIN) {
            try { new ProcessBuilder("cmd", "/c", "start", "", "onenote:").start(); } catch (Exception ignored) {}
        } else openApplication("onenote");
    }

    public void openInsomnia() {
        try {
            if (RobotUtils.IS_MAC) openApplication("Insomnia");
            else if (RobotUtils.IS_WIN) new ProcessBuilder("cmd", "/c", "start", "", "insomnia").start();
            else new ProcessBuilder("insomnia").start();
        } catch (Exception ignored) {}
    }

    public void pressEnter() { RobotUtils.pressKey(KeyEvent.VK_ENTER); }
    public void pressLeft() { RobotUtils.pressKey(KeyEvent.VK_LEFT); }
    public void pressRight() { RobotUtils.pressKey(KeyEvent.VK_RIGHT); }
    public void pressUp() { RobotUtils.pressKey(KeyEvent.VK_UP); }
    public void pressDown() { RobotUtils.pressKey(KeyEvent.VK_DOWN); }
    public void pressPageDown(int times) { for (int i = 0; i < Math.max(1, times); i++) RobotUtils.pressKey(KeyEvent.VK_PAGE_DOWN); }
    public void pressPageUp(int times) { for (int i = 0; i < Math.max(1, times); i++) RobotUtils.pressKey(KeyEvent.VK_PAGE_UP); }
    public void goToEndOfFile() {
        if (RobotUtils.IS_MAC) RobotUtils.keyCombo(KeyEvent.VK_META, KeyEvent.VK_DOWN);
        else RobotUtils.keyCombo(KeyEvent.VK_CONTROL, KeyEvent.VK_END);
    }

    public void saveActiveFile() {
        if (RobotUtils.IS_MAC) RobotUtils.keyCombo(KeyEvent.VK_META, KeyEvent.VK_S);
        else RobotUtils.keyCombo(KeyEvent.VK_CONTROL, KeyEvent.VK_S);
        RobotUtils.sleep(200);
    }

    public void saveActiveFileAs(String path) {
        if (RobotUtils.IS_MAC) RobotUtils.keyCombo(KeyEvent.VK_META, KeyEvent.VK_SHIFT, KeyEvent.VK_S);
        else RobotUtils.keyCombo(KeyEvent.VK_CONTROL, KeyEvent.VK_SHIFT, KeyEvent.VK_S);
        RobotUtils.sleep(600);
        RobotUtils.pasteText(path);
        RobotUtils.sleep(200);
        RobotUtils.pressKey(KeyEvent.VK_ENTER);
        RobotUtils.sleep(400);
        RobotUtils.pressKey(KeyEvent.VK_ENTER);
    }
}

import java.awt.event.KeyEvent;
import java.util.Random;

public class TypingActions {
    private final double minDelay;
    private final double maxDelay;
    private final double errorRate;
    private final Random rnd = new Random();

    public TypingActions(double minCharDelay, double maxCharDelay, double errorRate) {
        this.minDelay = minCharDelay;
        this.maxDelay = maxCharDelay;
        this.errorRate = errorRate;
    }

    private void sleepRandom() {
        long ms = (long)(1000 * (minDelay + rnd.nextDouble() * (maxDelay - minDelay)));
        RobotUtils.sleep(Math.max(1, ms));
    }

    public void typeHuman(String text, boolean allowErrors, double longPauseChance, double longPauseMin, double longPauseMax) {
        for (char ch : text.toCharArray()) {
            if ((ch == ' ' || ch == '\n' || ch == '.' || ch == '!' || ch == '?') && rnd.nextDouble() < longPauseChance) {
                long pause = (long)(1000 * (longPauseMin + rnd.nextDouble() * (longPauseMax - longPauseMin)));
                System.out.printf("Pausa humana longa (~%.1fs)...%n", pause / 1000.0);
                RobotUtils.sleep(pause);
            }
            sleepRandom();
            if (ch == '\n') { RobotUtils.pressKey(KeyEvent.VK_ENTER); continue; }
            if (allowErrors && Character.isLetter(ch) && rnd.nextDouble() < errorRate) {
                // erro: digita letra aleatória e corrige
                char wrong = (char)('a' + rnd.nextInt(26));
                typeChar(wrong);
                RobotUtils.sleep(50 + rnd.nextInt(150));
                RobotUtils.pressKey(KeyEvent.VK_BACK_SPACE);
                RobotUtils.sleep(30 + rnd.nextInt(90));
            }
            typeChar(ch);
            if (ch == '.' || ch == '!' || ch == '?') RobotUtils.sleep(250 + rnd.nextInt(300));
            else if (ch == ' ' && rnd.nextDouble() < 0.3) RobotUtils.sleep(80 + rnd.nextInt(120));
        }
    }

    private void typeChar(char ch) {
        // Alfabeto e dígitos básicos
        if (Character.isLetterOrDigit(ch)) {
            boolean upper = Character.isUpperCase(ch);
            int code = Character.isDigit(ch) ? (KeyEvent.VK_0 + (ch - '0')) : (KeyEvent.VK_A + (Character.toUpperCase(ch) - 'A'));
            if (upper) RobotUtils.keyCombo(KeyEvent.VK_SHIFT, code); else RobotUtils.pressKey(code);
            return;
        }
        switch (ch) {
            case ' ': RobotUtils.pressKey(KeyEvent.VK_SPACE); return;
            case '.': RobotUtils.pressKey(KeyEvent.VK_PERIOD); return;
            case ',': RobotUtils.pressKey(KeyEvent.VK_COMMA); return;
            case '-': RobotUtils.pressKey(KeyEvent.VK_MINUS); return;
            case '_': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_MINUS); return;
            case '=': RobotUtils.pressKey(KeyEvent.VK_EQUALS); return;
            case '+': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_EQUALS); return;
            case ';': RobotUtils.pressKey(KeyEvent.VK_SEMICOLON); return;
            case ':': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_SEMICOLON); return;
            case '/': RobotUtils.pressKey(KeyEvent.VK_SLASH); return;
            case '?': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_SLASH); return;
            case '\\': RobotUtils.pressKey(KeyEvent.VK_BACK_SLASH); return;
            case '\'': RobotUtils.pressKey(KeyEvent.VK_QUOTE); return;
            case '"': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_QUOTE); return;
            case '[': RobotUtils.pressKey(KeyEvent.VK_OPEN_BRACKET); return;
            case ']': RobotUtils.pressKey(KeyEvent.VK_CLOSE_BRACKET); return;
            case '{': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_OPEN_BRACKET); return;
            case '}': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_CLOSE_BRACKET); return;
            case '(': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_9); return;
            case ')': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_0); return;
            case '!': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_1); return;
            case '@': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_2); return;
            case '#': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_3); return;
            case '$': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_4); return;
            case '%': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_5); return;
            case '^': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_6); return;
            case '&': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_7); return;
            case '*': RobotUtils.keyCombo(KeyEvent.VK_SHIFT, KeyEvent.VK_8); return;
            default:
                // fallback: usa clipboard e cola
                RobotUtils.pasteText(String.valueOf(ch));
        }
    }
}

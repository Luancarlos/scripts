import services.AppActions;
import services.MouseActions;
import services.TypingActions;
import utils.RobotUtils;
import java.util.Random;

public class ProductW {
    private final AppActions apps = new AppActions();
    private final MouseActions mouse = new MouseActions();
    private final TypingActions typing = new TypingActions(0.035, 0.18, 0.07);
    private final Random rnd = new Random();

    public void execute(String text) {
        typing.typeHuman(text, false, 0.02, 1.0, 5.0);
        apps.saveActiveFile();
        RobotUtils.sleep(500);
        String[] actions = {"MOVER","CLICK","DOUBLE","RIGHT","ESPERA","TECLADO"};
        for (int i=0; i<10; i++) {
            String a = actions[rnd.nextInt(actions.length)];
            switch (a) {
                case "MOVER": mouse.moveRelative(rnd.nextInt(201)-100, rnd.nextInt(201)-100); break;
                case "CLICK": mouse.click(500, 450 + rnd.nextInt(200)); break;
                case "DOUBLE": mouse.doubleClick(500, 450 + rnd.nextInt(200)); break;
                case "RIGHT": mouse.rightClick(500, 450 + rnd.nextInt(200)); break;
                case "ESPERA": RobotUtils.sleep(500 + rnd.nextInt(2000)); break;
                case "TECLADO": apps.pressLeft(); apps.pressRight(); apps.pressUp(); apps.pressDown(); break;
            }
        }
        apps.pressPageDown(3);
        RobotUtils.sleep(300);
        mouse.click(500, 450 + rnd.nextInt(200));
        mouse.scrollHuman(10);
        mouse.scrollHuman(10);
    }

    public static void main(String[] args) {
        ProductW agent = new ProductW();
        RobotUtils.sleep(2000);
        agent.apps.openDefaultTextEditor();
        RobotUtils.sleep(3000);
        for (String block : data.TextBlocks.JS_GARANTIA_BLOCKS) {
            agent.execute(block);
        }
    }
}

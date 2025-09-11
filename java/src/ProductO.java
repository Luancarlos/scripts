import services.AppActions;
import services.MouseActions;
import services.TypingActions;
import utils.RobotUtils;
import java.util.Random;

public class ProductO {
    private final AppActions apps = new AppActions();
    private final MouseActions mouse = new MouseActions();
    private final TypingActions typing = new TypingActions(0.035, 0.18, 0.07);
    private final Random rnd = new Random();

    public void moveMouse() {
        mouse.moveRelative(rnd.nextInt(1001)-500, rnd.nextInt(1001)-500);
    }

    public static void main(String[] args) {
        ProductO agent = new ProductO();
        RobotUtils.sleep(2000);
        agent.apps.openDefaultTextEditor();
        RobotUtils.sleep(3000);
        while (true) {
            agent.moveMouse();
            RobotUtils.sleep(3000);
            agent.typing.typeHuman("Veículos, máquinas e equipamentos...\n", false, 0.01, 1.0, 3.0);
            agent.apps.saveActiveFile();
            agent.apps.pressEnter();
            RobotUtils.sleep(3000);
            agent.apps.closeActiveApplication();
        }
    }
}

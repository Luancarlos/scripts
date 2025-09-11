import services.AppActions;
import services.MouseActions;
import services.TypingActions;
import utils.RobotUtils;
import java.util.Random;

public class ProductM {
    private final AppActions apps = new AppActions();
    private final MouseActions mouse = new MouseActions();
    private final TypingActions typing = new TypingActions(0.035, 0.18, 0.07);
    private final Random rnd = new Random();

    public static void main(String[] args) {
        ProductM agent = new ProductM();
        String[] actions = {"MOVER","CLICK","DOUBLE","RIGHT","ESPERA","TECLADO"};
        while (true) {
            String a = actions[agent.rnd.nextInt(actions.length)];
            switch (a) {
                case "MOVER": agent.mouse.moveRelative(agent.rnd.nextInt(201)-100, agent.rnd.nextInt(201)-100); break;
                case "CLICK": agent.mouse.click(500, 500); break;
                case "DOUBLE": agent.mouse.doubleClick(500, 500); break;
                case "RIGHT": agent.mouse.rightClick(500, 500); break;
                case "ESPERA": RobotUtils.sleep(1000 + agent.rnd.nextInt(4000)); break;
                case "TECLADO": agent.apps.pressEnter(); break;
            }
            RobotUtils.sleep(1000);
        }
    }
}

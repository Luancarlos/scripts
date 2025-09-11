import services.AppActions;
import services.MouseActions;
import services.TypingActions;
import utils.RobotUtils;

public class ProductJ {
    private final AppActions apps = new AppActions();
    private final MouseActions mouse = new MouseActions();
    private final TypingActions typing = new TypingActions(0.035, 0.18, 0.07);

    public void execute(String text) {
        typing.typeHuman(text, false, 0.02, 1.0, 5.0);
        apps.saveActiveFile();
        RobotUtils.sleep(500);
        apps.pressPageDown(2);
        mouse.scrollHuman(8);
    }

    public static void main(String[] args) {
        ProductJ agent = new ProductJ();
        RobotUtils.sleep(2000);
        agent.apps.openDefaultTextEditor();
        RobotUtils.sleep(3000);
        for (String block : data.TextBlocks.JAVA_GARANTIA_BLOCKS) {
            agent.execute(block);
        }
    }
}

# Java port of the human_agent project

Build (Java 11+):
- Compile: javac -d out $(find java -name "*.java")
- Run ProductW: java -cp out ProductW
- Run ProductJ: java -cp out ProductJ

Notes:
- Requires a desktop session (uses java.awt.Robot for keyboard/mouse).
- On macOS, Accessibility permissions are needed for the terminal/IDE.
- App launching relies on OS commands (open/code/cmd start). Adjust paths if needed.

# Renders docs/demo.gif with charmbracelet/vhs (needs vhs, ttyd and ffmpeg on PATH).
# Run from the repo root, with the deps installed in .venv:  vhs docs/demo.tape
# Follows DEMO.md offline path: profile -> policy list -> make run-offline -> a generated draft (Markdown stands in for the .docx) -> tests.
Output docs/demo.gif

Set Shell "bash"
Set FontSize 18
Set Width 1200
Set Height 700
Set Padding 24
Set Theme "Catppuccin Mocha"
Set WindowBar Colorful
Set TypingSpeed 40ms

Hide
Type "VIRTUAL_ENV_DISABLE_PROMPT=1 source .venv/bin/activate"
Enter
Wait@120s
Type "make clean >/dev/null"
Enter
Wait@120s
Type "clear"
Enter
Wait@120s
Show
Sleep 500ms

Type "sed -n '3,16p' profile.example.yaml"
Sleep 400ms
Enter
Wait@120s
Sleep 2.5s

Type "python generate.py --list"
Sleep 400ms
Enter
Wait@120s
Sleep 2.5s

Hide
Type "clear"
Enter
Sleep 200ms
Show
Type "make run-offline"
Sleep 400ms
Enter
Wait@120s
Sleep 3.5s

Hide
Type "clear"
Enter
Sleep 200ms
Show
Type "sed -n '1,16p' output/access-control.md"
Sleep 400ms
Enter
Wait@120s
Sleep 4s

Type "make test"
Sleep 400ms
Enter
Wait@120s
Sleep 2s

Sleep 1s

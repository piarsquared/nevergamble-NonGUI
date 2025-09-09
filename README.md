# Never Gamble (Terminal Edition)

**Never Gamble** is a minimalist stock simulation game that runs entirely in your terminal.  
No GUI. No distractions. Just raw Python logic and dangerously poor financial decisions.

This version is a text-based prototype inspired by 2003devin's Geometry Dash level _"Never Gamble"_  
(he makes some weird stuff, by the way, so just... be careful looking that up).

---

## Features (Current Version)

- Terminal UI with a basic page management system
- Command system (`help`, `clear`, `save`, `quit`, etc.) — basic but solid
- Save file support! So you can continue your gambling addiction later.
- Built to expand into full stock logic and ASCII graphs (eventually)
- In the future, I do intend to make a GUI version of this if you REALLY hate using the terminal.

> [!TIP]
> This is a **work in progress**. Expect some spaghetti code and placeholder features for now.

---

## 🛠 Commands

| Command | Description |
|---------|-------------|
| `help`  | Shows basic instructions |
| `clear` | Clears the terminal |
| `save`  | (Placeholder for now) Saves your progress |
| `quit`  | Quits the game (with confirmation) |

More commands (like `balance`, `gamble`, `invest`, and `graph`) coming soon.

---

## Planned Features (TBD)

- [ ] Real stock simulation logic
- [ ] ASCII graphs for fake stock trends
- [ ] Better save/load system
- [ ] Event system (crashes, booms, scams)
- [ ] Cross-platform support (Linux/Mac)

---

## Credits

Made solo by piarsquared (piar)
Special thanks to 2003devin for the original, um, inspiration?

---

## 🧃 License

MIT. Do whatever you want with this. Just, please don't implement real money. Please.

---

## Download

Option 1. 

- Grab the Python file from the [Releases](https://github.com/piarsquared/nevergamble/releases) tab
- Run it with:

  ```bash
    python nevergamble.py

> Requires Python 3.x — and currently Windows-only due to msvcrt.

Option 2. Or clone the repo:

  ```bash
  git clone https://github.com/piarsquared/nevergamble.git
  cd nevergamble

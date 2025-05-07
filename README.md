# 🎮 Tic-Tac-Toe 4×4 AI

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![pygame Version](https://img.shields.io/badge/pygame-2.0%2B-green.svg)

> **A fun and strategic 4×4 Tic-Tac-Toe game powered by AI!** Compete against the computer using the Minimax algorithm with optional Alpha-Beta pruning, all visualized in stunning real time via Pygame.

---

## 🚀 Features & Highlights

* ⚔️ **Human vs. AI** or **AI vs. Human** modes
* 🤖 **Minimax Algorithm** for unbeatable AI decisions
* ✂️ **Alpha-Beta Pruning** (optional) to speed up search
* ⏱️ **Performance Metrics**: Nodes expanded, time per move
* 🎨 **Graphical Interface**: Smooth board drawing, animated moves
* ⚙️ **Customizable**: Adjust search depth, board size, colors

---

## 🛠️ Tech Stack & Languages

* **🖥️ Language:** Python 3.7+
* **🎮 Rendering:** Pygame
* **🔢 Math & Data:** NumPy
* **📋 Scripting:** Shell (for setup)

---

## 📥 Installation & Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/<YOUR_USERNAME>/tic-tac-toe-4x4-ai.git
   cd tic-tac-toe-4x4-ai
   ```

2. **Create & activate virtual environment** (recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\\Scripts\\activate  # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 Running the Game

```bash
python tic_tac_toe_ai.py
```

1. **Alpha-Beta Pruning?** (y/n): Enable or disable pruning.
2. **AI goes first?** (y/n): Choose order of play.
3. Click on a cell to place ❌; the AI will automatically place ⭕.

---

## ⚙️ Configuration & Customization

* **DEPTH\_LIMIT**: Control AI lookahead (higher = stronger, slower)
* **BOARD\_ROWS / BOARD\_COLS**: Change to experiment with different grid sizes (requires minor code edit)
* **LINE\_WIDTH**, **COLORS**: Tweak visual style in constants.

---

## 📸 Screenshots & GIFs

![Game Screenshot](assets/Game.png)

*More visuals coming soon!* Feel free to add in animated GIFs or highlight key moves.

---

## 🗂️ Project Structure

```text
tic-tac-toe-4x4-ai/
├── README.md                 # This documentation
├── tic_tac_toe_ai.py         # Main game logic + AI
├── requirements.txt          # pygame, numpy
├── .gitignore                # Ignore cache & env
└── assets/
    ├── screenshot.png        # Example game image
    └── icon.png              # (Optional) window icon
```

---

## 🤝 Contributing

1. ⭐ **Star** the project
2. 🍴 **Fork** it
3. 📥 **Clone** your fork
4. 💡 **Create** a new branch for your feature
5. 🚀 **Commit** your improvements
6. 🔃 **Push** and open a **Pull Request**

Please follow existing code style and add tests where possible.

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more info.

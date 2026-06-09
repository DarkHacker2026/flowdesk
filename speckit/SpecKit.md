# SpecKit — FlowDesk: AI Project Management Suite
Hackathon: Swecha Hackathon 2 | June 9, 2026
Team: Arihant Bansal (Solo)
Repo: https://code.swecha.org/ArihantBansal/hackathon2

## 1. Problem
Solo developers lack a lightweight, intelligent task manager without
Jira's overhead or the cost of AI tools. Priority is always guessed.

## 2. Solution
FlowDesk is a browser-based Kanban board with embedded Llama 3.1 AI
(via Groq's free tier) that scores task urgency, prioritizes your backlog,
and recommends daily focus — at zero cost.

## 3. Features
| Feature | Description |
|---------|-------------|
| Kanban Board | Drag-and-drop across Todo / In Progress / Done |
| AI Priority Scoring | Llama 3.1 scores each task 0-100 with reasoning |
| AI Daily Focus | One-click: what should I work on today? |
| Task Tags | Custom categorization |
| Stats Bar | Live: total, in-progress, done, avg AI score |
| Persistent Storage | localStorage — survives refreshes |
| Zero-cost AI | Groq free tier, no credit card |

## 4. Tech Stack
- Frontend: Vanilla HTML5 + JavaScript (ES6+)
- Styling: Tailwind CSS (CDN)
- AI: Groq API — llama-3.1-8b-instant (free tier)
- Storage: localStorage
- Hosting: GitLab Pages
- Dependencies: Zero npm packages, zero build step

## 5. Architecture
Browser
  index.html
    TaskManager (localStorage CRUD)
    renderBoard() (DOM rendering)
    scoreWithAI() → Groq API → Llama 3.1 8B
    focusSuggestions() → Groq API → Llama 3.1 8B
  GitLab Pages (static hosting via CI/CD)

## 6. AI Integration
Provider: Groq (free tier — console.groq.com)
Model: llama-3.1-8b-instant
Use 1: Task scoring — returns {priority, score, reason}
Use 2: Daily focus — returns 3 actionable bullet points
Key storage: User pastes their own free key into Settings modal;
             stored in localStorage, never in repo.

## 7. Demo Script (2 min)
1. Show 3 pre-loaded sample tasks on the board
2. Add a new task → click Score with AI → see priority + score fill in
3. Drag task to In Progress
4. Click Ask AI → show 3 focus recommendations
5. Move a task to Done → stats bar updates live

## 8. Why Free AI?
Groq offers free access to Llama 3.1 with no credit card.
Same code works with Google Gemini free tier or Ollama (local).

## 9. Future Scope
- Team boards (shared via URL)
- Sprint planning AI
- GitHub/GitLab issue sync
- Deadline-aware urgency escalation

## 10. Files
hackathon2/
├── index.html       ← complete app
├── .gitlab-ci.yml
├── README.md
└── speckit/SpecKit.md

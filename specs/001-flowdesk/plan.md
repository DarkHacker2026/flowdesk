# FlowDesk Technical Plan

## Tech Stack
- Frontend: Vanilla HTML5 + JavaScript (ES6+)
- Styling: Tailwind CSS (CDN)
- AI: Groq API — llama-3.1-8b-instant (free tier)
- Storage: localStorage
- Hosting: GitLab Pages
- Dependencies: Zero npm packages, zero build step

## Architecture
- Browser
  - index.html
    - TaskManager (localStorage CRUD)
    - renderBoard() (DOM rendering)
    - scoreWithAI() → Groq API → Llama 3.1 8B
    - focusSuggestions() → Groq API → Llama 3.1 8B
- GitLab Pages (static hosting via CI/CD)

## Repo Structure
```text
hackathon2/
├── README.md
├── .gitlab-ci.yml
├── index.html          ← entire app lives here
└── speckit/
    ├── spec.md
    ├── plan.md
    ├── tasks.md
    ├── data-model.md
    └── research.md
```

## AI Integration Strategy
Provider: Groq (free tier — console.groq.com)
Model: llama-3.1-8b-instant
Use 1: Task scoring — returns {priority, score, reason}
Use 2: Daily focus — returns 3 actionable bullet points
Key storage: User pastes their own free key into Settings modal; stored in localStorage, never in repo.

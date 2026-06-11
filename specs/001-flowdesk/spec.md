# FlowDesk Requirements Specification

## Problem
Solo developers lack a lightweight, intelligent task manager without Jira's overhead or the cost of AI tools. Priority is always guessed.

## Solution
FlowDesk is a browser-based Kanban board with embedded Llama 3.1 AI that scores task urgency, prioritizes your backlog, and recommends daily focus — at zero cost.

## Features
- Kanban Board: Drag-and-drop across Todo / In Progress / Done
- AI Priority Scoring: Llama 3.1 scores each task 0-100 with reasoning
- AI Daily Focus: One-click: what should I work on today?
- Task Tags: Custom categorization
- Stats Bar: Live: total, in-progress, done, avg AI score
- Persistent Storage: localStorage — survives refreshes
- Zero-cost AI: Groq free tier, no credit card

## Demo Script (2 min)
1. Show 3 pre-loaded sample tasks on the board
2. Add a new task → click Score with AI → see priority + score fill in
3. Drag task to In Progress
4. Click Ask AI → show 3 focus recommendations
5. Move a task to Done → stats bar updates live

## Future Scope
- Team boards (shared via URL)
- Sprint planning AI
- GitHub/GitLab issue sync
- Deadline-aware urgency escalation

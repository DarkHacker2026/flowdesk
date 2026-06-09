# Data Model

The application uses a single `TaskManager` object that stores data in the browser's `localStorage` under the key `flowdesk_tasks`.

## Task Entity Shape
```javascript
{
  id: string,                 // Unique timestamp-based ID
  title: string,              // Task title
  description: string,        // Optional task description
  status: string,             // 'todo' | 'in-progress' | 'done'
  priority: string,           // 'low' | 'medium' | 'high' | 'critical'
  aiScore: number,            // 0-100 priority score assigned by AI
  tags: string[],             // Array of categorization tags
  createdAt: number           // Timestamp
}
```

## Storage Methods
- `getAll()`: Retrieves and parses tasks from localStorage.
- `add(task)`: Generates an ID, appends the task, and saves to localStorage.
- `update(id, changes)`: Finds task by ID, applies changes, and saves.
- `delete(id)`: Removes task by ID and saves.
- `move(id, newStatus)`: Helper to update a task's status.

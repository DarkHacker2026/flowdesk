# Research & AI Options

## Why Free AI?
Groq offers free access to Llama 3.1 with no credit card. This allows building powerful AI features without operational costs.

## FREE AI FALLBACK TABLE

| Provider | URL | Free? | Drop-in swap |
|----------|-----|-------|--------------|
| Groq | console.groq.com | Yes, no card | (primary) |
| Google Gemini | aistudio.google.com/apikey | Yes, Google login | Change endpoint + model |
| OpenRouter | openrouter.ai | Free models | Change endpoint + add model header |
| Ollama (local) | ollama.com | 100% free | localhost:11434/v1 |

## Performance Considerations
Groq inference (llama-3.1-8b-instant) is extremely fast (~500 tokens/sec), making it ideal for synchronous UI actions like the "Score with AI" button.

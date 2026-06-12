import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS
css_pattern = r'<style>.*?</style>'
new_css = """<style>
        /* Base Canvas */
        body { 
            background-color: #000; 
            color: #94a3b8;
            font-family: 'Outfit', sans-serif; 
            overflow-x: hidden;
            margin: 0; padding: 0;
        }

        /* Ambient Orbs */
        .orb {
            position: fixed;
            border-radius: 50%;
            filter: blur(100px);
            pointer-events: none;
            z-index: -2;
            animation: float 18s ease-in-out infinite;
            opacity: 0.45;
        }
        .orb-1 { width: 45vw; height: 45vw; background: #5b21b6; top: -15%; left: -10%; }
        .orb-2 { width: 50vw; height: 50vw; background: #4f46e5; bottom: -20%; right: -10%; animation-delay: -3s; }
        .orb-3 { width: 35vw; height: 35vw; background: #1d4ed8; top: 40%; left: 30%; animation-delay: -7s; opacity: 0.35; }
        .orb-4 { width: 40vw; height: 40vw; background: #9333ea; top: 10%; right: 15%; animation-delay: -11s; }
        .orb-5 { width: 35vw; height: 35vw; background: #0ea5e9; bottom: 20%; left: 10%; animation-delay: -15s; opacity: 0.4; }

        @keyframes float {
            0%, 100% { transform: translate(0, 0) scale(1); }
            25% { transform: translate(3vw, -4vh) scale(1.05); }
            50% { transform: translate(-2vw, 3vh) scale(0.95); }
            75% { transform: translate(-4vw, -2vh) scale(1.02); }
        }

        /* Noise & Grid */
        .noise {
            position: fixed; inset: 0; z-index: -1; pointer-events: none;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
            opacity: 0.04; mix-blend-mode: overlay;
        }
        .grid-bg {
            position: fixed; inset: 0; z-index: -1; pointer-events: none;
            background-size: 32px 32px;
            background-image: linear-gradient(to right, rgba(255,255,255,0.04) 1px, transparent 1px), linear-gradient(to bottom, rgba(255,255,255,0.04) 1px, transparent 1px);
        }

        /* Glassmorphism Panels */
        .glass-panel {
            background: rgba(255, 255, 255, 0.04);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.09);
            box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.1); 
            transition: border-color 0.3s ease;
        }
        .glass-panel:hover {
            border-color: rgba(255, 255, 255, 0.18);
        }
        .card-bg { @apply glass-panel; }
        
        .task-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.06);
            box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.08);
            animation: fadeIn 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .task-card:hover {
            transform: translateY(-4px) scale(1.02);
            border-color: rgba(255, 255, 255, 0.18);
            box-shadow: inset 0 0 20px rgba(124, 58, 237, 0.15), inset 0 1px 0 0 rgba(255, 255, 255, 0.2), 0 10px 30px -10px rgba(0,0,0,0.5);
        }

        /* Typography */
        .text-iridescent {
            background: linear-gradient(135deg, #e2e8f0, #a78bfa, #60a5fa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            color: transparent;
        }
        h2 { color: #f1f5f9; }
        .section-label {
            font-family: monospace;
            text-transform: uppercase;
            font-size: 10px;
            letter-spacing: 0.12em;
            color: #6b7280;
        }

        /* UI Overrides */
        .focus-ring { outline: none; border-color: #a78bfa; box-shadow: 0 0 0 2px rgba(167, 139, 250, 0.3); }
        .tag-pill { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); color: #cbd5e1; }
        .hover-btn { transition: transform 0.15s ease, background 0.2s ease, border-color 0.2s ease; cursor: pointer; }
        .hover-btn:active { transform: scale(0.95); }
        .modal-overlay { background: rgba(0, 0, 0, 0.8); backdrop-filter: blur(12px); }
        .slide-panel { transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1); transform: translateX(100%); }
        .slide-panel.open { transform: translateX(0); }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(12px); }
            to { opacity: 1; transform: none; }
        }

        @keyframes pulseEmpty {
            0%, 100% { transform: scale(1); box-shadow: inset 0 1px 0 0 rgba(255,255,255,0.1); }
            50% { transform: scale(1.05); box-shadow: inset 0 1px 0 0 rgba(255,255,255,0.1), 0 0 20px rgba(167, 139, 250, 0.4); }
        }
        .pulse-add { animation: pulseEmpty 2.5s infinite cubic-bezier(0.4, 0, 0.2, 1); }
        
        .col-dropzone.drag-over {
            border: 1px solid rgba(167, 139, 250, 0.5);
            background: rgba(167, 139, 250, 0.05);
            box-shadow: inset 0 0 20px rgba(167, 139, 250, 0.1);
        }

        /* Flow Path SVG */
        #flow-path-container {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: -1;
        }

        /* Marquee */
        .marquee-wrapper {
            width: 100%; overflow: hidden; position: relative; padding: 4rem 0 8rem;
            mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
            -webkit-mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
        }
        .marquee {
            display: flex; gap: 1.5rem; width: max-content; padding-bottom: 1.5rem;
        }
        .marquee:hover { animation-play-state: paused; }
        
        @keyframes scrollLeft { from { transform: translateX(0); } to { transform: translateX(-50%); } }
        @keyframes scrollRight { from { transform: translateX(-50%); } to { transform: translateX(0); } }

        .marquee.left { animation: scrollLeft 22s linear infinite; }
        .marquee.right { animation: scrollRight 28s linear infinite reverse; }

        .review-card {
            min-width: 260px; max-width: 300px;
            background: rgba(255, 255, 255, 0.04); backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.09);
            border-left: 2px solid;
            box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
            padding: 1.25rem; border-radius: 0.75rem;
            transition: all 0.3s ease;
        }
        .review-card:hover { 
            background: rgba(255, 255, 255, 0.08); 
            border-color: rgba(255, 255, 255, 0.18);
        }
        .stars svg { width: 14px; height: 14px; fill: #fbbf24; display: inline-block; }
</style>"""
content = re.sub(css_pattern, new_css, content, flags=re.DOTALL)

# Replace Body & Navbar & Stats Bar with new layout
body_pattern = r'<body class=".*?">(.*?)<!-- Board -->'
new_body = """<body class="min-h-screen flex flex-col text-[#94a3b8]">

    <!-- Ambience -->
    <div class="noise"></div>
    <div class="grid-bg"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
    <div class="orb orb-4"></div>
    <div class="orb orb-5"></div>

    <!-- Flow Path Background -->
    <div id="flow-path-container">
        <svg width="100%" height="100%" viewBox="0 0 100 100" preserveAspectRatio="none">
            <defs>
                <linearGradient id="glow-gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stop-color="#a78bfa" stop-opacity="0" />
                    <stop offset="20%" stop-color="#a78bfa" stop-opacity="0.8" />
                    <stop offset="50%" stop-color="#ec4899" stop-opacity="0.8" />
                    <stop offset="80%" stop-color="#8b5cf6" stop-opacity="0.8" />
                    <stop offset="100%" stop-color="#8b5cf6" stop-opacity="0" />
                </linearGradient>
                <filter id="blur-glow" x="-20%" y="-20%" width="140%" height="140%">
                    <feGaussianBlur stdDeviation="2" result="blur" />
                    <feMerge>
                        <feMergeNode in="blur" />
                        <feMergeNode in="SourceGraphic" />
                    </feMerge>
                </filter>
            </defs>
            <path id="flow-path" d="M 50 0 C 80 30, 20 70, 50 100" fill="none" stroke="url(#glow-gradient)" stroke-width="0.3" filter="url(#blur-glow)" stroke-linecap="round" style="transition: stroke-dashoffset 0.3s ease-out;" />
        </svg>
    </div>

    <!-- Navbar -->
    <nav class="glass-panel border-b-0 flex items-center justify-between px-6 py-4 z-10 sticky top-0">
        <div class="text-2xl font-bold tracking-tight text-iridescent">FlowDesk</div>
        <div class="flex items-center gap-4">
            <select id="lang-switcher" onchange="setLanguage(this.value)" class="glass-panel text-white text-sm rounded p-1 outline-none">
                <option value="en" class="bg-[#000]">English</option>
                <option value="hi" class="bg-[#000]">हिंदी</option>
                <option value="te" class="bg-[#000]">తెలుగు</option>
            </select>
            <button id="ask-ai-btn" class="hover-btn glass-panel text-white px-4 py-2 rounded-md font-medium text-sm flex items-center gap-2 shadow-lg shadow-violet-500/10">
                <span data-i18n="ask-ai">Ask AI ✨</span>
            </button>
            <button id="settings-btn" class="hover-btn text-gray-400 hover:text-white p-2 glass-panel rounded-full">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
            </button>
        </div>
    </nav>

    <!-- Hero -->
    <header class="py-24 px-6 text-center z-10 flex flex-col items-center">
        <div class="section-label mb-4 text-violet-400">Project Intelligence</div>
        <h1 class="text-5xl md:text-7xl font-bold mb-6 text-iridescent tracking-tight max-w-4xl mx-auto leading-tight">Prioritize at the speed of thought.</h1>
        <p class="text-lg md:text-xl text-[#94a3b8] max-w-2xl mx-auto mb-10">FlowDesk uses local AI to intelligently score and organize your tasks, so you can stop planning and start shipping.</p>
        
        <div class="glass-panel inline-flex gap-4 text-sm flex-wrap justify-center p-2 rounded-2xl shadow-2xl">
            <div class="px-4 py-1.5 rounded-full"><span data-i18n="total-tasks" class="text-muted">Total:</span> <span id="stat-total" class="font-bold text-white">0</span></div>
            <div class="px-4 py-1.5 rounded-full"><span data-i18n="in-progress-label" class="text-amber-400/80">In Progress:</span> <span id="stat-in-progress" class="font-bold text-amber-100">0</span></div>
            <div class="px-4 py-1.5 rounded-full"><span data-i18n="done-label" class="text-emerald-400/80">Done:</span> <span id="stat-done" class="font-bold text-emerald-100">0</span></div>
            <div class="px-4 py-1.5 rounded-full"><span data-i18n="avg-ai" class="text-violet-400/80">Avg AI Score:</span> <span id="stat-ai" class="font-bold text-violet-100">—</span></div>
        </div>
    </header>

    <!-- Board -->"""
content = re.sub(body_pattern, new_body, content, flags=re.DOTALL)

# Add Marquee Reviews section before Modals
board_end_pattern = r'(</main>)\s*<!-- Modals -->'
new_board_end = """</main>

    <!-- Wall of Love (Reviews) -->
    <section class="z-10 w-full mb-32" id="wall-of-love">
        <div class="text-center mb-8">
            <div class="section-label mb-2 text-fuchsia-400">Wall of Love</div>
            <h2 class="text-3xl font-bold text-[#f1f5f9]">Loved by builders everywhere.</h2>
        </div>
        <div class="marquee-wrapper">
            <div class="marquee left" id="marquee-1"></div>
            <div class="marquee right" id="marquee-2"></div>
        </div>
    </section>

    <!-- Modals -->"""
content = re.sub(board_end_pattern, new_board_end, content)

# Change <main class="..."> to add z-10 and mx-auto
main_pattern = r'<main class="flex-1 overflow-x-auto p-6 flex flex-col md:flex-row gap-6 relative">'
new_main = r'<main class="flex-1 w-full max-w-7xl mx-auto px-6 flex flex-col md:flex-row gap-6 relative z-10 mb-32">'
content = content.replace(main_pattern, new_main)

# Add JS for Reviews
js_inject_pattern = r'(// Init\s+renderBoard\(\);)'
reviews_js = """// Reviews Generation
        const reviews = [
            "Insane product", "Mind-blowing UX", "10x my workflow", "Best tool I've used", "Obsessed with this",
            "Pure magic", "Replaced 3 apps", "My team loves this", "Genuinely futuristic", "Game over for competitors",
            "Ship faster than ever", "This completely changed how our team ships. The AI layer is actually useful.",
            "Aesthetic alone made me show my whole team. Then they actually used it.",
            "I can never go back to Jira.", "Ollama integration is genius.", "Blazing fast UI.",
            "A masterclass in modern design.", "Saves me 2 hours a day.", "Simply perfect.",
            "The glowing path is so satisfying.", "Incredible value.", "Best Kanban out there.",
            "Finally, a smart task manager.", "Beautifully engineered.", "Top tier product."
        ];
        
        const authors = [
            "@prakash_dev · Product Lead", "@s_miriam · Founder", "@alex_codes · Engineer",
            "@design_ninja · UX Designer", "@sarah_ships · CEO", "@john_doer · VP Product",
            "@tech_guru · CTO", "@startup_steve · Maker"
        ];
        
        const colors = ["#a78bfa", "#60a5fa", "#ec4899"];
        const starsSVG = '<svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>';

        function createReviewCard(text, i) {
            const author = authors[i % authors.length];
            const color = colors[i % colors.length];
            const card = document.createElement('div');
            card.className = 'review-card glass-panel';
            card.style.borderLeftColor = color;
            card.innerHTML = `
                <div class="stars mb-3">${starsSVG.repeat(5)}</div>
                <p class="text-sm text-gray-200 mb-4 font-medium">"${text}"</p>
                <div class="text-xs text-muted">${author}</div>
            `;
            return card;
        }

        const m1 = document.getElementById('marquee-1');
        const m2 = document.getElementById('marquee-2');
        
        // 13 in first, 12 in second
        const r1 = reviews.slice(0, 13);
        const r2 = reviews.slice(13);

        const buildMarquee = (el, arr) => {
            if (!el) return;
            const fragment = document.createDocumentFragment();
            arr.forEach((text, i) => fragment.appendChild(createReviewCard(text, i)));
            el.appendChild(fragment);
            // Clone for infinite scroll
            const clone = el.innerHTML;
            el.innerHTML += clone;
        };

        buildMarquee(m1, r1);
        buildMarquee(m2, r2);

        // Init
        renderBoard();"""
content = re.sub(js_inject_pattern, reviews_js, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

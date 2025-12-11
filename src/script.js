/* ═══════════════════════════════════════════════════════════════════
   THE ARXIV SYNDICATE — SCRIPTS
   "Where the future leaks before it's announced"
   ═══════════════════════════════════════════════════════════════════ */

// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', () => {
    initScrollAnimations();
    initNavigation();
    initTerminalTyping();
    initCellInteractions();
    initGlitchEffect();
    initParallax();
});

/* === SCROLL ANIMATIONS === */
function initScrollAnimations() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');

                // Stagger child animations
                const children = entry.target.querySelectorAll('.animate-child');
                children.forEach((child, index) => {
                    child.style.animationDelay = `${index * 0.1}s`;
                    child.classList.add('visible');
                });
            }
        });
    }, observerOptions);

    // Observe sections
    document.querySelectorAll('section').forEach(section => {
        section.classList.add('animate-on-scroll');
        observer.observe(section);
    });

    // Observe specific elements
    document.querySelectorAll('.cell-card, .pattern-card, .epoch-item').forEach(el => {
        el.classList.add('animate-on-scroll');
        observer.observe(el);
    });
}

/* === NAVIGATION === */
function initNavigation() {
    const nav = document.querySelector('.nav');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        // Add/remove background on scroll
        if (currentScroll > 100) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }

        // Hide/show nav on scroll direction
        if (currentScroll > lastScroll && currentScroll > 500) {
            nav.style.transform = 'translateY(-100%)';
        } else {
            nav.style.transform = 'translateY(0)';
        }

        lastScroll = currentScroll;
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 80;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/* === TERMINAL TYPING EFFECT === */
function initTerminalTyping() {
    const terminalBody = document.querySelector('.terminal-body');
    if (!terminalBody) return;

    const commands = [
        { type: 'command', text: './activate-syndicate.sh', delay: 100 },
        { type: 'output', text: 'SYNDICATE INITIALIZED', delay: 500 },
        { type: 'output', text: 'CELLS: SCANNER, WEAVER, HYPERLEXIC, ARCHITECT, ORCHESTRA', delay: 200 },
        { type: 'output', text: 'STATUS: ACTIVE', delay: 200 },
        { type: 'command', text: 'Activate THE ARXIV SYNDICATE. Full pipeline. Ship the zine.', delay: 1000 }
    ];

    // Store original content
    const originalContent = terminalBody.innerHTML;

    // Create new terminal content on intersection
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateTerminal(terminalBody, commands);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    observer.observe(terminalBody);
}

function animateTerminal(container, commands) {
    container.innerHTML = '';
    let totalDelay = 0;

    commands.forEach((cmd, index) => {
        totalDelay += cmd.delay;

        setTimeout(() => {
            const line = document.createElement('div');
            line.className = 'terminal-line' + (cmd.type === 'output' ? ' output' : '');

            if (cmd.type === 'command') {
                const prompt = document.createElement('span');
                prompt.className = 'prompt';
                prompt.textContent = '$';
                line.appendChild(prompt);

                const command = document.createElement('span');
                command.className = 'command';
                line.appendChild(command);

                container.appendChild(line);

                // Type out the command
                typeText(command, cmd.text, 30);
            } else {
                const span = document.createElement('span');

                // Check for status active
                if (cmd.text.includes('ACTIVE')) {
                    span.innerHTML = 'STATUS: <span class="status-active">ACTIVE</span>';
                } else {
                    span.textContent = cmd.text;
                }

                line.appendChild(span);
                container.appendChild(line);
            }
        }, totalDelay);
    });
}

function typeText(element, text, speed) {
    let index = 0;
    const type = () => {
        if (index < text.length) {
            element.textContent += text.charAt(index);
            index++;
            setTimeout(type, speed);
        } else {
            // Add blinking cursor at the end
            element.classList.add('typing');
        }
    };
    type();
}

/* === CELL INTERACTIONS === */
function initCellInteractions() {
    const cellNodes = document.querySelectorAll('.cell-node[data-cell]');
    const cellCards = document.querySelectorAll('.cell-card');

    cellNodes.forEach(node => {
        node.addEventListener('click', () => {
            const cellId = node.dataset.cell;
            const targetCard = document.getElementById(`cell-${cellId}`);

            if (targetCard) {
                targetCard.scrollIntoView({ behavior: 'smooth', block: 'center' });

                // Highlight effect
                targetCard.classList.add('highlight');
                setTimeout(() => {
                    targetCard.classList.remove('highlight');
                }, 2000);
            }
        });

        // Hover effects
        node.addEventListener('mouseenter', () => {
            node.style.transform = 'scale(1.02) translateX(10px)';
        });

        node.addEventListener('mouseleave', () => {
            node.style.transform = '';
        });
    });
}

/* === GLITCH EFFECT === */
function initGlitchEffect() {
    const title = document.querySelector('.hero-title');
    if (!title) return;

    // Random glitch on the title
    setInterval(() => {
        if (Math.random() > 0.95) {
            title.classList.add('glitch');
            setTimeout(() => {
                title.classList.remove('glitch');
            }, 200);
        }
    }, 2000);
}

/* === PARALLAX EFFECT === */
function initParallax() {
    const hero = document.querySelector('.hero');
    const gridOverlay = document.querySelector('.grid-overlay');

    if (!hero || !gridOverlay) return;

    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const rate = scrolled * 0.3;

        if (scrolled < window.innerHeight) {
            gridOverlay.style.transform = `translate(${rate}px, ${rate}px)`;
        }
    });
}

/* === ADDITIONAL STYLES FOR JS EFFECTS === */
const styleSheet = document.createElement('style');
styleSheet.textContent = `
    .nav {
        transition: transform 0.3s ease, background 0.3s ease;
    }

    .nav.scrolled {
        background: rgba(10, 10, 15, 0.98);
    }

    .animate-on-scroll {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }

    .animate-on-scroll.visible {
        opacity: 1;
        transform: translateY(0);
    }

    .cell-card.highlight {
        animation: highlightPulse 2s ease;
    }

    @keyframes highlightPulse {
        0%, 100% {
            box-shadow: 0 0 0 0 rgba(0, 255, 136, 0);
        }
        50% {
            box-shadow: 0 0 40px rgba(0, 255, 136, 0.4);
        }
    }

    .glitch {
        animation: glitch 0.2s ease;
    }

    @keyframes glitch {
        0% {
            transform: translate(0);
            text-shadow: none;
        }
        20% {
            transform: translate(-2px, 2px);
            text-shadow: 2px 0 #ff3366, -2px 0 #00ff88;
        }
        40% {
            transform: translate(-2px, -2px);
            text-shadow: 2px 0 #00ff88, -2px 0 #ff3366;
        }
        60% {
            transform: translate(2px, 2px);
            text-shadow: 2px 0 #ff3366, -2px 0 #00ff88;
        }
        80% {
            transform: translate(2px, -2px);
            text-shadow: -2px 0 #00ff88, 2px 0 #ff3366;
        }
        100% {
            transform: translate(0);
            text-shadow: none;
        }
    }

    .cell-node {
        transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    }

    /* Mobile menu improvements */
    @media (max-width: 768px) {
        .nav-links {
            position: fixed;
            top: 60px;
            left: 0;
            right: 0;
            background: rgba(10, 10, 15, 0.98);
            padding: 1rem;
            border-bottom: 1px solid var(--border-color);
            transform: translateY(-100%);
            opacity: 0;
            transition: transform 0.3s ease, opacity 0.3s ease;
            pointer-events: none;
        }

        .nav-links.active {
            transform: translateY(0);
            opacity: 1;
            pointer-events: all;
        }
    }
`;
document.head.appendChild(styleSheet);

/* === EASTER EGG: KONAMI CODE === */
const konamiCode = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
let konamiIndex = 0;

document.addEventListener('keydown', (e) => {
    if (e.key === konamiCode[konamiIndex]) {
        konamiIndex++;
        if (konamiIndex === konamiCode.length) {
            activateSecretMode();
            konamiIndex = 0;
        }
    } else {
        konamiIndex = 0;
    }
});

function activateSecretMode() {
    document.body.style.transition = 'filter 0.5s ease';
    document.body.style.filter = 'hue-rotate(180deg)';

    const message = document.createElement('div');
    message.innerHTML = `
        <div style="
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0, 0, 0, 0.95);
            border: 2px solid #ff3366;
            padding: 2rem 3rem;
            font-family: 'JetBrains Mono', monospace;
            color: #ff3366;
            z-index: 10000;
            text-align: center;
            animation: fadeIn 0.5s ease;
        ">
            <div style="font-size: 1.5rem; margin-bottom: 1rem;">THE SYNDICATE SEES ALL</div>
            <div style="font-size: 0.8rem; color: #888;">You found the secret. Stay paranoid.</div>
        </div>
    `;
    document.body.appendChild(message);

    setTimeout(() => {
        message.remove();
        document.body.style.filter = '';
    }, 3000);
}

/* === CONSOLE MESSAGE === */
console.log(`
%c
╔═══════════════════════════════════════════════════════════════╗
║              THE ARXIV SYNDICATE                              ║
║       "Where the future leaks before it's announced"          ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║   You found the console. Of course you did.                   ║
║                                                               ║
║   The patterns are everywhere.                                ║
║   You just have to know where to look.                        ║
║                                                               ║
║   Stay paranoid. Stay curious. Stay ahead.                    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
`, 'color: #00ff88; font-family: monospace; font-size: 10px;');

# Contributing to The Arxiv Syndicate

First off, thank you for considering contributing to The Arxiv Syndicate. The future leaks faster when more people are watching.

## Code of Conduct

- Be respectful and constructive
- Stay paranoid, but stay civil
- The math is in the margins — show your work

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title** describing the issue
- **Steps to reproduce** the behavior
- **Expected behavior** vs. actual behavior
- **Screenshots** if applicable
- **Environment** (browser, OS, screen size)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title** describing the suggestion
- **Detailed description** of the proposed functionality
- **Why this enhancement would be useful**
- **Possible implementation** approach (optional)

### Pull Requests

1. **Fork the repo** and create your branch from `main`
2. **Follow the code style** — we use vanilla HTML/CSS/JS
3. **Test your changes** across different browsers
4. **Update documentation** if needed
5. **Write a clear PR description**

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/ArxivSynFire.git
cd ArxivSynFire

# Install dependencies (optional, for dev server)
npm install

# Start development server
npm start

# Or use Python
python -m http.server 8000 -d src
```

## Style Guidelines

### HTML

- Semantic HTML5 elements
- Meaningful class names
- Accessibility attributes where appropriate

### CSS

- Use CSS custom properties (variables) for theming
- Mobile-first responsive design
- BEM-like naming convention
- Comments for complex selectors

### JavaScript

- Vanilla JS only (no frameworks)
- ES6+ features
- Clear function names
- Comments for complex logic

### Git Commit Messages

Follow conventional commits:

```
feat: add new section for paradigm analysis
fix: correct animation timing on mobile
docs: update README with new features
style: improve code formatting
refactor: simplify scroll animation logic
```

## Project Structure

```
ArxivSynFire/
├── src/                 # Source files
│   ├── index.html      # Main HTML
│   ├── styles.css      # Styles
│   └── script.js       # JavaScript
├── assets/             # Static assets
├── docs/               # Documentation
└── ...
```

## Questions?

Open an issue with the `question` label.

---

*Stay paranoid. Stay curious. Stay ahead.*

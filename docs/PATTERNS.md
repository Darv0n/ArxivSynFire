# Pattern Library

Reference patterns for THE HYPERLEXIC and THE ARCHITECT.

---

## Mathematical Equivalences

These are the same thing with different names:

### Attention is Matrix Factorization

```
Self-attention = softmax over dot products = learned factorization
Memory networks = external matrix lookup
Same operation, different marketing
```

### Diffusion is Score Matching is Denoising

```
Diffusion models = learn to reverse noise
Score matching = learn gradient of log density
Denoising autoencoders = learn to remove noise
Three names, one idea, decades apart
```

### Transformers are Hopfield Networks

```
Attention = associative memory retrieval
Modern transformers = continuous Hopfield with softmax
1982 → 2017, same core mechanics
```

### RL is Just Search with Gradients

```
Policy gradient = differentiable search
MCTS + neural nets = learned search heuristics
AlphaGo = search + learning = RL
```

### Everything is Optimization

```
Training = optimization
Inference = optimization (energy-based view)
Evolution = optimization (fitness)
Markets = optimization (utility)
```

### Everything is Compression

```
Learning = compression
Intelligence = compression
Prediction = compression
Kolmogorov complexity = the measure
```

### Everything is Prediction

```
Perception = prediction
Action = prediction of outcomes
Language = next token prediction
Intelligence = prediction machine
```

---

## Architectural Genealogies

### Neural Network Evolution

```
Perceptrons (1958)
    ↓
MLPs + Backprop (1986)
    ↓
CNNs (1989/2012)
    ↓
RNNs → LSTMs (1997)
    ↓
Attention (2014)
    ↓
Transformers (2017)
    ↓
??? (emerging)
```

### Generative Model Evolution

```
Boltzmann Machines (1985)
    ↓
VAEs (2013)
    ↓
GANs (2014)
    ↓
Flow Models (2015)
    ↓
Diffusion (2015/2020)
    ↓
??? (emerging)
```

### Scale Evolution

```
Feature Engineering Era
    ↓
Model Engineering Era
    ↓
Scale Era (compute = capability)
    ↓
Data Era (quality > quantity?)
    ↓
??? (emerging)
```

---

## Discovery Heuristics

### Low Hype, High Signal

- Papers with <10 citations doing what big labs announced months later
- Workshop papers that become main conference best papers
- Preprints from unknown authors that get acquired
- Techniques from 2018 appearing in 2024 production systems

### Talent Movement Signals

- Same first author, different institutions = person moved
- Author disappears from arxiv = joined industry (or had a baby)
- Sudden co-authorship with big lab = collaboration or acquisition
- Senior researcher starts advising startups = planning exit

### Funding/Commercial Signals

- Arxiv preprint → company blog post gap <30 days = commercialization imminent
- Patent filed 6-18 months before paper = serious commercial intent
- Open source release = commoditizing competitor's advantage
- Hiring spree for specific skill = about to announce something

### Silence Signals

- Lab stops publishing on topic = either solved it or gave up
- Company removes feature = didn't work
- Researcher changes topic = previous approach hit wall
- PR goes quiet = bad news incoming

### Paradigm Shift Signals

- Multiple labs converge on same approach independently
- Old technique suddenly gets new name and traction
- "It's just [simple thing]" papers start appearing
- Benchmarks stop mattering (everyone saturates)

---

## Prior Art Reference

Common reinventions to check:

| Current Buzzword | Historical Equivalent | Original |
|-----------------|----------------------|----------|
| "Neural scaling laws" | Learning curves | 1990s statistical learning |
| "In-context learning" | Meta-learning, few-shot | 2016-2017 |
| "Chain of thought" | Decomposition, intermediate steps | Classical AI planning |
| "RLHF" | Preference learning, IRL | 2000s |
| "Mixture of experts" | Mixture of experts | 1991 (Jacobs et al.) |
| "Retrieval augmentation" | Case-based reasoning | 1980s |
| "Prompt engineering" | Feature engineering | Always |
| "Emergent capabilities" | Phase transitions | Statistical physics |
| "Multimodal" | Multi-view learning | 1990s |
| "World models" | Learned simulators | 1980s (Sutton, Schmidhuber) |

---

## Source Tier Reference

### Tier 1: Primary Sources

- arxiv.org (preprints, fastest)
- OpenReview (conference reviews, honest)
- GitHub (code, ground truth)
- Patent filings (legal = serious)

### Tier 2: Curated Sources

- Papers With Code (benchmarks)
- Semantic Scholar (citations)
- Conference proceedings (peer reviewed)
- Official company blogs (first-party)

### Tier 3: Analysis Sources

- Distill.pub (if it still published)
- Quality substacks (Sander Dieleman, Lilian Weng)
- Research group blogs (BAIR, Google AI)

### Tier 4: Signal (Inverse Reliability)

- Twitter/X (hype indicator, not truth)
- Tech press (lagging, often wrong)
- LinkedIn (career signaling)
- Press releases (pure PR)

**Rule:** The more polished the announcement, the less novel the work.

---

## Hype Calibration

### Overrated Signals

- "Revolutionary" in press release
- Celebrity researcher involved
- Massive Twitter engagement
- Corporate PR-driven announcement
- Benchmark SOTA without code release

### Underrated Signals

- Workshop paper, not main conference
- Unknown institution
- No Twitter presence
- Dense mathematical notation
- Negative results paper
- "Simple baseline" papers

### Red Flags

- Benchmark designed by same authors
- Results only on toy datasets
- No ablations
- "Details in appendix" for key components
- Code "coming soon" forever

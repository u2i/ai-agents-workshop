<div class="container">
<div class="main-content">

<img src="./.svg/we_are_U2I.svg">

<br><br>

u2i is a Kraków-based software house that just recently turned 25. We specialize in Medtech and Edtech, having worked on 15+ projects within these fields, with some partnerships lasting over 10 years.

**How we work**

- We build long-term partnerships with our clients, which means more trust and space to grow and less project hopping.
- We build small, autonomous teams where everyone's voice actually matters. Developers work closely with clients, not just follow tickets.

**Growth & culture**

- We invest heavily in development: mentoring, feedback, self-dev time, and more.
- u2iers participate in the company's profit and have transparent access to data.

**Why join u2i**

- You will be involved in the full product lifecycle, from high-level architecture to deployment, working directly with our US-based partners.
- You will have space to take ownership, learn fast, and work on meaningful software with people who care.
- You get free lunches and a full pantry.

</div>
</div>
<br><br>

<img src="./.svg/check_out_our_social_media_channels.svg">

<br>

<a href="https://u2i.com/careers"><img src="./.svg/world-wide-web.svg"></a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://linkedin.com/company/u2i"><img src="./.svg/linkedin.svg"></a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://instagram.com/u2ikrk"><img src="./.svg/instagram.svg"></a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://facebook.com/u2ikrk"><img src="./.svg/facebook.svg"></a>

<br>

---

# AI Agents Workshop

This repository contains materials and exercises for AI Agents Workshop.

### Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop/)
- [Task/Taskfile](https://taskfile.dev/docs/installation) (optional, but recommended)
- [VS Code Jupyter Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) (optional, but recommended)

### 1. Workshop plan
Learn the fundamentals through examples:
- Basic API calls to LLMs
- Function calling (Tools)
- Structured output
- What are the agents under the hood?

[View the workshop README](./workshop/README.md)

📚 Need help with some technical terms? See the [Glossary](./GLOSSARY.md) for explanations of HTTP, Docker, JSON, and more.

### 2. Discussion

---

### Homework
At home, solve a practical task located in `/homework` directory!

[View the homework README here](./homework/README.md)

---

## Repository Structure

```
.
├── workshop/
│   ├── 0_theory.md
│   ├── 1_simple_calls.ipynb
│   ├── 2_function_calling.ipynb
│   ├── 3_structured_output.ipynb
│   ├── 4_lets_loop.ipynb
│   └── scripts/                 # Benchmark scripts that generated the charts
├── homework/                    # Homework for you!
├── homework_test/               # Test module for the homework
├── GLOSSARY.md                  # Technical terms explained
└── .docker/                     # Docker configuration files
```
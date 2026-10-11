# Pitwall

This is a 3-year personal training program in F1 data engineering and race strategy, 
built alongside an Ingénieur Data Science degree at Faculty of Science of Tunis. Everything here is 
built in public, from scratch, with the goal of becoming the first Tunisian to work 
as a race strategy engineer in Formula 1.

## Progress

| Chapter | Topic | Status |
|---|---|---|
| A | Foundations & Tools | 🟡 In Progress |
| B | Exploratory Data & Visualization | ⬜ Not Started |
| C | Motorsport Performance Analytics | ⬜ Not Started |
| D | Modeling, Simulation & Strategy | ⬜ Not Started |
| E | Systems, Live Data & Deployment | ⬜ Not Started |

## Setup

Clone the repo and create a virtual environment:

```bash
git clone git@github.com:MouafekErrachi/pitwall.git
cd pitwall
python -m venv .venv
```

Activate the environment:

```bash
# On Windows
.venv\Scripts\activate

# On Mac or Linux
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r f1_training/A_foundations/requirements.txt
```

## Structure
pitwall/

├── f1_training/

├── A_foundations/

│ ├── notebooks/ # Lesson notebooks

│ ├── scripts/ # Reusable functions and tests

│ └── data/ # Local data files, not tracked by Git

├── B_exploration/

├── C_motorsport_analytics/

├── D_modeling_strategy/

└── E_systems_deployment/

## Goal
Become an F1 race strategy engineer. Every lesson is applied to real 
motorsport data including FastF1 telemetry, AIM MyChron karting exports 
and Monte Carlo pit stop simulation.
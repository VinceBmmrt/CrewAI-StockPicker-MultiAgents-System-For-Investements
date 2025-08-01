# StockPicker

---

## 🇫🇷  
StockPicker est un projet basé sur **CrewAI** qui orchestre la collaboration entre des agents IA spécialisés dans l'analyse de marchés boursiers. L'objectif : automatiser la recherche, l'analyse et la recommandation d'opportunités d'investissement dans un secteur donné.

Chaque agent coopère dans un processus hiérarchique pour :

- 🔍 Identifier les entreprises les plus tendances via une recherche en ligne (actualités, popularité, secteurs dynamiques).
- 📊 Mener une analyse financière détaillée sur ces entreprises.
- 📝 Rédiger une recommandation finale à destination de l'utilisateur.
- 📲 Envoyer une **notification push personnalisée sur le mobile** de l'utilisateur avec la recommandation finale.

StockPicker intègre également différents types de mémoires (court terme, long terme, entités) grâce à une base SQLite et l'utilisation d'**embeddings via Google Generative AI** pour renforcer la compréhension contextuelle.

---

## 🇬🇧  
StockPicker is a project powered by **CrewAI**, orchestrating collaboration between specialized AI agents to automate market research and stock investment recommendations.

Agents collaborate hierarchically to:

- 🔍 Identify trending companies within a given sector using online search and trend analysis.
- 📊 Perform deep financial analysis of shortlisted companies.
- 📝 Generate a final recommendation for investment.
- 📲 Send a **custom push notification to the user's mobile** with the final recommendation.

The system also integrates various memory layers (short-term, long-term, entity) using a local SQLite DB and **Google Generative AI embeddings** for semantic context and relevance.

---

## Features

- 🤖 Collaborative autonomous agents coordinated via Crew AI.  
- 🌐 Internet research for trending companies using Serper.dev API.  
- 📈 Financial deep-dive analysis by a specialized research agent.  
- 💡 Automated decision-making with investment recommendation.  
- 📲 Custom push notifications sent to user’s mobile via a dedicated tool.  
- 🗂 Hierarchical task delegation and process orchestration.  
- 🧠 Contextual memory management (short-term, long-term, entity memories).  
- 💾 Memory storage using SQLite and RAG (Retrieval Augmented Generation) system.  
- 🔍 Use of Google generative AI embeddings for semantic memory.

---

## Demo

🎥 [Video demonstration](https://drive.google.com/file/d/1HG1JC5O2oSJlb37m414rXMAWGtmwg8dD/view)

The model initially seems to format the push notification incorrectly when using the send push notification tool, but it self-corrects after failing and manages to send the notification. I tried to improve the prompt, but the behavior seems to vary depending on the model used. I kept this as it’s interesting to see how the agent can autonomously recover from its own mistakes.

---

## Agents Configuration  
LLMs and tools used by each agent are configurable in `config/agents.yaml`. Example agents include:

- 🔎 **trending_company_finder**: Analyzes current trends and filters top-performing companies by sector.  
- 📊 **financial_researcher**: Performs in-depth financial and strategic analysis.  
- 📈 **stock_picker**: Makes the final investment recommendation and sends the final decision via push notification to the user.  
- 🤝 **manager**: Coordinates the entire process between agents and ensures task completion.

---

## Tasks

### find_trending_companies  
Searches for trending companies in a given sector using internet search tools like SerperDevTool. Produces a list of candidates with basic info.

### research_trending_companies  
Analyzes financial performance, risks, and growth potential of shortlisted companies. Outputs structured insights.

### pick_best_company  
Selects the best investment opportunity based on prior research. Outputs a short, final recommendation.

---

## Crew Configuration  
The main crew is defined in `stock_picker/crew.py`:

- 🌐 Web search is enabled via `SerperDevTool`.  
- 📲 Push notification is handled via a custom tool using **Pushover API**.

---


## Installation

**Requirements**:  
- 🐍 Python ≥3.10 and <3.14

Install uv (recommended):  
https://docs.astral.sh/uv/getting-started/first-steps/

Install dependencies:
bash
uv sync


You also need your to write your keys in the .env files, you ca look at .env.example for more details.

---

## Usage

Run the project with:
bash
crewai run


This will launch the full pipeline and output the final result in the console.

---

## Customization

- Add your API keys in .env (GOOGLE_API_KEY, PUSHOVER_USER, PUSHOVER_TOKEN, etc.)  
- Edit config/agents.yaml and config/tasks.yaml to tweak agent roles and task prompts.  
- Modify stock_picker/crew.py to change the execution flow or add memory/tools.  
- Adjust main.py to set your target sector or add runtime arguments.

---

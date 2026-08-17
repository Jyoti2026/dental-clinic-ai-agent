# dental-clinic-ai-agent
# Dental Clinic AI Automation Agent
An intelligent, tool-calling backend orchestration system designed to automate patient inquiry sorting, clinic capacity checking, and critical emergency routing for a dental practice.

## 📁 Repository Structure
```text
├── src/
│   ├── clinic_tools.py     # Functional interfaces (Mock Database & Calendar APIs)
│   └── agent_core.py       # Decision-making orchestration layer (LangChain-based engine)
├── requirements.txt         # Package configuration
└── README.md                # Project documentation
```

## 🧠 System Architecture & Capability Layout
1. **Intent Interpretation & Parsing**: Evaluates raw customer inputs (text or transcribed voice metrics) without explicit hardcoded rules or regular expressions.
2. **Autonomous Tool Routing**: The core engine evaluates patient intent and dynamically executes the appropriate internal utility module (e.g., matching open calendar blocks or flagging extreme surgical cases).
3. **Emergency Safeguards**: Contains hardcoded structural heuristics to identify critical conditions (severe bleeding, structural trauma) and automatically flag them for immediate human intervention.

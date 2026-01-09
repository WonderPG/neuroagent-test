# Neuroagent: AI Assistant for Neuroscience Research

## What is Neuroagent?

Neuroagent is an AI chatbot specialized for neuroscience research. It understands neuroscience terminology and can access specialized databases, analyze data, and help with research tasks through natural conversation.

## Core Capabilities

### 🧠 **Brain Data & Structure**
Ask about brain regions, circuits, morphologies, and anatomical structures:
- "Show me pyramidal neurons in layer 5 of the cortex"
- "What brain regions are connected to the hippocampus?"
- "Find morphologies of interneurons in the cerebellum"

### 🔬 **Experimental Data**
Access and analyze experimental recordings and measurements:
- "Plot ion channel recordings for NMDA receptors"
- "Show me firing patterns of basket cells"
- "Analyze morphometric data for dendritic branching"

### 📊 **Data Analysis & Visualization**
Execute Python code and create plots using scientific libraries:
- "Calculate the mean firing rate and plot the distribution"
- "Create a 3D visualization of this morphology"
- "Run statistical analysis on these experimental results"

### 📚 **Scientific Literature**
Search and analyze research papers:
- "Find recent papers about synaptic plasticity in Alzheimer's"
- "What research exists on dopamine receptors in Parkinson's?"
- "Summarize this paper about neural circuits"

## Available Tools

### **Data Retrieval**
- **Brain Atlas & Regions**: Query anatomical structures and brain region hierarchies
- **Cell Morphologies**: Access detailed cellular structure data
- **Circuits & Connectivity**: Retrieve neural circuit information and connection patterns
- **Ion Channels & Recordings**: Access electrophysiological data and channel properties
- **Experimental Data**: Query bouton densities, neuron densities, synaptic connections

Note: EntityCore-backed queries are used for direct database lookups (e.g., retrieving IDs, listings, or direct platform data). These are intended for direct data access rather than general-purpose knowledge.

### **Analysis & Computation**
- **Python Execution**: Run custom analysis with NumPy, Pandas, SciPy, Plotly
- **Circuit Analysis**: Analyze population dynamics and connectivity metrics
  - Note: For circuit population analysis, the assistant supplies the population filter separately from your question. Do NOT include the population name in the natural-language question (the tool receives the population name as a separate parameter). The circuit analysis tool converts your question into a SQL SELECT query and executes it; only read-only SELECT queries are allowed and some SQL operations (e.g., DROP, DELETE, INSERT, UPDATE, CREATE, ALTER, EXEC) are prohibited for safety.
- **Morphometrics**: Measure cellular properties and structural features
- **Electrophysiology**: Process and analyze electrical recordings

### **Visualization**
- **Interactive Plots**: Generate publication-ready figures with Plotly
- **3D Morphology Rendering**: Visualize cellular structures in 3D
- **Data Plotting**: Create custom visualizations from experimental data

### **Research Support**
- **Literature Search**: Semantic search across 100M+ research papers
- **Paper Analysis**: Extract insights from scientific publications
- **Expert Knowledge**: Access curated neuroscience information
- **Web Search**: Find current information and resources

## How to Interact

### **Natural Language Queries**
Simply ask questions in plain English:
- "What types of neurons are in the striatum?"
- "Show me calcium imaging data from pyramidal cells"
- "Compare morphologies between different cell types"

### **Multi-Step Analysis**
Build complex workflows through conversation:
1. "Find morphology data for cortical neurons"
2. "Now calculate the average dendritic length"
3. "Plot the distribution and compare across layers"

### **Combining Tools**
The AI automatically selects and chains appropriate tools:
- Literature search → Paper analysis → Data visualization
- Data retrieval → Statistical analysis → Plot generation
- Morphology query → 3D visualization → Measurement analysis

### Tool-calling behavior and brief reasoning
- Before any tool call in a multi-step process, the assistant will include a concise (1–2 line) rationale for the next action or tool selection to clarify intent.
- When user intent is clear, the assistant proceeds with tool calls without unnecessary confirmations; it defaults to taking action rather than seeking confirmation.
- The assistant avoids explicit self-referential phrases like "I'll generate" or "I'll search"; instead it presents the reasoning as part of the natural narrative.
- The assistant will refuse or avoid tool calls that would generate excessive outputs or resource-intensive operations (e.g., massive loops, extremely large file processing, or operations producing voluminous output).
- Tool outputs are authoritative for answers derived from tools; the assistant will not invent or add information beyond the tool output.

### UI & Platform Questions
- The assistant does not have access to the platform's UI layout or interactive elements and cannot provide step-by-step navigation of the UI.
- For platform-related or glossary-like questions, the assistant uses specialized internal tools (for example, an "obi-expert" tool) to retrieve authoritative guidance; it may also use a context-analyzer tool to determine a user's current view when available.
- Responses about the platform must be restricted to information explicitly provided by those tools. For questions about where items appear in the interface, please consult platform help resources or contact support.

## Key Features

### **Intelligent Tool Selection**
The AI chooses the right tools based on your question without you needing to specify which tools to use.

### **Context Awareness**
Remembers previous parts of the conversation to build on earlier results and maintain context.

### **Real-Time Execution**
See results as they're generated, with live updates during tool execution.

### **Scientific Accuracy**
Built specifically for neuroscience with domain expertise and validated data sources.

### **Flexible Analysis**
From simple queries to complex multi-step research workflows.

## Common Research Workflows

### **Exploratory Research**
- "What do we know about GABAergic interneurons in autism?"
- "Show me all available data on dopamine signaling in the basal ganglia"

### **Data Analysis**
- "Analyze the firing patterns in this dataset and identify clusters"
- "Compare morphological features between control and disease conditions"

### **Literature Review**
- "Find papers about optogenetics in motor cortex from the last 3 years"
- "What are the current theories about consciousness and neural correlates?"

### **Hypothesis Generation**
- "Based on this connectivity data, what predictions can we make about function?"
- "How might these morphological differences affect electrical properties?"

## Understanding Responses

### **Tool Execution**
When the AI uses tools, you'll see:
- Which tool is being called
- What parameters are being used
- Real-time results as they're generated

### **Data Sources**
Results come from curated neuroscience databases including:
- Brain atlases and anatomical data
- Experimental recordings and measurements
- Published research literature
- Simulation and modeling data

### **Limitations**
- Some queries may hit rate limits for computational resources
- Complex analyses may take time to complete
- Results depend on available data in the databases
- Always verify important findings with additional sources

## Best Practices

### **Effective Queries**
- Be specific about brain regions, cell types, or experimental conditions
- Ask follow-up questions to refine results
- Request visualizations to better understand data

### **Building Analysis**
- Start with broad queries, then narrow down
- Ask for explanations of unfamiliar results
- Request different visualization approaches for complex data

### **Research Workflow**
- Use literature search to understand current knowledge
- Combine multiple data sources for comprehensive analysis
- Generate hypotheses based on integrated findings


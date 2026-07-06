# LangChain Models Demo

This project provides examples and demonstrations of various AI models using the LangChain framework. It includes implementations for LLMs, Chat Models, Embedded Models, and structured outputs.

## Project Structure

- `1.LLMs/`: Examples of using standard Large Language Models.
- `2.ChatModels/`: Examples demonstrating Chat Models (e.g., OpenAI, Anthropic, Gemini).
- `3.EmbeddedModels/`: Examples of text embeddings and related use cases.
- `structured_output/`: Demonstrations on getting structured data/outputs from models (e.g., using Pydantic).
- `prompts/`: Prompt management and templates.
- `vhack/`: Additional tools and utilities.

## Setup Instructions

### Prerequisites
Make sure you have Python installed. It is recommended to use a virtual environment.

### STEP 1: Install Dependencies

Install LangChain and AI model dependencies:

```bash
pip install -r requirement.txt
```

### STEP 2: Configure Environment Variables

Create a `.env` file in the root directory and add your API keys (e.g., OpenAI, Anthropic, Google Gemini, Hugging Face). 

Example `.env` content:
```env
OPENAI_API_KEY=your_api_key_here
ANTHROPIC_API_KEY=your_api_key_here
GOOGLE_API_KEY=your_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_api_key_here
```

### STEP 3: Run the Examples

Navigate to the specific folders and run the Python scripts to see the models in action.
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
    Please summarize the research paper title {paper_input}
    Explanation style: {explanation_style}
    Explanation length: {explanation_length}
    """,
    input_variables=["paper_input", "explanation_style", "explanation_length"]
)

template.save("./json_prompts/prompt_template.json")

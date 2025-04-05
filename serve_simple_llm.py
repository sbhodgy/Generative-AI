from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from databricks_langchain import ChatDatabricks
from langserve import add_routes

system_template = "You are an assistant that translates text. Translate the user text into {language}."
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

model = ChatDatabricks(endpoint="databricks-meta-llama-3-3-70b-instruct", temperature=0.0)

# llm = HuggingFaceEndpoint(
#     repo_id="microsoft/Phi-3-mini-4k-instruct",
#     task="text-generation",
#     max_new_tokens=512,
#     do_sample=False,
#     repetition_penalty=1.03
# )

# model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = prompt_template | model | parser

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces"
)

add_routes(
    app,
    chain,
    path=""
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)


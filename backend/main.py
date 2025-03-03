from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from vllm import LLM

from backend.models.codestral_25_01 import Codestral2501
from backend.routes import chat, history, mode, system_prompt
from backend.utils import authentication, database, session

app = FastAPI()

# Load environment variables
env_vars = {
    "LLM_MODEL": "codestral_25_01",
    "LLM_HOST": "localhost",
    "LLM_PORT": 8000,
    "LLM_PROTOCOL": "http",
    "LLM_API_KEY": "your_api_key",
    "LLM_SYSTEM_PROMPT_PATH": "backend/prompts/normal_mode.txt",
    "LLM_DARK_MAGIC_PROMPT_PATH": "backend/prompts/dark_magic_mode.txt",
    "LLM_MODE_COOKIE_NAME": "alchemist_mode",
    "LLM_MODE_COOKIE_VALUE_NORMAL": "normal",
    "LLM_MODE_COOKIE_VALUE_DARK_MAGIC": "dark_magic",
    "LLM_CHAT_HISTORY_COOKIE_NAME": "alchemist_chat_history",
    "LLM_CHAT_HISTORY_LOCAL_STORAGE_KEY": "alchemist_chat_history",
    "LLM_CHAT_HISTORY_DB_TABLE_NAME": "chat_history",
    "LLM_CHAT_HISTORY_DB_PATH": "backend/database.db",
    "LLM_CHAT_HISTORY_DB_ENGINE": "sqlite",
    "LLM_CHAT_HISTORY_DB_ECHO": False,
}

# Initialize LLM model
llm = LLM(
    model=env_vars["LLM_MODEL"],
    host=env_vars["LLM_HOST"],
    port=env_vars["LLM_PORT"],
    protocol=env_vars["LLM_PROTOCOL"],
    api_key=env_vars["LLM_API_KEY"],
)

# Load system prompt
with open(env_vars["LLM_SYSTEM_PROMPT_PATH"], "r") as f:
    system_prompt_text = f.read()

# Load dark magic mode system prompt
with open(env_vars["LLM_DARK_MAGIC_PROMPT_PATH"], "r") as f:
    dark_magic_prompt_text = f.read()

# Initialize database (if enabled)
db_engine = None
if env_vars["LLM_CHAT_HISTORY_DB_ENGINE"] == "sqlite":
    db_engine = database.init_sqlite_db(env_vars["LLM_CHAT_HISTORY_DB_PATH"])

# Initialize templates
templates = Jinja2Templates(directory="frontend/templates")

# Mount static files
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Include routes
app.include_router(chat.router)
app.include_router(history.router)
app.include_router(mode.router)
app.include_router(system_prompt.router)

# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "llm_model": env_vars["LLM_MODEL"],
            "llm_host": env_vars["LLM_HOST"],
            "llm_port": env_vars["LLM_PORT"],
            "llm_protocol": env_vars["LLM_PROTOCOL"],
            "llm_api_key": env_vars["LLM_API_KEY"],
            "llm_system_prompt_path": env_vars["LLM_SYSTEM_PROMPT_PATH"],
            "llm_dark_magic_prompt_path": env_vars["LLM_DARK_MAGIC_PROMPT_PATH"],
            "llm_mode_cookie_name": env_vars["LLM_MODE_COOKIE_NAME"],
            "llm_mode_cookie_value_normal": env_vars["LLM_MODE_COOKIE_VALUE_NORMAL"],
            "llm_mode_cookie_value_dark_magic": env_vars["LLM_MODE_COOKIE_VALUE_DARK_MAGIC"],
            "llm_chat_history_cookie_name": env_vars["LLM_CHAT_HISTORY_COOKIE_NAME"],
            "llm_chat_history_local_storage_key": env_vars["LLM_CHAT_HISTORY_LOCAL_STORAGE_KEY"],
            "llm_chat_history_db_table_name": env_vars["LLM_CHAT_HISTORY_DB_TABLE_NAME"],
            "llm_chat_history_db_path": env_vars["LLM_CHAT_HISTORY_DB_PATH"],
            "llm_chat_history_db_engine": env_vars["LLM_CHAT_HISTORY_DB_ENGINE"],
            "llm_chat_history_db_echo": env_vars["LLM_CHAT_HISTORY_DB_ECHO"],
        },
    )

# Call LLM model with system prompt
def call_llm_model(prompt, system_prompt):
    response = llm.generate(
        prompt=prompt,
        system_prompt=system_prompt,
    )
    return response.outputs[0].text

# Call LLM model with dark magic mode system prompt
def call_llm_model_dark_magic(prompt):
    return call_llm_model(prompt, dark_magic_prompt_text)

# Call LLM model with normal mode system prompt
def call_llm_model_normal(prompt):
    return call_llm_model(prompt, system_prompt_text)
import json

def get_chat_history(request):
    chat_history_cookie = request.cookies.get("alchemist_chat_history")
    if chat_history_cookie:
        return json.loads(chat_history_cookie)
    return []

def set_chat_history(request, chat_history):
    chat_history_cookie = json.dumps(chat_history)
    response_headers = request.scope["response"]._headers
    response_headers.append(
        ("Set-Cookie", f"alchemist_chat_history={chat_history_cookie}; path=/")
    )

def get_mode(request):
    mode_cookie = request.cookies.get("alchemist_mode")
    if mode_cookie:
        return mode_cookie
    return "normal"

def switch_mode(request):
    mode_cookie = request.cookies.get("alchemist_mode")
    if mode_cookie == "normal":
        mode = "dark_magic"
    else:
        mode = "normal"
    response_headers = request.scope["response"]._headers
    response_headers.append(
        ("Set-Cookie", f"alchemist_mode={mode}; path=/")
    )
    return mode

def get_system_prompt(request):
    mode_cookie = request.cookies.get("alchemist_mode")
    if mode_cookie == "dark_magic":
        return "dark_magic_mode.txt"
    return "normal_mode.txt"

def set_system_prompt(request, system_prompt):
    response_headers = request.scope["response"]._headers
    response_headers.append(
        ("Set-Cookie", f"alchemist_system_prompt={system_prompt}; path=/")
    )
    return system_prompt
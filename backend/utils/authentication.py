from fastapi import HTTPException

def authenticate(username, password):
    # Implement your authentication logic here
    # Return True if authentication is successful, False otherwise
    pass

def get_current_user(request):
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    if not authenticate(username, password):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return username
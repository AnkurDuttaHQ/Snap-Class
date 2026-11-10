from src.database.config import supabase
import bcrypt


def hash_pass(pwd):
    
    return bcrypt.hashpw(
        pwd.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")



def check_pass(pwd, hashed):
    try:
        return bcrypt.checkpw(
            pwd.encode("utf-8"),
            hashed.encode("utf-8")
        )
    except (ValueError, TypeError, AttributeError):
        return False



def check_teacher_exists(username):

    response = (
        supabase
        .table("teachers")
        .select("username")
        .eq("username", username)
        .execute()
    )

    return len(response.data) > 0


def create_teacher(username, password, name):

    username = username.strip()
    name = name.strip()

    if not username or not password or not name:
        return None

    if check_teacher_exists(username):
        return None

    hashed_password = hash_pass(password)

    data = {
        "username": username,
        "password": hashed_password,
        "name": name
    }

    response = (
        supabase
        .table("teachers")
        .insert(data)
        .execute()
    )

    return response.data


def teacher_login(username, password):

    username = username.strip()

    if not username or not password:
        return None

    response = (
        supabase
        .table("teachers")
        .select("username, password, name")
        .eq("username", username)
        .execute()
    )

    if not response.data:
        return None

    teacher = response.data[0]

    if check_pass(password, teacher["password"]):

        return {
            "username": teacher["username"],
            "name": teacher["name"]
        }

    return None


def get_teacher(username):

    response = (
        supabase
        .table("teachers")
        .select("username, name")
        .eq("username", username)
        .execute()
    )

    if response.data:
        return response.data[0]

    return None

def get_all_students():
    response = supabase.table("students").select("*").execute()
    return response.data

def create_student(new_name,face_embedding=None,voice_embedding=None):
    data = {'name':new_name,'face_login':face_embedding,'voice_login':voice_embedding}
    response = supabase.table("students").insert(data).execute()
    return response.data
    
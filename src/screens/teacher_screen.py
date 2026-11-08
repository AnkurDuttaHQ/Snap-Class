import streamlit as st
from src.components.header import header_layout_dashboard_login_teacher,header_layout_dashboard_register_teacher
from src.ui.home_basic_layout import home_page_dashboard,style_base_layout
from src.components.footer import footer_layout_dashboard
from src.database.db import check_teacher_exists , create_teacher ,teacher_login

def teacher_screen():
    home_page_dashboard()
    style_base_layout()
    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=='login':
        teacher_screen_login()
    else:
        teacher_screen_register()

## teacher Dashboard 
def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    st.header(f"""Welcome {teacher_data["name"]}""")

## Intermediate function after login state chnage to dashboard
def login_teacher(username , password):
    if not username or not password:
        return False
    teacher = teacher_login(username , password)
    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data = teacher
        st.session_state.isLoggedin = True
        return True

    return False

def teacher_screen_login():
    header_layout_dashboard_login_teacher()
   
    st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Outfit:wght@400;500;600;700&display=swap');
    
            .teacher-page-title {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: clamp(20px, 4vw, 48px) !important;
                font-weight: 400 !important;
                line-height: 1.2 !important;
                letter-spacing: -1px !important;
                color: #24243D !important;
                text-align: center !important;
                margin: 15px 0 30px 0 !important;
            }

            /* Input fields */
            .stTextInput input {
                height: 55px !important;
                width : 100px !important;
                font-size: 17px !important;
                padding: 12px 20px !important;
                border-radius: 12px !important;
            }

            /* Input labels */
            .stTextInput label {
                font-size: 17px !important;
                margin-bottom: 8px;
            }
            </style>
            """, unsafe_allow_html=True)
    teacher_username = st.text_input("Enter your username",placeholder="john Doe")
    teacher_password = st.text_input("Enter your password",type="password")

    st.divider()

    btncol1,btncol2 = st.columns(2)

    with btncol1:
        if st.button('Login',type="primary",icon=":material/passkey:",shortcut="Enter",width="stretch"):
            if login_teacher(teacher_username,teacher_password):
                st.toast("Welcome Back!",icon="🤗")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid login Credentials")
    with btncol2:
        if st.button("Register",type="secondary",width="stretch",shortcut="Shift+Enter"):
            st.session_state.teacher_login_type="register"
            st.rerun()

    footer_layout_dashboard()


## Function to create a tacher profile 
def teacher_register(teacher_name,teacher_username,teacher_pass,teacher_confirm_pass):
    if not teacher_username or not teacher_pass or not teacher_confirm_pass:
        return False , "All Fields are required !"
    if check_teacher_exists(teacher_username):
        return False , " Username already taken"
    if teacher_pass != teacher_confirm_pass:
        return False , "Password doesn't match"
    try:
        create_teacher(teacher_username,teacher_pass,teacher_name)
        return True , "Successfully Registered ! Redirect to login...."
    except Exception as e :
        return False , "Registration failed !Unexpected Error"

def teacher_screen_register():
    header_layout_dashboard_register_teacher()
    st.markdown("""
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Outfit:wght@400;500;600;700&display=swap');
        
                .teacher-page-title {
                    font-family: 'Climate Crisis', sans-serif !important;
                    font-size: clamp(20px, 4vw, 48px) !important;
                    font-weight: 400 !important;
                    line-height: 1.2 !important;
                    letter-spacing: -1px !important;
                    color: #24243D !important;
                    text-align: center !important;
                    margin: 15px 0 30px 0 !important;
                }
    
                /* Input fields */
                .stTextInput input {
                    height: 55px !important;
                    width : 100px !important;
                    font-size: 17px !important;
                    padding: 12px 20px !important;
                    border-radius: 12px !important;
                }
    
                /* Input labels */
                .stTextInput label {
                    font-size: 17px !important;
                    margin-bottom: 8px;
                }
                </style>
                """, unsafe_allow_html=True)
    teacher_username = st.text_input("Enter your username",placeholder="johndoe")
    teacher_name = st.text_input("Enter your name",placeholder="John Doe")
    teacher_pass = st.text_input("Enter your password",type="password")
    teacher_confirm_pass=st.text_input("Conform Your Password",type="password")
    
    st.divider()
    
    btncol1,btncol2 = st.columns(2)
    
    with btncol1:
        if st.button("Register",type="primary",width="stretch",shortcut="Shift+Enter"):
            success , message = teacher_register(teacher_name,teacher_username, teacher_pass,teacher_confirm_pass)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type="login"
                st.rerun()
            else:
                st.error(message);

         
    with btncol2:
        
        if st.button('Login Instead',type="secondary",icon=":material/passkey:",shortcut="Enter",width="stretch"):
            st.session_state.teacher_login_type="login"
            st.rerun()
        
    footer_layout_dashboard()
    

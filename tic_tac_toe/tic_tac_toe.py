import streamlit as st
import random

st.set_page_config(page_title="Tic Tac Toe")

# simple background
st.markdown("""
<style>
.stApp{
    background-color:#5c6bc0;
}

h1{
    color:white;
    text-align:center;
}

.text{
    color:white;
    text-align:center;
    font-size:20px;
}

div.stButton > button{
    height:80px;
    font-size:35px;
    font-weight:bold;
    border-radius:10px;
    background:white;
    color:black;
}
</style>
""", unsafe_allow_html=True)

st.title("Tic Tac Toe")
st.markdown('<p class="text">Play with Computer</p>', unsafe_allow_html=True)

# board create
if "board" not in st.session_state:
    st.session_state.board = ["","","","","","","","",""]

if "result" not in st.session_state:
    st.session_state.result = ""

board = st.session_state.board

# winner function
def check(player):

    if board[0]==player and board[1]==player and board[2]==player:
        return True
    if board[3]==player and board[4]==player and board[5]==player:
        return True
    if board[6]==player and board[7]==player and board[8]==player:
        return True
    if board[0]==player and board[3]==player and board[6]==player:
        return True
    if board[1]==player and board[4]==player and board[7]==player:
        return True
    if board[2]==player and board[5]==player and board[8]==player:
        return True
    if board[0]==player and board[4]==player and board[8]==player:
        return True
    if board[2]==player and board[4]==player and board[6]==player:
        return True

    return False

# computer move
def computer():

    empty=[]

    for i in range(9):
        if board[i]=="":
            empty.append(i)

    if len(empty)>0:
        move=random.choice(empty)
        board[move]="O"

# player move
def play(pos):

    if board[pos]=="" and st.session_state.result=="":

        board[pos]="X"

        if check("X"):
            st.session_state.result="🎉 You Won"
            return

        computer()

        if check("O"):
            st.session_state.result="😢 Computer Won"
            return

        if "" not in board:
            st.session_state.result="🤝 Match Draw"

# game board
for r in range(3):

    cols=st.columns(3)

    for c in range(3):

        index=r*3+c

        with cols[c]:
            st.button(
                board[index] if board[index] else " ",
                key=index,
                on_click=play,
                args=(index,),
                use_container_width=True
            )

# result
if st.session_state.result!="":
    st.success(st.session_state.result)

# restart
if st.button("Restart Game"):
    st.session_state.board=["","","","","","","","",""]
    st.session_state.result=""
    st.rerun()

import streamlit as st
import random

st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮", layout="centered")

# Background and button styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #667eea, #764ba2);
}

h1 {
    color: white;
    text-align: center;
}

p {
    color: white;
    text-align: center;
    font-size:18px;
}

div.stButton > button {
    height: 90px;
    font-size: 30px;
    border-radius: 15px;
    border: none;
    background-color: white;
    color: #333;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #ddd;
}
</style>
""", unsafe_allow_html=True)

st.title("🎮 Tic Tac Toe")
st.write("### Play Against Computer 🤖")

# create board
if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "msg" not in st.session_state:
    st.session_state.msg = ""

board = st.session_state.board

# winner check
def check(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for w in wins:
        if board[w[0]] == player and board[w[1]] == player and board[w[2]] == player:
            return True
    return False

# computer move
def computer():
    empty = []

    for i in range(9):
        if board[i] == "":
            empty.append(i)

    if empty:
        move = random.choice(empty)
        board[move] = "O"

# play move
def play(pos):

    if board[pos] == "":
        board[pos] = "X"

        if check("X"):
            st.session_state.msg = "🎉 You Won!"
            return

        computer()

        if check("O"):
            st.session_state.msg = "😢 Computer Won!"
            return

        if "" not in board:
            st.session_state.msg = "🤝 Match Draw"

# board
for r in range(3):
    cols = st.columns(3)

    for c in range(3):
        index = r * 3 + c
        with cols[c]:
            st.button(
                board[index] if board[index] else " ",
                key=index,
                on_click=play,
                args=(index,),
                use_container_width=True
            )

# message
if st.session_state.msg:
    st.success(st.session_state.msg)

# restart
if st.button("🔄 Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.msg = ""
    st.rerun()

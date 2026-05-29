import streamlit as st
import random

st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮", layout="centered")

# CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#4e54c8,#8f94fb);
}

h1 {
    text-align:center;
    color:white;
}

.sub {
    text-align:center;
    color:white;
    font-size:22px;
    margin-bottom:20px;
}

/* Game buttons */
div.stButton > button {
    height:90px;
    width:100%;
    font-size:35px;
    font-weight:bold;
    border-radius:15px;
    border:none;
    background-color:white;
    color:#222 !important;
    box-shadow:2px 2px 10px rgba(0,0,0,0.3);
}

div.stButton > button:hover {
    background:#dfe6ff;
}

/* Highlight message */
.msg {
    text-align:center;
    font-size:30px;
    font-weight:bold;
    padding:15px;
    border-radius:12px;
    margin-top:25px;
    margin-bottom:15px;
    color:white;
}

.win {
    background:#28a745;
}

.lose {
    background:#dc3545;
}

.draw {
    background:#ff9800;
}

</style>
""", unsafe_allow_html=True)

st.title("🎮 Tic Tac Toe")
st.markdown('<p class="sub">Play Against Computer 🤖</p>', unsafe_allow_html=True)

# board
if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "msg" not in st.session_state:
    st.session_state.msg = ""

if "type" not in st.session_state:
    st.session_state.type = ""

board = st.session_state.board

# winner check
def winner(player):
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
def computer_move():
    empty = []

    for i in range(9):
        if board[i] == "":
            empty.append(i)

    if empty:
        move = random.choice(empty)
        board[move] = "O"

# play move
def play(pos):

    if board[pos] == "" and st.session_state.msg == "":

        board[pos] = "X"

        if winner("X"):
            st.session_state.msg = "🎉 YOU WON!"
            st.session_state.type = "win"
            return

        if "" not in board:
            st.session_state.msg = "🤝 MATCH DRAW!"
            st.session_state.type = "draw"
            return

        computer_move()

        if winner("O"):
            st.session_state.msg = "😢 COMPUTER WON!"
            st.session_state.type = "lose"
            return

        if "" not in board:
            st.session_state.msg = "🤝 MATCH DRAW!"
            st.session_state.type = "draw"

# board UI
for r in range(3):
    cols = st.columns(3)

    for c in range(3):
        idx = r * 3 + c

        with cols[c]:
            st.button(
                board[idx] if board[idx] else " ",
                key=idx,
                on_click=play,
                args=(idx,),
                use_container_width=True
            )

# highlighted message
if st.session_state.msg:
    st.markdown(
        f'<div class="msg {st.session_state.type}">{st.session_state.msg}</div>',
        unsafe_allow_html=True
    )

# restart
if st.button("🔄 Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.msg = ""
    st.session_state.type = ""
    st.rerun()

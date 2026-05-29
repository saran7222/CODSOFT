import streamlit as st
import random

st.set_page_config(
    page_title="Tic Tac Toe",
    page_icon="🎮",
    layout="centered"
)

# CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#4e54c8,#8f94fb);
}

/* Title */
h1 {
    text-align:center;
    color:white;
}

.sub {
    text-align:center;
    color:white;
    font-size:22px;
    margin-bottom:25px;
}

/* Game Boxes */
div.stButton > button {
    height:95px;
    width:100%;
    border-radius:18px;
    border:none;
    background:white;
    font-size:42px;
    font-weight:900 !important;
    color:#111 !important;
    box-shadow:0px 4px 12px rgba(0,0,0,0.3);
    transition:0.3s;
}

div.stButton > button:hover {
    transform:scale(1.04);
    background:#e9ecff;
}

/* Result Message */
.msg {
    text-align:center;
    font-size:30px;
    font-weight:bold;
    padding:15px;
    border-radius:14px;
    margin-top:25px;
    margin-bottom:20px;
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

/* Restart Button */
.restart-btn button {
    background: linear-gradient(90deg,#ff416c,#ff4b2b) !important;
    color: white !important;
    font-size: 20px !important;
    font-weight: 800 !important;
    border: none !important;
    border-radius: 30px !important;
    padding: 10px 25px !important;
    height: 55px !important;
    width: 220px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    transition: 0.3s;
}

.restart-btn button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 18px rgba(0,0,0,0.4);
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🎮 Tic Tac Toe")
st.markdown(
    '<p class="sub">Play Against Computer 🤖</p>',
    unsafe_allow_html=True
)

# Session State
if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "msg" not in st.session_state:
    st.session_state.msg = ""

if "type" not in st.session_state:
    st.session_state.type = ""

board = st.session_state.board

# Winner Check
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

# Computer Move
def computer_move():

    empty = []

    for i in range(9):
        if board[i] == "":
            empty.append(i)

    if empty:
        move = random.choice(empty)
        board[move] = "O"

# Play Move
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

# Game Board
for r in range(3):

    cols = st.columns(3)

    for c in range(3):

        idx = r * 3 + c
        value = board[idx]

        if value == "X":
            text = "❌"
        elif value == "O":
            text = "⭕"
        else:
            text = " "

        with cols[c]:
            st.button(
                text,
                key=idx,
                on_click=play,
                args=(idx,),
                use_container_width=True
            )

# Result Message
if st.session_state.msg:
    st.markdown(
        f'<div class="msg {st.session_state.type}">{st.session_state.msg}</div>',
        unsafe_allow_html=True
    )

# Restart Button
st.markdown('<div class="restart-btn">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("🔄 Play Again"):
        st.session_state.board = [""] * 9
        st.session_state.msg = ""
        st.session_state.type = ""
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
import random

st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮", layout="centered")

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

/* Game buttons */
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

/* Result box */
.msg {
    text-align:center;
    font-size:30px;
    font-weight:bold;
    padding:15px;
    border-radius:12px;
    margin-top:25px;
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

/* Restart button */
.restart button {
    background:#ff4b4b !important;
    color:white !important;
    font-size:20px !important;
    font-weight:bold !important;
    border-radius:12px !important;
    height:50px !important;
}

</style>
""", unsafe_allow_html=True)

st.title("🎮 Tic Tac Toe")
st.markdown('<p class="sub">Play Against Computer 🤖</p>', unsafe_allow_html=True)

# session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "msg" not in st.session_state:
    st.session_state.msg = ""

if "type" not in st.session_state:
    st.session_state.type = ""

board = st.session_state.board

# winner
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

# play
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
        value = board[idx]

        # color for X and O
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

# result
if st.session_state.msg:
    st.markdown(
        f'<div class="msg {st.session_state.type}">{st.session_state.msg}</div>',
        unsafe_allow_html=True
    )

# restart
st.markdown('<div class="restart">', unsafe_allow_html=True)
if st.button("🔄 Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.msg = ""
    st.session_state.type = ""
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

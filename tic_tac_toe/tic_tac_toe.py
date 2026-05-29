import streamlit as st
import random

st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮")

# title
st.title("🎮 Tic Tac Toe Game")
st.write("Play against Computer")

# create board
if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "message" not in st.session_state:
    st.session_state.message = ""

board = st.session_state.board

# winner check
def check_winner(player):
    win = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for x in win:
        if board[x[0]] == player and board[x[1]] == player and board[x[2]] == player:
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

# click button
def play(pos):

    if board[pos] == "":

        board[pos] = "X"

        if check_winner("X"):
            st.session_state.message = "🎉 You Won!"
            return

        computer_move()

        if check_winner("O"):
            st.session_state.message = "😢 Computer Won!"
            return

        if "" not in board:
            st.session_state.message = "🤝 Match Draw"

# board UI
for row in range(3):
    cols = st.columns(3)

    for col in range(3):
        index = row * 3 + col

        with cols[col]:
            st.button(
                board[index] if board[index] else " ",
                key=index,
                on_click=play,
                args=(index,),
                use_container_width=True
            )

# message
if st.session_state.message:
    st.success(st.session_state.message)

# restart button
if st.button("🔄 Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.message = ""
    st.rerun()

import streamlit as st
import random

# create board
if "board" not in st.session_state:
    st.session_state.board = [" "] * 9

board = st.session_state.board

st.title("Tic Tac Toe")
st.write("You are X and Computer is O")

# show board
for i in range(0, 9, 3):
    st.write(board[i] + " | " + board[i+1] + " | " + board[i+2])

# winner check
def check(mark):
    win = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for x in win:
        if board[x[0]] == mark and board[x[1]] == mark and board[x[2]] == mark:
            return True
    return False

# user input
pos = st.number_input("Enter position (1-9)", 1, 9)

if st.button("Play"):

    pos = pos - 1

    if board[pos] == " ":
        board[pos] = "X"

        if check("X"):
            st.success("You Won!")

        else:
            empty = []

            for i in range(9):
                if board[i] == " ":
                    empty.append(i)

            if empty:
                comp = random.choice(empty)
                board[comp] = "O"

                if check("O"):
                    st.error("Computer Won!")

    else:
        st.warning("Position already filled")

    st.rerun()

import streamlit as st

def is_valid_group(nums):
    return sorted(nums) == list(range(1, 10))

def verify_sudoku(grid):
    for i in range(9):
        if not is_valid_group(grid[i]):
            return False, f"Invalid row {i+1}"

    for j in range(9):
        col = [grid[i][j] for i in range(9)]
        if not is_valid_group(col):
            return False, f"Invalid column {j+1}"

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = []
            for x in range(3):
                for y in range(3):
                    box.append(grid[i+x][j+y])
            if not is_valid_group(box):
                return False, f"Invalid 3x3 box at ({i+1},{j+1})"

    return True, "Valid Sudoku"

def parse_grid(text):
    lines = text.strip().split("\n")
    grid = []

    if len(lines) != 9:
        raise ValueError("Must have exactly 9 rows")

    for line in lines:
        row = list(map(int, line.strip().split()))
        if len(row) != 9:
            raise ValueError("Each row must have 9 numbers")
        grid.append(row)

    return grid

st.title("Sudoku LLM Answer Verifier")

st.write("Paste a 9x9 Sudoku solution below:")

user_input = st.text_area("Sudoku Grid", height=200)

if st.button("Verify"):
    try:
        grid = parse_grid(user_input)
        valid, message = verify_sudoku(grid)

        if valid:
            st.success("✔ " + message)
        else:
            st.error("✘ " + message)

    except Exception as e:
        st.warning(f"Input Error: {e}")

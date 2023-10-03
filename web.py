import streamlit as st
import functions
import os


# Creating todos.txt file for first time
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


todos = functions.get_todos()


def add_todo():
    # session_state looks like dictionary, it is not exactly dictionary type it is session_state type
    # it contains key and value associate with that key
    # st.session_state =
    # {
    #   "new_todo" : value,
    # }
    todo_ = st.session_state["new_todo"].strip().lower().title() + "\n"
    if todo_.isspace():
        pass
    else:
        todos.append(todo_)
        functions.write_todos(todos)

    st.session_state["new_todo"] = ''


# st.title() - to create title
st.title("My todo app ✔")

# st.write() - to create normal text
st.write("This app is to increase your productivity")

# st.checkbox("checkbox leve here") - to create checkbox
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    # if checkbox is True the do these things
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # delete this pair from the session_state
        del st.session_state[todo]
        # now rerun the program to update UI, this is needed for checkboxes
        st.rerun()


# st.text_input() - to create text input field
# on_change is a callback function to perform action
st.text_input(placeholder="Add new todo...", label="", on_change=add_todo, key="new_todo")


# st.session_state

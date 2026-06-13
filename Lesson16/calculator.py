import streamlit as st

def calculator(n1, n2, ope):
    if ope == 'Addition':
        result = n1 + n2
    elif ope == 'Subtraction':
        result = n1 - n2
    elif ope == 'Multiplication':
        result = n1 * n2
    elif ope == 'Division':
        try:
            result = n1 / n2
        except ZeroDivisionError:
            result = "Cannot divide by zero"

    return result

def main():
    st.title("Simple Calculator")

    n1 = st.number_input("Enter the first number", step=1)
    n2 = st.number_input("Enter the second number", step=1)

    ope = st.radio("Select Operation", ['Addition', 'Subtraction', 'Multiplication', 'Division'])
    result = calculator(n1, n2, ope)
    st.write(f"Result of the{ope} of {n1} and {n2} is: {result}")

    if __name__ == "__main__":
        main()

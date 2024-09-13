import streamlit as st


def main():
    st.title("Simple Calculator")

    # Input fields
    num1 = st.number_input("Enter the first number", value=0.0)
    num2 = st.number_input("Enter the second number", value=0.0)

    # Operation selection
    operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Perform calculation based on selected operation
    if operation == "Add":
        result = num1 + num2
        st.write(f"The result of {num1} + {num2} is {result}")

    elif operation == "Subtract":
        result = num1 - num2
        st.write(f"The result of {num1} - {num2} is {result}")

    elif operation == "Multiply":
        result = num1 * num2
        st.write(f"The result of {num1} * {num2} is {result}")

    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.write(f"The result of {num1} / {num2} is {result}")
        else:
            st.error("Error: Division by zero is not allowed!")


if __name__ == "__main__":
    main()

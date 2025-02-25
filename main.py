import streamlit as st
import random
import string

# Function to generate random password
def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase  # Always include lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit App
def main():
    st.title("🔐 Random Password Generator")

    # User selects password length
    length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

    # Checkbox options for user preference
    use_uppercase = st.checkbox("Include Uppercase Letters (A-Z)")
    use_numbers = st.checkbox("Include Numbers (0-9)")
    use_symbols = st.checkbox("Include Symbols (!@#$%^&*)")

    # Generate password button
    if st.button("🔑 Generate Password"):
        if not any([use_uppercase, use_numbers, use_symbols]):  
            st.warning("⚠ Please select at least one option (Uppercase, Numbers, or Symbols)!")
        else:
            password = generate_password(length, use_uppercase, use_numbers, use_symbols)
            st.success(f"**Your Password:** `{password}`")

            # Copy button
            st.code(password, language="plaintext")

if __name__ == "__main__":
    main()

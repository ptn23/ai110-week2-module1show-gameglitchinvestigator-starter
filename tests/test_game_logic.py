from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_attempts_initialized_zero():
    """Regression test: importing the app should initialize attempts to 0."""
    import importlib
    import sys
    import streamlit as st

    # Ensure a clean session and force app to reload
    st.session_state.clear()
    if "app" in sys.modules:
        del sys.modules["app"]

    importlib.import_module("app")

    assert "attempts" in st.session_state
    assert st.session_state.attempts == 0

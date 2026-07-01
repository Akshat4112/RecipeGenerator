"""Framework for running multiple Streamlit applications as a single app."""
import streamlit as st


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title: str, func) -> None:
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self) -> None:
        app = st.sidebar.selectbox(
            "Navigation",
            self.apps,
            format_func=lambda app: app["title"])
        app["function"]()

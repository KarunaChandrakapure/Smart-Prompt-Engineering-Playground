import streamlit as st
import pandas as pd
import yaml
from pathlib import Path
from llm import run_prompt

st.set_page_config(
    page_title="Smart Prompt Engineering Playground",
    layout="wide"
)

st.title("Smart Prompt Engineering Playground")

with open("prompts.yaml", "r") as f:
    prompts = yaml.safe_load(f)

if "results" not in st.session_state:
    st.session_state.results = []

user_input = st.text_area(
    "Enter customer message",
    "The product is useful, but onboarding took forever."
)

if st.button("Run all prompt strategies"):
    results = []

    for key, config in prompts.items():
        final_prompt = config["template"].format(input=user_input)

        with st.spinner(f"Running {config['name']}..."):
            result = run_prompt(final_prompt)

        results.append({
            "strategy": config["name"],
            "input": user_input,
            "output": result["output"],
            "latency": result["latency"],
            "score": 3,
        })

    st.session_state.results = results

if st.session_state.results:
    st.subheader("Rate Latest Results")

    for i, row in enumerate(st.session_state.results):
        with st.expander(row["strategy"], expanded=True):
            st.write(row["output"])
            st.caption(f"Latency: {row['latency']}s")

            score = st.slider(
                f"Rate {row['strategy']}",
                min_value=1,
                max_value=5,
                value=int(row["score"]),
                key=f"score_slider_{i}"
            )

            st.session_state.results[i]["score"] = score

    st.subheader("Current Results")
    current_df = pd.DataFrame(st.session_state.results)
    st.dataframe(current_df)

    if st.button("Save results"):
        Path("logs").mkdir(exist_ok=True)

        log_path = Path("logs/results.csv")
        new_df = pd.DataFrame(st.session_state.results)

        if log_path.exists():
            old_df = pd.read_csv(log_path)
            final_df = pd.concat([old_df, new_df], ignore_index=True)
        else:
            final_df = new_df

        final_df.to_csv(log_path, index=False)

        st.success("Results saved successfully")
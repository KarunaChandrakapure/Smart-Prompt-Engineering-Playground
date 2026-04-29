import streamlit as st
import pandas as pd
import yaml
from pathlib import Path
from llm import run_prompt

st.set_page_config(page_title="Smart Prompt Engineering Playground",layout='wide')
st.title("Smart Prompt Engineering Playground")

with open('prompts.yaml','r') as f:
    prompts = yaml.safe_load(f)

user_input = st.text_area(
    "enter customer message",
    "The product is useful, but onboarding took forever. "
)   

if st.button("Run all prompt strategies"):
    results = []

    cols = st.columns(len(prompts))

    for col ,(key,config) in zip(cols,prompts.items()):
        final_prompt = config["template"].format(input=user_input)

        with col:
            st.subheader(config["name"])
            with st.spinner("Running .........."):
                result = run_prompt(final_prompt)

            st.write(result["output"])    
            st.caption(f"Latency:{result['latency']}s")
            score = st.slider(
                f"Rate {config['name']}",
                1,
                5,
                3,
                key=f'score_{key}'
            )
            results.append({
                "strategy":config['name'],
                "input":user_input,
                "output":result['output'],
                "latency":result['latency'],
                "score":score,
            })
    if st.button("save results"):
        Path("logs").mkdir(exist_ok=True)
        df = pd.DataFrame(results)

        log_path = Path("logs/results.csv")
        if log_path.exists():
            old=pd.read_csv(log_path)
            df =pd.concat([old,df],ignore_index=True)
        df.to_csv(log_path,index=False)    
        st.success("Results saved")

log_path=Path("logs/results.csv")  
if log_path.exists():
    st.header("Prompt Strategy Performance") 
    df = pd.read_csv(log_path)    
    summary=df.groupby("strategy")["score"].mean().sort_values(ascending=False)
    st.bar_chart(summary)
    st.dataframe(df)
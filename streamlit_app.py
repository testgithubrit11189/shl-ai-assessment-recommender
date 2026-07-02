import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="SHL Assessment Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 SHL Assessment Recommendation Assistant")

st.markdown(
    "Describe the role you are hiring for and I'll recommend suitable SHL assessments."
)

if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

        if "recommendations" in msg:

            for rec in msg["recommendations"]:

                st.markdown(
                    f"""
### {rec['name']}

{rec['description']}

🔗 {rec['url']}

---
"""
                )


prompt = st.chat_input("Type your hiring requirement...")


if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    payload = {
        "messages": st.session_state.messages
    }

    response = requests.post(
        API_URL,
        json=payload
    )

    data = response.json()

    assistant_message = {
        "role": "assistant",
        "content": data["reply"],
        "recommendations": data["recommendations"]
    }

    st.session_state.messages.append(
        assistant_message
    )

    with st.chat_message("assistant"):

        st.markdown(data["reply"])

        if len(data["recommendations"]) > 0:

            st.subheader("Recommended Assessments")

            for rec in data["recommendations"]:

                with st.container():

                    st.markdown(f"### {rec['name']}")

                    st.write(rec["description"])

                    st.link_button(
                        "Open SHL Assessment",
                        rec["url"]
                    )

                    st.divider()
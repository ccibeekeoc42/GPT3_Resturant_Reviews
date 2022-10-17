import streamlit as st
import openai

openai.api_key = "KEY GOES HERE!!!"

st.header("GPT-3 Resturnat Review Replier")
review = st.text_area("Enter Customer Review")
button = st.button("Generate Reply")


def generate_reply(review):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"""Write a reply to the given review. If the customer has any concerns, 
    address them.\n\nReview: {review}\n\nReply:""",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # st.write(response)
    return response.choices[0].text


if button and review:
    with st.spinner("Generating Reply..."):
        reply = generate_reply(review)
    st.write(reply)

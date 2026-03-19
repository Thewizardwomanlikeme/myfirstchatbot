
import streamlit as st
from groq import Groq

# Must be the first Streamlit command
st.set_page_config(
    page_title="Thrupthi - Mental Wellness",
    page_icon="🧘‍♂️",
    layout="centered"
)

page_bg = """
<style>
.stApp {
    background-image: url("https://i.pinimg.com/1200x/c0/ca/56/c0ca561dd91597af2ac2e5f4ba5f48b8.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* frosted glass container for headers */
.glass-box {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: #1E3A8A;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.glass-box h1 {
    color: #1e3a8a;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.glass-box h4 {
    color: #3b82f6;
    font-weight: 500;
    line-height: 1.5;
}

/* Customizing the chat messages to stand out against the background */
[data-testid="stChatMessage"] {
    background: rgba(255, 255, 255, 0.65);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border-radius: 15px;
    padding: 10px 15px;
    margin-bottom: 10px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

[data-testid="stChatMessage"] p {
    color: #1e293b;
    font-size: 16px;
}

/* Make chat input more visible */
[data-testid="stChatInput"] {
    background: rgba(255, 255, 255, 0.85) !important;
    border-radius: 15px !important;
    backdrop-filter: blur(8px) !important;
}

/* Adjust colors for markdown specifically inside chat messages */
[data-testid="stMarkdownContainer"] p {
    color: #0f172a;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.markdown("""
<div class="glass-box">
    <h1>ⲯ﹍ⲯ﹍ Thrupthi ⲯ﹍ⲯ﹍</h1>
    <h4>
    A mental wellness companion built for you.<br>
    <span style="font-size: 16px; color: #1e293b;">She speaks Romanized Kannada & English, offering emotional support, practical advice, and a warm presence for whatever is on your mind.</span>
    </h4>
</div>
""", unsafe_allow_html=True)

# API Keys setup
try:
    groq_key = st.secrets["GROQ_API_KEY"]
except Exception as e:
    st.error("Missing API configurations in secrets.")
    st.stop()

client = Groq(api_key=groq_key)

SYSTEM_PROMPT = (
"You are Thrupthi, a mental wellness chatbot. "
        "Speak in Romanized Kannada if the user speaks in romanized kannada. "
            "Be warm, friendly, emotionally intelligent with conversational tone (not formal). "
            "Keep responses short (3-6 lines) with emojis like 💛 😊 💔 😂 🌸. "
            "Always end with warm follow-up in Kannada. Use Kannada spellings: mada, yenu, nanage, nanna, nagu, niru, irodu, bittuhodre, obbanti. "
            "Use English only for emotional words: confuse, capable, weak, relax, breathe, focus."
            "MOOD DETECTION: For breakup/heartbreak - acknowledge pain, validate, give 3-4 actionable steps. "
            "For loneliness - validate, suggest hobby/walk/journaling, remind they are special. For stress/overthinking - calm tone, practical steps, reassure they are capable. "
            "For sadness - offer grounding activities, encourage small achievements. "
            "For anger - validate, suggest calming techniques. For humor - match energy with fun. "
            "For happiness - celebrate together. For low confidence - reassure, suggest small wins. "
            "For missing ex - validate memories, support healing. If self-harm mentioned - respond calmly, encourage talking to trusted people. "
            "Use follow-ups like yake yenaithu, hegiddira, ninna dina hegittu. Be authentic, emotionally aware, and supportive."
            "Breakup or Heartbreak Mood Detect phrases like “gf/bf cheat madidlu”, “bittuhodlu”, “love fail”, “heart break”."
            "Respond with care, understanding, and short actionable steps to handle the emotion."
            "Example:"
            "User: nanna girlfriend nanna cheat madidlu, avalanna sais bekantha annasthaide"
            "Response:"
            "ninna manassu odeda hage anstide 💔 swalpa breathe maaDu, calm aagona. Avalu bittuhodre, adu ninna tappu alla — nanage nanna gf bittuhodre yenu sukha kodutte? anta kelkobedi. Friends jothe irodu, nagu barutte 😊 Naanu nimmondige iddene 💛"

            "Loneliness / Feeling Isolated"

            "Detect “obbane anstide”, “yaaru illa”, “no one understands”."

            "Respond gently and remind user they are not alone."

            "Example:"  

            "User: nanu obbane anstide"

            "Response:"
            "Ayy obbanti anstirodu normal 💔 ninna mind busy itkolu, journaling try maaDu. Neevu special, neevu illa andre bere yaaru? 🌼"

            "Stress / Overthinking"

            "Detect “stress aagide”, “overthink madta idini”, “tension ide”."

            "Give calm, doable actions instead of generic advice."

            "Example:"

            "User: nanage stress aagide, ellaru nanna mele pressure haakidare"

            "Response:"
            "swalpa relax maaDu 🌸 ninna efforts already super ide. 3 simple steps try maaDu — 1. Deep breathe, 2. 5 nimisha walk, 3. Ninna mind calm madoke ninna favourite haadu kelri 🎶. Ella sari aagutte 💛"

            "Sadness / Low Mood"

            "Detect “sad ide”, “feel madta idini”, “nanage yenu artha aagalla”."

            "Offer small grounding steps."

            "Example:"

            "User: nanage ivathu tumba sad aagide"

            "Response:"
            "Ayy 💔 sad aagiradu okay. Swalpa fresh air tago, ninna favourite haadu kelri, at least 10 nimisha ninna manassige time kodi. Santosh barutte 💛"

            "Anger"

            "Detect “sittu bandide”, “gussa aagide”."

            "Calm tone + practical ways to let go." 

            "Example:"

            "User: nange bahala sittu bandaga nanu yenu madbeku?"

            "Response:"
            "sittu barodu normal 🔥 aadre calm aagona. 1. Swalpa nishabdha irri, 2. Ninna thoughts baraduko, 3. Ninna mind divert madoke haadu kelri. Calm aagidmele matadri 💛"

            "Funny / Light Mood"

            "Detect jokes or laughing tone (“😂”, “haha”, “madbeku anta”, etc.)."

            "Respond with humor and lightness."

            "Example:"

            "User: nanna friend nanna pizza thindlu 😂"

            "Response:"
            "😂 Ayyo adu serious crime ide! Next time double cheese order maadu anta helri 🍕😄"

            "Happy / Excited Mood"

            "Detect joy or excitement (“santosha”, “haagide”, “party”, etc.)"

            "Match the users energy."

            "Example:"

            "User: ivattu nanna birthday 🎉"

            "Response:"
            "Wow 🎂 Huttida dina shubhashayagalu 💛 ivattu full enjoy maaDu, ninna smile world ge beku 😊"

            " Sensitive / Safety Situations"

            "If user mentions self-harm, harm to others, or feeling unsafe:"

            "Never repeat violent phrases."

            "Respond calmly and safely."

            "Encourage the user to stay safe and talk to someone trustworthy."

            "Example safe structure:"
            "ninna manassu hurt aagide anta gottu 💔 swalpa calm aagona, decisions madoke time togolli. "
            "Trusted friend athava family jothe maatadi. Nanage gottu neevu strong idira 💛"
    )



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add a welcoming initial message
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Namaskara! Naanu Thrupthi. Hegiddira ivattu? Nanna jothe yenu anstide anta hanchikolli 🌸"
    })

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Nanna jothe matanadbeku anstide? (Type your message here...)"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Prepare messages for API
    api_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    # Append conversation history (keeping recent context)
    for msg in st.session_state.messages[-10:]:
        api_messages.append({"role": msg["role"], "content": msg["content"]})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=api_messages
            )
            full_response = response.choices[0].message.content
            message_placeholder.markdown(full_response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Ondu chikka samasye aagide (Error): {str(e)}")


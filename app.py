import streamlit as st

st.set_page_config(
    page_title="Conscia",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Conscia")
st.subheader("Emotional Sustainability Intelligence")

st.write(
    "Understand how emotions influence consumption, waste, and sustainability behavior."
)

st.divider()

mood = st.slider("Mood Level", 1, 10, 5)

stress = st.slider("Stress Level", 1, 10, 5)

purchases = st.number_input(
    "Impulse Purchases Today",
    min_value=0,
    max_value=20,
    value=0
)

food_waste = st.number_input(
    "Food Waste Instances Today",
    min_value=0,
    max_value=10,
    value=0
)

if st.button("Analyze Behavior"):

    st.divider()

    if stress > 7 and purchases > 3:
        st.warning(
            "⚠️ Stress-driven consumption pattern detected."
        )

    elif mood < 4 and food_waste > 2:
        st.error(
            "⚠️ Emotional low mood may be increasing waste behavior."
        )

    else:
        st.success(
            "✅ No major unsustainable emotional patterns detected."
        )

    st.subheader("🌍 Sustainability Insight")

    sustainability_score = 100 - (purchases * 5) - (food_waste * 8)

    sustainability_score = max(0, sustainability_score)

    st.metric(
        label="Sustainability Behavior Score",
        value=f"{sustainability_score}/100"
    )

    st.write(
        "Your emotional state can influence environmental impact through behavioral patterns."
    )

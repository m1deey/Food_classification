import streamlit as st


pipe = joblib.load('personality_pipeline.joblib')

cols = ['E1','E2','E5','E7','N1','N2','N3','N8',
        'A1','A2','A4','A9','C1','C2','C3','C5',
        'O1','O2','O3','O5']
reverse_cols = ['E2','N2','A1','C2','O2']
cluster_names = {
    0: "The Chaotic Social Butterfly",
    1: "The Ghost",
    2: "The Overthinking Softie",
    3: "The Main Character"
}

questions = {
    'E1': "I am the life of the party.",
    'E2': "I don't talk a lot.",
    'E5': "I start conversations.",
    'E7': "I talk to a lot of different people at parties.",
    'N1': "I get stressed out easily.",
    'N2': "I am relaxed most of the time.",
    'N3': "I get upset easily.",
    'N8': "I have frequent mood swings.",
    'A1': "I feel little concern for others.",
    'A2': "I am interested in people.",
    'A4': "I sympathize with others' feelings.",
    'A9': "I feel others' emotions.",
    'C1': "I am always prepared.",
    'C2': "I leave my belongings around.",
    'C3': "I pay attention to details.",
    'C5': "I get chores done right away.",
    'O1': "I have a rich vocabulary.",
    'O2': "I have difficulty understanding abstract ideas.",
    'O3': "I have a vivid imagination.",
    'O5': "I have excellent ideas."
}

st.title("What's Your Type?")
answers = {}
for col, text in questions.items():
    answers[col] = st.slider(text, 1, 5, 3)

if st.button("Reveal my type"):
    for col in reverse_cols:
        answers[col] = 6 - answers[col]
    row = pd.DataFrame([answers])[cols]
    pred = pipe.predict(row)[0]
    st.write(f"You are: **{cluster_names[pred]}**")

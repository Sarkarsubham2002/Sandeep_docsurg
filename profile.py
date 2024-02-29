import streamlit as st

def main():
    st.title("Doctor's Profile Page")

    # Doctor's information
    doctor_name = "Dr. John Smith"
    specialization = "Cardiologist"
    description = "Dr. John Smith is a highly experienced cardiologist with over 15 years of experience. He has a passion for helping patients lead heart-healthy lives and specializes in advanced cardiac interventions."

    st.header(doctor_name)
    st.subheader(specialization)
    st.write(description)

    # Interactive image
    # st.image("doctor_image.jpg", use_column_width=True, caption="Dr. John Smith")

if __name__ == "__main__":
    main()

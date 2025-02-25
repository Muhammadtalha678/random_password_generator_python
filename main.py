import streamlit as st
import pandas as pd

def main():
    st.title(" Customizable Class Grade Calculator 🎓")

    # Take input of class name
    class_name = st.text_input(" **Class Name**")

    if class_name:
        st.subheader(f" **{class_name}**")

        # Take the class subjects
        class_subjects = st.text_area(
            "📖 **Enter the Class Subjects (Comma Separated)**",
            placeholder="Math, English, Physics"
        )

        if class_subjects:
            # Convert the subjects into a list
            subjects_list = [s.strip() for s in class_subjects.split(",") if s.strip()]

            # Take input for number of students
            number_of_students = st.number_input(
                "**Number of Students in Class**",
                min_value=1,
                step=1
            )

            student_data = []  # Store students' data

            if number_of_students >= 1:
                for i in range(number_of_students):
                    student_info = {}
                    student_name = st.text_input(f" **Student {i+1} Name**", key=f"name_{i}")
                    student_info["Student Name"] = student_name

                    total_obtained = 0  # Track total obtained marks
                    total_marks = len(subjects_list) * 100  # Each subject is out of 100

                    for subject in subjects_list:
                        marks = st.number_input(f"📘 **{subject} Marks**", key=f"{i}_{subject}", min_value=0, max_value=100)
                        student_info[subject] = marks
                        total_obtained += marks  # Sum up marks

                    # Calculate percentage
                    percentage = (total_obtained / total_marks) * 100
                    student_info["Percentage"] = round(percentage, 2)  # Round to 2 decimal places

                    student_data.append(student_info)

            # 🔥 Button to Generate CSV File
            if st.button("Generate CSV Report"):
                if student_data:
                    df_students = pd.DataFrame(student_data)  # Convert list to DataFrame

                    #  Create a proper CSV format with Class Name as heading
                    csv_header = f"Class Name:, {class_name}\n"  # Class name at the top
                    csv_body = df_students.to_csv(index=False)  # Convert student data to CSV format
                    final_csv = csv_header + csv_body  # Merge both parts

                    # Show DataFrame in UI
                    st.dataframe(df_students)

                    # Download Button
                    st.download_button(
                        label=" Download CSV File",
                        data=final_csv.encode('utf-8'),
                        file_name=f"{class_name}_grades.csv",
                        mime="text/csv"
                    )
                else:
                    st.error("Please enter student names and marks before generating the CSV.")

if __name__ == "__main__":
    main()

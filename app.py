
---

# **app.py**  

**Copy and paste this entire code** into `app.py`:  

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load data
df = pd.read_csv("Synthetic_health_lifestyle_dataset.csv")

st.set_page_config(page_title="Health & Lifestyle Dashboard", layout="wide")

st.title("🩺 Synthetic Health Lifestyle Dashboard")
st.markdown("""
This interactive dashboard helps HR Directors and stakeholders explore chronic disease risk factors
based on synthetic health and lifestyle data. Use filters on the left to drill down insights.
""")

# Sidebar filters
st.sidebar.header("Apply Filters")
age_slider = st.sidebar.slider("Age Range", int(df['Age'].min()), int(df['Age'].max()), (20,60))
gender_options = st.sidebar.multiselect("Gender", options=df['Gender'].unique(), default=list(df['Gender'].unique()))
smoking_options = st.sidebar.multiselect("Smoking Status", options=df['Smoking'].unique(), default=list(df['Smoking'].unique()))

# Filter
filtered_df = df[
    (df['Age'] >= age_slider[0]) &
    (df['Age'] <= age_slider[1]) &
    (df['Gender'].isin(gender_options)) &
    (df['Smoking'].isin(smoking_options))
]

# Preview
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df.head(20))

# 1. Chronic Disease Distribution
st.subheader("Chronic Disease Distribution")
st.markdown("This pie chart shows how many individuals are affected by chronic disease.")
chronic_counts = filtered_df['Chronic_Disease'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(chronic_counts, labels=chronic_counts.index, autopct='%1.1f%%', startangle=90)
st.pyplot(fig1)

# 2. Age distribution
st.subheader("Age Distribution")
st.markdown("This histogram shows the age spread of individuals in the filtered dataset.")
st.hist(filtered_df['Age'], bins=30)

# 3. Gender distribution
st.subheader("Gender Distribution")
st.markdown("Displays the gender breakdown among the filtered data.")
st.bar_chart(filtered_df['Gender'].value_counts())

# 4. BMI vs Chronic Disease
st.subheader("BMI by Chronic Disease")
st.markdown("Boxplot of BMI across chronic disease categories.")
fig2 = px.box(filtered_df, x="Chronic_Disease", y="BMI")
st.plotly_chart(fig2)

# 5. Alcohol Consumption vs Chronic Disease
st.subheader("Alcohol Consumption vs Chronic Disease")
st.markdown("Boxplot showing alcohol intake based on chronic disease status.")
fig3 = px.box(filtered_df, x="Chronic_Disease", y="Alcohol Consumption")
st.plotly_chart(fig3)

# 6. Smoking vs Chronic Disease
st.subheader("Smoking vs Chronic Disease")
st.markdown("Bar chart of smoking status by chronic disease.")
smoke_ct = pd.crosstab(filtered_df['Smoking'], filtered_df['Chronic_Disease'])
st.bar_chart(smoke_ct)

# 7. Physical Activity
st.subheader("Physical Activity")
st.markdown("Histogram of physical activity scores in filtered data.")
st.hist(filtered_df['Physical Activity'], bins=30)

# 8. Sleep Hours
st.subheader("Sleep Hours Distribution")
st.markdown("How much people sleep in hours.")
st.hist(filtered_df['Sleep Hours'], bins=30)

# 9. Steps vs BMI
st.subheader("Steps per Day vs BMI")
st.markdown("Scatter plot of daily steps vs BMI colored by chronic disease.")
fig4 = px.scatter(filtered_df, x="Steps per Day", y="BMI", color="Chronic_Disease")
st.plotly_chart(fig4)

# 10. Correlation Heatmap
st.subheader("Correlation Heatmap")
st.markdown("Heatmap showing relationships between numeric variables.")
fig5, ax5 = plt.subplots(figsize=(10,6))
sns.heatmap(filtered_df.corr(), annot=True, cmap="coolwarm")
st.pyplot(fig5)

# 11. Alcohol by Gender
st.subheader("Average Alcohol Consumption by Gender")
st.markdown("Mean alcohol consumption split by gender.")
avg_alcohol = filtered_df.groupby("Gender")["Alcohol Consumption"].mean()
st.bar_chart(avg_alcohol)

# 12. Steps per Day
st.subheader("Steps per Day Distribution")
st.markdown("How many steps people take each day.")
st.hist(filtered_df['Steps per Day'], bins=30)

# 13. Average Sleep by Gender
st.subheader("Average Sleep Hours by Gender")
st.markdown("Shows how sleep hours differ between genders.")
avg_sleep = filtered_df.groupby("Gender")["Sleep Hours"].mean()
st.bar_chart(avg_sleep)

# 14. Age vs Sleep Hours
st.subheader("Age vs Sleep Hours")
st.markdown("Scatter showing relation between age and sleep hours.")
fig6 = px.scatter(filtered_df, x="Age", y="Sleep Hours", color="Gender")
st.plotly_chart(fig6)

# 15. BMI by Gender
st.subheader("BMI by Gender")
st.markdown("Boxplot showing BMI split by gender.")
fig7 = px.box(filtered_df, x="Gender", y="BMI")
st.plotly_chart(fig7)

# 16. Alcohol vs Age
st.subheader("Alcohol Consumption vs Age")
st.markdown("Scatter plot of alcohol consumption with age.")
fig8 = px.scatter(filtered_df, x="Age", y="Alcohol Consumption", color="Chronic_Disease")
st.plotly_chart(fig8)

# 17. Physical Activity by Chronic Disease
st.subheader("Physical Activity vs Chronic Disease")
st.markdown("Physical activity scores across chronic disease statuses.")
fig9 = px.box(filtered_df, x="Chronic_Disease", y="Physical Activity")
st.plotly_chart(fig9)

# 18. Smoking Pie Chart
st.subheader("Smoking Distribution")
st.markdown("Pie chart of smoking status proportions.")
smoke_counts = filtered_df['Smoking'].value_counts()
fig10, ax10 = plt.subplots()
ax10.pie(smoke_counts, labels=smoke_counts.index, autopct='%1.1f%%')
st.pyplot(fig10)

# 19. Steps by Chronic Disease
st.subheader("Steps per Day by Chronic Disease")
st.markdown("Boxplot comparing daily steps across chronic disease statuses.")
fig11 = px.box(filtered_df, x="Chronic_Disease", y="Steps per Day")
st.plotly_chart(fig11)

# 20. Alcohol vs Smoking
st.subheader("Alcohol Consumption by Smoking Status")
st.markdown("Boxplot of alcohol consumption grouped by smoking.")
fig12 = px.box(filtered_df, x="Smoking", y="Alcohol Consumption")
st.plotly_chart(fig12)

st.success("✅ Dashboard loaded! Explore more with filters on the left.")

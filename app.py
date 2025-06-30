import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load data
df = pd.read_csv("Synthetic_health_lifestyle_dataset.csv")

st.set_page_config(page_title="Health & Lifestyle Dashboard", layout="wide")

st.title("🩺 Synthetic Health Lifestyle Dashboard")
st.markdown(
    "This interactive dashboard helps HR Directors and stakeholders explore chronic disease risk factors "
    "based on synthetic health and lifestyle data. Use filters on the left to drill down for insights."
)

# Sidebar filters
st.sidebar.header("Apply Filters")
age_slider = st.sidebar.slider(
    "Age Range",
    int(df['Age'].min()),
    int(df['Age'].max()),
    (20, 60)
)
gender_options = st.sidebar.multiselect(
    "Gender",
    options=df['Gender'].unique(),
    default=list(df['Gender'].unique())
)
smoking_options = st.sidebar.multiselect(
    "Smoking Status",
    options=df['Smoking'].unique(),
    default=list(df['Smoking'].unique())
)

# Apply filters
filtered_df = df[
    (df['Age'] >= age_slider[0]) &
    (df['Age'] <= age_slider[1]) &
    (df['Gender'].isin(gender_options)) &
    (df['Smoking'].isin(smoking_options))
]

# Preview data
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df.head(20))

# 1. Chronic Disease Distribution
st.subheader("Chronic Disease Distribution")
st.markdown("This pie chart shows the proportion of individuals affected vs. not affected by chronic disease.")
chronic_counts = filtered_df['Chronic_Disease'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(chronic_counts, labels=chronic_counts.index, autopct='%1.1f%%', startangle=90)
st.pyplot(fig1)

# 2. Age distribution
st.subheader("Age Distribution")
st.markdown("Shows how ages are distributed among filtered individuals.")
fig2, ax2 = plt.subplots()
ax2.hist(filtered_df['Age'], bins=30, color="skyblue", edgecolor="black")
st.pyplot(fig2)

# 3. Gender distribution
st.subheader("Gender Distribution")
st.markdown("Displays the gender breakdown in the filtered data.")
st.bar_chart(filtered_df['Gender'].value_counts())

# 4. BMI vs Chronic Disease
st.subheader("BMI by Chronic Disease")
st.markdown("Boxplot showing BMI across chronic disease groups.")
fig3 = px.box(filtered_df, x="Chronic_Disease", y="BMI")
st.plotly_chart(fig3)

# 5. Alcohol Consumption vs Chronic Disease
st.subheader("Alcohol Consumption by Chronic Disease")
st.markdown("Boxplot showing differences in alcohol consumption between disease groups.")
fig4 = px.box(filtered_df, x="Chronic_Disease", y="Alcohol Consumption")
st.plotly_chart(fig4)

# 6. Smoking vs Chronic Disease
st.subheader("Smoking Status vs Chronic Disease")
st.markdown("Bar chart comparing smoking categories by chronic disease status.")
smoke_ct = pd.crosstab(filtered_df['Smoking'], filtered_df['Chronic_Disease'])
st.bar_chart(smoke_ct)

# 7. Physical Activity
st.subheader("Physical Activity")
st.markdown("Histogram of physical activity scores.")
fig5, ax5 = plt.subplots()
ax5.hist(filtered_df['Physical Activity'], bins=30, color="lightgreen", edgecolor="black")
st.pyplot(fig5)

# 8. Sleep Hours
st.subheader("Sleep Hours Distribution")
st.markdown("Distribution of sleep hours in the filtered data.")
fig6, ax6 = plt.subplots()
ax6.hist(filtered_df['Sleep Hours'], bins=30, color="salmon", edgecolor="black")
st.pyplot(fig6)

# 9. Steps per Day vs BMI
st.subheader("Steps per Day vs BMI")
st.markdown("Scatter plot of daily steps vs BMI, colored by chronic disease status.")
fig7 = px.scatter(filtered_df, x="Steps per Day", y="BMI", color="Chronic_Disease")
st.plotly_chart(fig7)

# 10. Correlation Heatmap
st.subheader("Correlation Heatmap")
st.markdown("Visualizing relationships between numeric features.")
fig8, ax8 = plt.subplots(figsize=(10, 6))
sns.heatmap(filtered_df.corr(), annot=True, cmap="coolwarm", ax=ax8)
st.pyplot(fig8)

# 11. Average Alcohol by Gender
st.subheader("Average Alcohol Consumption by Gender")
st.markdown("Bar chart of mean alcohol consumption by gender.")
avg_alcohol = filtered_df.groupby("Gender")["Alcohol Consumption"].mean()
st.bar_chart(avg_alcohol)

# 12. Steps per Day
st.subheader("Steps per Day Distribution")
st.markdown("Histogram of daily step counts.")
fig9, ax9 = plt.subplots()
ax9.hist(filtered_df['Steps per Day'], bins=30, color="violet", edgecolor="black")
st.pyplot(fig9)

# 13. Average Sleep by Gender
st.subheader("Average Sleep Hours by Gender")
st.markdown("Shows how average sleep differs across genders.")
avg_sleep = filtered_df.groupby("Gender")["Sleep Hours"].mean()
st.bar_chart(avg_sleep)

# 14. Age vs Sleep Hours
st.subheader("Age vs Sleep Hours")
st.markdown("Scatter plot of age vs sleep hours colored by gender.")
fig10 = px.scatter(filtered_df, x="Age", y="Sleep Hours", color="Gender")
st.plotly_chart(fig10)

# 15. BMI by Gender
st.subheader("BMI by Gender")
st.markdown("Boxplot of BMI across genders.")
fig11 = px.box(filtered_df, x="Gender", y="BMI")
st.plotly_chart(fig11)

# 16. Alcohol Consumption vs Age
st.subheader("Alcohol Consumption vs Age")
st.markdown("Scatter plot of alcohol intake with respect to age.")
fig12 = px.scatter(filtered_df, x="Age", y="Alcohol Consumption", color="Chronic_Disease")
st.plotly_chart(fig12)

# 17. Physical Activity by Chronic Disease
st.subheader("Physical Activity by Chronic Disease")
st.markdown("Boxplot showing physical activity across chronic disease status.")
fig13 = px.box(filtered_df, x="Chronic_Disease", y="Physical Activity")
st.plotly_chart(fig13)

# 18. Smoking Pie Chart
st.subheader("Smoking Status Distribution")
st.markdown("Pie chart of smoking status proportions.")
smoke_counts = filtered_df['Smoking'].value_counts()
fig14, ax14 = plt.subplots()
ax14.pie(smoke_counts, labels=smoke_counts.index, autopct='%1.1f%%')
st.pyplot(fig14)

# 19. Steps by Chronic Disease
st.subheader("Steps per Day by Chronic Disease")
st.markdown("Boxplot of daily steps across chronic disease groups.")
fig15 = px.box(filtered_df, x="Chronic_Disease", y="Steps per Day")
st.plotly_chart(fig15)

# 20. Alcohol Consumption by Smoking
st.subheader("Alcohol Consumption by Smoking Status")
st.markdown("Boxplot of alcohol consumption based on smoking status.")
fig16 = px.box(filtered_df, x="Smoking", y="Alcohol Consumption")
st.plotly_chart(fig16)

st.success("✅ Dashboard loaded successfully! Use the filters on the left to explore more insights.")

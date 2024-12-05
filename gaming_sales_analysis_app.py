pip install matplotlib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the Streamlit page
st.title("Gaming Sales and Reviews Analysis")
st.markdown("An interactive dashboard for exploring video game sales and user reviews data.")

# Upload files
st.sidebar.header("Upload Data Files")
reviews_file = st.sidebar.file_uploader("Upload Reviews CSV", type=["csv"])
sales_file = st.sidebar.file_uploader("Upload Sales CSV", type=["csv"])

if reviews_file and sales_file:
    # Load the datasets
    reviews_df = pd.read_csv(reviews_file)
    sales_df = pd.read_csv(sales_file)

    # Clean the datasets
    reviews_df.columns = reviews_df.columns.str.strip()
    reviews_df.dropna(inplace=True)
    reviews_df.drop_duplicates(inplace=True)
    sales_df.columns = sales_df.columns.str.strip()
    sales_df.dropna(inplace=True)
    sales_df.drop_duplicates(inplace=True)

    # Merge datasets
    merged_df = pd.merge(
        reviews_df,
        sales_df,
        left_on=["Game_Title", "Release_Year"],
        right_on=["Name", "Year"],
        how="inner"
    )
    filtered_df = merged_df[merged_df["Year"] > 2015]

    st.success("Data loaded and filtered successfully!")
    st.write("Filtered DataFrame:", filtered_df.head())

    # Sidebar options for EDA
    st.sidebar.header("Visualization Options")
    eda_option = st.sidebar.selectbox(
        "Select a Visualization",
        ["User Rating Distribution", "Sales by Genre", "Correlation Heatmap", "Popular Platforms"]
    )

    # User Rating Distribution
    if eda_option == "User Rating Distribution":
        st.subheader("Distribution of User Ratings")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.histplot(filtered_df["User_Rating"], kde=True, bins=20, color="blue", ax=ax)
        ax.set_title("Distribution of User Ratings")
        ax.set_xlabel("User Rating")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    # Sales by Genre
    elif eda_option == "Sales by Genre":
        st.subheader("Sales by Genre")
        sales_by_genre = filtered_df.groupby("Genre_x")[
            ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
        ].sum()
        fig, ax = plt.subplots(figsize=(10, 6))
        sales_by_genre.plot(kind="bar", stacked=True, ax=ax)
        ax.set_title("Sales by Genre")
        ax.set_xlabel("Genre")
        ax.set_ylabel("Sales (in millions)")
        st.pyplot(fig)

    # Correlation Heatmap
    elif eda_option == "Correlation Heatmap":
        st.subheader("Correlation Heatmap")
        numeric_df = filtered_df.select_dtypes(include=["number"])
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        ax.set_title("Correlation Heatmap")
        st.pyplot(fig)

    # Popular Platforms
    elif eda_option == "Popular Platforms":
        st.subheader("Popular Platforms")
        platform_popularity = filtered_df["Platform_x"].value_counts()
        fig, ax = plt.subplots(figsize=(8, 6))
        platform_popularity.plot(kind="pie", autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"), ax=ax)
        ax.set_title("Popular Platforms")
        ax.set_ylabel("")
        st.pyplot(fig)

    # Save filtered data option
    st.sidebar.header("Save Filtered Data")
    if st.sidebar.button("Download Filtered CSV"):
        filtered_df.to_csv("filtered_data.csv", index=False)
        st.sidebar.success("Filtered data saved as filtered_data.csv")
else:
    st.warning("Please upload both Reviews and Sales CSV files to proceed.")

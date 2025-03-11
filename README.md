# ⚽ Football Transfer Market Analysis & Player Value Prediction  

## 📌 Introduction  
This project aims to analyze the **football transfer market** across multiple teams and leagues for **two seasons (2021-2022 and 2022-2023)**. By exploring **player performances, market value fluctuations, transfer trends, and injury impacts**, we gain insights into how player valuations evolve over time.  

### The project consists of two main components:  
1️⃣ **A global transfer market analysis** that examines **player valuations, transfer trends, and the impact of injuries on market value**. Additionally, a **predictive model** is built to estimate **player market values** based on various attributes such as **age, position, match performance, injury history, and past transfers**.  
2️⃣ **An interactive Streamlit dashboard for Real Madrid** that focuses specifically on **visualizing and analyzing the performance, transfers, and market value trends of Real Madrid players**.  

Through **Exploratory Data Analysis (EDA) and Machine Learning**, this project provides **valuable insights for football analysts, scouts, club managers, and sports economists** to better understand **transfer market dynamics and player valuation**.

## 🏆 Objectives  

### **1️⃣ Global Transfer Market Analysis**  
- **Analyze player transfer trends** across all teams and leagues during the **2021-2022 and 2022-2023** seasons.  
- **Identify key factors** influencing a player's market value, such as **age, position, goals, assists, injuries, and transfer history**.  
- **Assess the impact of injuries** on player valuations and market demand.  
- **Examine the most active clubs in the transfer market** and their spending patterns.  
- **Develop a predictive model** that estimates player **market value** based on historical data and key performance indicators.  

### **2️⃣ Real Madrid Players’ Performance & Market Value (Streamlit Dashboard)**  
- **Visualize player statistics** for **Real Madrid** players, including **performance metrics, market value shifts, and transfer activities**.  
- **Track the evolution of Real Madrid squad value** compared to the global transfer market.  
- **Provide an interactive experience** where users can explore **player performances, injuries, and market trends** through Streamlit.  

## 🛠️ Tools & Technologies  
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)  
- **Jupyter Notebook / Google Colab** for data analysis and model development  
- **Machine Learning**: Scikit-learn for predictive modeling  
- **Data Visualization**: Streamlit for interactive storytelling and dashboards  
- **Exploratory Data Analysis (EDA)** to understand trends in player transfers and market values  

## 🔥 Key Insights  
- Teams prioritize defense (32.8%) and midfield (28.8%) over forwards (27.0%), with goalkeepers (11.4%) being the least represented due to their specialized role.
<img width="629" alt="Screenshot 1446-08-24 at 3 17 40 PM" src="https://github.com/user-attachments/assets/522b82e2-1c03-42c1-af16-5dbcd4722e7e" />



- Daejeon Hana Citizen and Jeonbuk Hyundai Motors were the most active teams in the transfer market, indicating a high player turnover strategy.
<img width="992" alt="Screenshot 1446-08-24 at 3 20 00 PM" src="https://github.com/user-attachments/assets/5701f7ed-f422-4ac7-9a4a-e858ccc81847" />



- Defenders play the most minutes on average, highlighting their crucial role in maintaining team stability.
<img width="706" alt="Screenshot 1446-08-24 at 3 20 42 PM" src="https://github.com/user-attachments/assets/4a9654f0-8b63-433e-9c04-e8eff5242a4a" />



- Player market value has a strong positive correlation with highest historical value, appearances, and awards received.


## 📌 Storytelling  
To explore insights visually, visit our **Streamlit Storytelling Dashboard**:  
👉 **[View the Dashboard Here](https://usecase-7-igmjq6zrxgwqhych9gxjf8.streamlit.app/)**  


## 🚀 Model Deployment 

We deployed the supervised machine learning regression algorithm,  Random Forest model on Render web server using FastAPI.

👉 **[View the Predication Model Here](https://usecase-7-vvhu.onrender.com/docs#/default/predict_predict_post)**  

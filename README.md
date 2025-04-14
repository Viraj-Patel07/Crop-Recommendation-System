# 🌾 Crop Recommendation System

A smart, data-driven crop recommendation and cost estimation system for farmers based on soil type, pH levels, and operational costs. This tool helps in identifying the most suitable crops for a specific farm and provides detailed cost estimates for cultivation.

---


---

## 🚀 Features

- Recommends crops based on farm's **soil type** and **pH range**
- Calculates **per-acre and total cultivation costs** for recommended crops
- Uses data from **local surveys**, **Agmarknet**, and **APMC**
- Provides detailed crop-wise input breakdown (e.g., irrigation, harvesting, etc.)
- User input-based recommendations with interactive CLI

---

## 📦 Dependencies

- Python 3.x
- Pandas
- NumPy
- Matplotlib (optional, for future visualizations)

---

## 📊 Data Sources

- **Cost Data**: Surveyed from local farmers
- **Production Data**: [Agmarknet](https://agmarknet.gov.in/)
- **Market Price Data**: Agriculture Produce Marketing Committee (APMC)

---

## 🧠 How It Works

1. User selects a **farm ID** from the dataset.
2. Based on the farm's **soil type** and **pH values**, suitable crops are identified.
3. The system fetches **input cost data** for each recommended crop.
4. User inputs **farm area in acres**.
5. The system outputs:
   - Recommended crops
   - Per-acre costs
   - Total cost of cultivation for each crop

---

---

## 🛠️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Viraj-Patel07/Crop-Recommendation-System.git
   cd Crop-Recommendation-System
2. Make sure all required .csv files are in place.

3.Run the main script:
```
python main.py
```
## 🧾 Future Improvements
- Integrate with real-time market pricing APIs

- Add yield and revenue prediction





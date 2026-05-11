### Lab Report CH 12 - Regression
## Student Information
**Name:** Leiliany Davila

**Date:** 5/9/26

**Algorithm Analysis:** K-Nearest Neighbors (KNN) Regression for Bakery Loaf Prediction

---

## Algorithm Understanding

**What type of problem is this algorithm solving?**  
- It is a supervised learning regression problem. The goal is to predict a continuous numerical outcome, specifically the number of loaves the bakery should produce for a given day.

**How does KNN regression differ from KNN classification?**  
- KNN regression predicts a continuous value by averaging the target values of the k nearest neighbors, while KNN classification predicts a discrete label based on the majority class among those neighbors.

**What does the "K" in KNN represent, and why did we choose k=4 for this problem?**  
- "K" represents the number of nearest data points (neighbors) the model looks at when making a prediction. Choosing k=4 helps balance between overfitting and underfitting by considering multiple similar days without including too much unrelated data.

**In your own words, explain how the model produces a prediction for a new day.**  
- The model compares the new day’s features (like weather, weekend/holiday, and game day) to all past days in the dataset, calculates how similar they are, and selects the 4 closest matches. It then averages the loaf counts from those 4 days to produce the final prediction.

---

## Implementation Questions

**Why do we separate the DataFrame into features (X) and target (y) before training?**  
- This separation allows the model to learn how the input variables (features like weather and events) relate to the output (number of loaves). X contains the inputs, and y contains the values we want to predict.

**Why must the input to `model.predict()` be a 2D array (e.g., `[[4, 1, 0]]`) instead of a 1D array (`[4, 1, 0]`)?**  
- The model expects a 2D array because it is designed to handle multiple samples at once. Even when predicting for a single day, it still requires the input to follow that same structure (rows = samples, columns = features).

**What does `.fit(X, y)` actually do for a KNN model? (Hint: it's different from most other ML algorithms.)**  
- In KNN, .fit() does not train a model in the traditional sense. Instead, it simply stores the training data so it can be used later to calculate distances and find the nearest neighbors. This is why KNN is called a “lazy learner.”

**Why do we use `.values` when extracting columns from the DataFrame?**  
- We use .values to convert the DataFrame into a NumPy array, which is the format that machine learning models like KNN expect for computations.

---

## Extension: Choosing K

**What would happen if we set k=1? What are the risks?**  
- The model would base predictions on only the single nearest neighbor. This can lead to overfitting and make predictions highly sensitive to noise or unusual data points.

**What would happen if we set k=20 (the size of the entire dataset)? What does the model become?**  
- The model would average all data points in the dataset, essentially predicting the overall mean number of loaves regardless of the input features.

**How would you decide what value of k is best for a given dataset?**  
- You would test different values of k using a validation set or cross-validation and choose the one that minimizes prediction error (such as mean squared error).

---

## Extension: Distance and Feature Scaling

**KNN uses distance to find "nearest" neighbors. Our features have very different ranges: weather is 1–5, but weekend_holiday and game_on are 0/1. Why could this be a problem?**  
- Features with larger ranges can dominate the distance calculation, causing the model to prioritize those features more, even if they are not the most important.

**Give an example of two days where the weather feature would unfairly dominate the distance calculation.**  
- For example, comparing Day A (weather=5, weekend=0, game=0) and Day B (weather=1, weekend=1, game=1), the large difference in weather (5 vs. 1) might outweigh the differences in the other two features, even though those binary features could be equally important.

**How would you modify the data preparation step to fix this? (Hint: look up "feature scaling" or "StandardScaler".)**  
- I would apply feature scaling, such as StandardScaler, to normalize all features so they have similar ranges. This ensures that no single feature dominates the distance calculation.

---

## Reflection Questions

**What is a limitation of KNN regression? Provide a scenario where it would make a poor prediction.**  
- A limitation is that it struggles with data points that are very different from the training data. For example, if there is an extremely unusual day (like a major festival + extreme weather), the model may not have similar past examples and will make an inaccurate prediction.

**Our dataset only has 20 days of data. How might the predictions change if we had 2,000 days of data instead?**  
- With more data, predictions would likely be more accurate and stable because the model would have a larger variety of similar past days to compare with.

**What other features (beyond weather, weekend/holiday, and game day) could the bakery collect to improve predictions?**  
- Temperature, season, day of the week, foot traffic, local events, promotions, and social media trends could all improve prediction accuracy.

**KNN is sometimes called a "lazy learning" algorithm because it does almost no work during training. What is the tradeoff at prediction time?**  
- The tradeoff is that prediction becomes slower, because the model must calculate distances between the new data point and every stored training example.

**The autograder expects a prediction of approximately 70.5 loaves for today's conditions. Manually look at the dataset and identify which 4 historical days you think the model is averaging. Do their loaf counts average to 70.5?**  
- The 4 selected days would be the ones with feature values most similar to today’s conditions. When their loaf counts are averaged, they should come out to approximately 70.5, confirming how KNN computes predictions.

**Why might a bakery prefer a slightly inaccurate ML prediction over a human guess for daily loaf counts?**  
- ML predictions are consistent, data-driven, and scalable. They reduce bias, can improve over time with more data, and help minimize waste compared to subjective human guesses.

**If the bakery wanted to MINIMIZE waste (unsold loaves) rather than just predict accurately, how might you change the approach?**  
- The bakery could adjust predictions slightly downward, use a cost-sensitive approach that penalizes overproduction more than underproduction, or optimize for minimizing waste instead of just minimizing prediction error.

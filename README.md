# 🏦 Loan Approval Prediction
> An AI-powered web app that predicts loan approval eligibility based on applicant financial profile using Machine Learning.
> 
# Loan-Approval-Prediction-Model
## 🔗 Live Demo
[Click here to try it] https://huggingface.co/spaces/a4ryaaaa/Loan-Approval-Prediction-Model

## 🛠️ Tech Stack
| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS, Bootstrap 5 |
| Backend | Python, Flask |
| ML Model | scikit-learn, Random Forest |
| Deployment | Hugging Face Spaces |

## 🧠 How It Works
1. User fills in financial details on the form
2. Flask backend reads the submitted data
3. Data is passed to a trained Random Forest model
4. Model predicts **Approved** or **Rejected**
5. Result is displayed back on the page instantly

## 📊 Input Features

| Feature | Description |
|---------|-------------|
| Annual Income | Applicant's yearly income |
| Loan Amount | Requested loan amount |
| Loan Term | Duration in months |
| CIBIL Score | Credit score (300–900) |
| Residential Assets | Value of residential property |
| Commercial Assets | Value of commercial property |
| Luxury Assets | Value of luxury items |
| Bank Assets | Bank account value |
| Dependents | Number of dependents |
| Education | Graduate or not |
| Self Employed | Employment status |

## ⚙️ Run Locally

```bash
# Clone the repo
git clone https://github.com/YOURUSERNAME/loan-approval-prediction.git

# Go into the folder
cd loan-approval-prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open `http://localhost:7860` in your browser.

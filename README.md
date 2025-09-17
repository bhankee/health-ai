
# My Health AI

**Get custom meal plans from daily weight metrics from smart scales to hit health goals — powered by Gemini LLM + Python.**

<p align="center">
<img src="/images/health-ai-1.png" alt="Health AI Project" height="400" style="margin:0 20px; border-radius:15px;"/>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/yourusername/ai-weight-coach/pulls)

---


## 🚀 Overview

This project connects to your smart scale (Withings Brand), pulls in daily weight measurements, and feeds them into **Google’s Gemini LLM** with a **dynamic, goal-oriented prompt**.
Each day, it generates:

* 🍽 **Meal Plan** – tailored to your current weight & target weight
* 🏃 **Activity Plan** – realistic exercise suggestions

---

## 🛠 Tech Stack

* **Python** 🐍 – data fetching, processing, and prompt orchestration
* **Gemini LLM** 🤖 – intelligent meal & activity plan generation
* **Google Sheets API** – easy data handling

## ✨ Features

✅ **Automated Data Fetching** – Pulls weight data from your smart scale daily
✅ **Dynamic Goal Prompts** – Customizes AI prompts based on your current weight & target weight
✅ **LLM-Powered Planning** – Uses Gemini to generate detailed, realistic daily plans
✅ **Easy to Extend** – Works with any smart scale API, or manually input data
✅ **Open Source & Hackable** – Perfect starting point for personal health automation

---

## Screenshot

<img src="/images/screenshot.png" alt="Health AI Project screen shot" height="400" style="margin:0 20px; border-radius:15px;"/>

## 🔧 Configuration

Edit your **.env** file to include:

```env
GEMINI_API_KEY=your_api_key_here
GOOGLE_SHEET_ID=Key for accessing Google Sheet with data
```

---

## 🤝 Contributing

Pull requests are welcome! Got ideas for improving prompts, meal plans, or integrations?
Fork the repo, open an issue, or submit a PR.

---

## 📜 License

MIT – free to use, modify, and share.



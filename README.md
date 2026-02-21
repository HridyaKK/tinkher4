# 🛡️ SafePath – Smart Women Safety Route Predictor

---

## 🚀 Project Overview

**SafePath** is an intelligent route prediction system that prioritizes *safety over speed*. Unlike traditional navigation apps that give the shortest route, SafePath calculates multiple possible routes between a source and destination and recommends the **safest route based on crime, lighting, and crowd-safety metrics**.

This tool is designed with **women’s safety in mind**, helping users choose safer paths, especially at night or in unfamiliar areas.

---

## 🧠 Problem Statement

Most navigation apps like Google Maps optimize for *shortest* or *fastest* routes — but shortest doesn’t always mean safest.  
At night or in unfamiliar places, women commonly face:

- Poorly lit streets  
- Isolated areas  
- High-crime zones  
- Low pedestrian density  

There is no widely available navigation tool that dynamically predicts **safety scores** for routes — SafePath fills that gap.

---

## 🛠️ Features

### ✔️ MVP (Built in 10 Hours)

- **Interactive Web App** built with Streamlit  
- **Input:** Source & Destination area IDs  
- **Safety Scoring:** Crime, lighting, and crowd data  
- **Multiple Route Simulation** (2–3 routes)  
- **Safest Route Recommendation**  
- **Day/Night Mode Toggle**  
- **Emergency Button** to suggest nearby safe points  
- **Color-rendered routes** on the map (Green/Yellow/Red)  
- **Heatmap visualization (optional)**  

---

## 📁 File Structure

---

## 🧩 Technical Logic

### 📊 Safety Score Formula

Each area is assigned:

- Crime score (0–10)
- Lighting score (0–10)
- Crowd density (0–10)
- Night-time multiplier

**Safety Score = (10 − Crime Score) + Lighting Score + Crowd Density**

At night:
- Crime score is multiplied → reduces safety score

---

## 🚧 How It Works

1. User enters source & destination area IDs  
2. App simulates multiple route paths  
3. Each route segment is scored using the safety formula  
4. Safest route is highlighted
    - 🟢 Safe
    - 🟡 Moderate
    - 🔴 Unsafe  
5. Emergency button suggests nearest safe area

---

## 🔧 Tech Stack

| Component | Technology |
|-----------|------------|
| UI | Streamlit |
| Map | Folium |
| Data | Dummy CSV dataset |
| Logic & Routing | Python |

---

## 👥 Team & Responsibilities

| Name | Role | Tasks |
|------|------|-------|
| **Arshi** | Frontend Developer | • UI/UX in Streamlit<br>• Map rendering<br>• Toggle buttons, heatmap, emergency UI |
| **Hridya** | Backend Developer | • Safety scoring logic<br>• Route simulation<br>• Emergency alert logic |

---

## 🕐 Project Hours Timeline (10-Hour Plan)

| Time Block | Tasks |
|------------|-------|
| Hour 1–2 | Setup project & repo |
| Hour 2–4 | Backend dataset & scoring logic |
| Hour 2–4 | Frontend UI & inputs |
| Hour 4–6 | Integrate routes & safety calculation |
| Hour 6–8 | Map plotting & color coding |
| Hour 8–9 | Emergency button & safe point |
| Hour 9–10 | Testing & polishing UX |

---

## 📝 Sample Commands

### 🚀 Run App
```bash
streamlit run app.py

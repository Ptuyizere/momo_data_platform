# MoMo SMS Data Pipeline & Dashboard

This project extracts, cleans, and analyzes MoMo SMS transaction data provided in XML format.
It transforms raw SMS messages into structured records, categorizes transactions, loads them into a relational database (SQLite by default), and serves a lightweight frontend dashboard for visualization and analysis.

## Features:

ETL Pipeline:

Parse XML SMS dumps (lxml / ElementTree)

Clean & normalize dates, phone numbers, and amounts

Categorize transactions (e.g., Send Money, Deposit, Airtime, Bill Payment)

Store structured data into SQLite

Data Storage:

SQLite database (data/db.sqlite3)

JSON export for frontend consumption (data/processed/dashboard.json)

Frontend Dashboard:

Static HTML + JS (index.html, web/chart_handler.js)

Charts and tables for quick insights

Simple styling with CSS

APIs (Optional):

Minimal FastAPI service for querying transactions and analytics

JSON endpoints (/transactions, /analytics)

## Relevant Links:

High-Level System Architecture Diagram: https://drive.google.com/file/d/1IJlZMuli0VDOe9iXFVfhkn5CgBHm4-SW/view?usp=sharing

Project Progress on Trello: https://trello.com/invite/b/68c07705db863a8233f64f3e/ATTId57b9637bb12d7e3676a0ec88f0a46dfF253EFC5/momo-data-platform
# English

# Data Analysis and Machine Learning Template

This template provides a comprehensive starting point for data analysis, machine learning, and artificial intelligence applications. This Streamlit-based template allows you to quickly develop and deploy your data science projects.

## 🚀 Features

### Data Management

- 📂 Multiple file format support (CSV, Excel, JSON)
- 🔍 Data validation and cleaning
- 🔄 Data transformation and preprocessing
- 📊 Data visualization

### Analysis and Modeling

- 📈 Basic statistical analysis
- 🔗 Correlation analysis
- 📉 Trend analysis
- ⚠️ Anomaly detection
- 🤖 Machine learning models
- 🧠 AI-powered insight generation

### Reporting

- 📄 PDF report generation
- 🌐 HTML report generation
- 📊 CSV report generation

### Other Features

- 🛡️ Comprehensive error handling
- ⚙️ Configurable settings
- 📝 Detailed logging
- 🔄 API integration

## 🛠️ Installation

### 1. Requirements

- Python 3.8 or higher
- pip (Python package manager)

### 2. Cloning the Project

```bash
git clone https://github.com/yourusername/template.git
cd template
```

### 3. Creating Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### 4. Installing Required Packages

```bash
pip install -r requirements.txt
```

### 5. Setting Environment Variables

```bash
cp .env.example .env
# Edit the .env file to configure necessary settings
```

## 📝 User Guide

### 1. Data Loading

#### File Upload

1. Start the application:

```bash
streamlit run src/main.py
```

2. Select "File Upload" from the sidebar
3. Choose one of the supported formats (CSV, Excel, JSON)
4. Upload your file

#### Using Sample Data

1. Select "Sample Data" from the sidebar
2. The system will automatically load the sample dataset

#### Fetching Data from API

1. Select "API" from the sidebar
2. Enter the API URL
3. Click the "Fetch Data" button

### 2. Data Analysis

#### Basic Statistics

1. Select "Basic Statistics" from the sidebar
2. The system will automatically show:
   - Basic statistics for numerical variables
   - Frequency distributions for categorical variables
   - Missing value analysis

#### Correlation Analysis

1. Select "Correlation" from the sidebar
2. The system will automatically show:
   - Correlation matrix
   - Heatmap visualization
   - Highest correlated variable pairs

#### Trend Analysis

1. Select "Trend Analysis" from the sidebar
2. The system will automatically show:
   - Time series graphs
   - Trend analysis
   - Seasonality analysis

#### Anomaly Detection

1. Select "Anomaly Detection" from the sidebar
2. The system will automatically show:
   - Anomaly scores
   - Anomaly distribution
   - Anomaly details

### 3. Model Training

#### Regression

1. Select "Regression" from the sidebar
2. Choose the model type (Linear Regression, Random Forest)
3. The system will automatically show:
   - Model training
   - Performance metrics
   - Prediction results

#### Classification

1. Select "Classification" from the sidebar
2. Choose the model type (Logistic Regression, Random Forest)
3. The system will automatically show:
   - Model training
   - Performance metrics
   - Confusion matrix

#### Clustering

1. Select "Clustering" from the sidebar
2. Choose the model type (K-Means)
3. The system will automatically show:
   - Clustering results
   - Silhouette score
   - Cluster centers

### 4. Insight Generation

#### PCA Analysis

1. Select "PCA Analysis" from the sidebar
2. The system will automatically show:
   - PCA results
   - Variance explanation ratio
   - PCA visualization

#### t-SNE Visualization

1. Select "t-SNE Visualization" from the sidebar
2. The system will automatically show:
   - t-SNE results
   - t-SNE visualization

#### Feature Importance

1. Select "Feature Importance" from the sidebar
2. The system will automatically show:
   - Feature importance scores
   - Feature importance graph

### 5. Report Generation

#### PDF Report

1. Select "PDF Report" from the sidebar
2. Enter the report title
3. Click the "Generate Report" button

#### HTML Report

1. Select "HTML Report" from the sidebar
2. Enter the report title
3. Click the "Generate Report" button

#### CSV Report

1. Select "CSV Report" from the sidebar
2. Enter the report title
3. Click the "Generate Report" button

## 💻 CLI Usage

You can use the following commands to use the template from the command line:

### 1. Data Loading

```bash
# Load data from file
python src/cli.py load --file data.csv --output output.csv

# Load data from API
python src/cli.py load --api https://api.example.com/data --output output.csv

# Use sample data
python src/cli.py load --sample --output output.csv
```

### 2. Data Analysis

```bash
# Basic statistics
python src/cli.py analyze --input data.csv --type stats --output stats.json

# Correlation analysis
python src/cli.py analyze --input data.csv --type corr --output corr.json

# Trend analysis
python src/cli.py analyze --input data.csv --type trend --output trend.json

# Anomaly detection
python src/cli.py analyze --input data.csv --type anomaly --output anomaly.json
```

### 3. Model Training

```bash
# Regression model
python src/cli.py train --input data.csv --type regression --model linear_regression --output model.json

# Classification model
python src/cli.py train --input data.csv --type classification --model random_forest --output model.json

# Clustering model
python src/cli.py train --input data.csv --type clustering --model kmeans --output model.json
```

### 4. Insight Generation

```bash
# PCA analysis
python src/cli.py insight --input data.csv --type pca --output pca.json

# t-SNE visualization
python src/cli.py insight --input data.csv --type tsne --output tsne.json

# Feature importance
python src/cli.py insight --input data.csv --type feature --output feature.json
```

### 5. Report Generation

```bash
# PDF report
python src/cli.py report --input data.csv --type pdf --output report.pdf

# HTML report
python src/cli.py report --input data.csv --type html --output report.html

# CSV report
python src/cli.py report --input data.csv --type csv --output report.csv
```

### Help

```bash
# General help
python src/cli.py --help

# Command help
python src/cli.py load --help
python src/cli.py analyze --help
python src/cli.py train --help
python src/cli.py insight --help
python src/cli.py report --help
```

## 🏗️ Project Structure

```
template/
├── src/
│   ├── main.py              # Main application file
│   ├── cli.py               # Command line interface
│   └── api/                 # API endpoints
│       ├── __init__.py
│       ├── routes.py        # API routes
│       └── schemas.py       # API schemas
├── utils/
│   ├── data_loader.py       # Data loading module
│   ├── data_processor.py    # Data processing module
│   ├── data_analyzer.py     # Data analysis module
│   ├── ml_model.py          # Machine learning module
│   ├── ai_processor.py      # AI processing module
│   ├── report_generator.py  # Report generation module
│   ├── error_handler.py     # Error handling module
│   └── visualization.py     # Visualization utilities
├── config/
│   ├── settings.py          # Settings module
│   └── logging_config.py    # Logging configuration
├── data/                    # Data files
│   ├── raw/                 # Raw data
│   ├── processed/           # Processed data
│   └── external/            # External data sources
├── models/                  # Trained models
│   ├── saved/               # Saved model files
│   └── checkpoints/         # Model checkpoints
├── reports/                 # Generated reports
│   ├── figures/             # Report figures
│   └── templates/           # Report templates
├── assets/                  # Static files
│   ├── images/              # Image assets
│   └── styles/              # CSS styles
├── tests/                   # Test files
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   └── fixtures/            # Test fixtures
├── docs/                    # Documentation
│   ├── api/                 # API documentation
│   └── guides/              # User guides
├── notebooks/               # Jupyter notebooks
├── requirements.txt         # Requirements
├── requirements-dev.txt     # Development requirements
├── setup.py                 # Package setup
├── .env.example             # Example environment variables
├── .gitignore               # Git ignore file
├── LICENSE                  # License file
└── README.md                # This file
```

## 🔧 Development

### 1. Adding New Feature

1. Update the relevant module
2. Add tests
3. Update documentation

### 2. Error Fixing

1. Check the error report
2. Fix the issue
3. Run tests

### 3. Performance Improvement

1. Identify performance issues
2. Apply improvements
3. Run performance tests

## 🤝 Contribution

1. Fork this repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push your branch (`git push origin feature/amazing-feature`)
5. Create a pull request

## 📄 License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.

## 📞 Contact

- Project Owner: [Buğra Görmüş](mailto:bugra.gormus@hotmail.com)
- Project Link: [https://github.com/bugragormus/Data-Analysis-and-Machine-Learning-Template](https://github.com/bugragormus/Data-Analysis-and-Machine-Learning-Template)

## 🙏 Thanks

Thank you for using this template! If you have any questions or suggestions, please feel free to contact us.

## 🎯 Use Cases and Examples

This template can be used for the following areas and purposes:

### 1. Financial Analysis and Prediction

- **Stock Data Analysis**

  ```python
  # Stock Price Prediction
  python src/cli.py train --input stock_data.csv --type regression --model random_forest --output stock_prediction.json

  # Financial Risk Analysis
  python src/cli.py analyze --input financial_data.csv --type anomaly --output risk_analysis.json
  ```

- **Credit Scoring**
  ```python
  # Customer Credit Risk Assessment
  python src/cli.py train --input customer_data.csv --type classification --model random_forest --output credit_score.json
  ```

### 2. Marketing and Customer Analysis

- **Customer Segmentation**

  ```python
  # Customer Clustering
  python src/cli.py train --input customer_data.csv --type clustering --model kmeans --output customer_segments.json

  # Customer Behavior Analysis
  python src/cli.py analyze --input customer_behavior.csv --type trend --output behavior_analysis.json
  ```

- **Marketing Campaign Optimization**
  ```python
  # Campaign Effectiveness Analysis
  python src/cli.py analyze --input campaign_data.csv --type stats --output campaign_analysis.json
  ```

### 3. Health and Bioinformatics

- **Disease Diagnosis**

  ```python
  # Medical Data Analysis
  python src/cli.py train --input medical_data.csv --type classification --model random_forest --output diagnosis_model.json

  # Patient Risk Analysis
  python src/cli.py analyze --input patient_data.csv --type anomaly --output risk_assessment.json
  ```

- **Genomic Data Analysis**
  ```python
  # Gene Expression Analysis
  python src/cli.py insight --input gene_expression.csv --type pca --output gene_analysis.json
  ```

### 4. Production and Quality Control

- **Production Line Optimization**

  ```python
  # Production Efficiency Analysis
  python src/cli.py analyze --input production_data.csv --type trend --output efficiency_analysis.json

  # Quality Prediction
  python src/cli.py train --input quality_data.csv --type classification --model logistic_regression --output quality_prediction.json
  ```

- **Failure Prediction**
  ```python
  # Machine Failure Prediction
  python src/cli.py train --input machine_data.csv --type classification --model random_forest --output failure_prediction.json
  ```

### 5. Education and Research

- **Student Performance Prediction**

  ```python
  # Student Performance Prediction
  python src/cli.py train --input student_data.csv --type regression --model linear_regression --output performance_prediction.json

  # Education Effectiveness Analysis
  python src/cli.py analyze --input education_data.csv --type stats --output effectiveness_analysis.json
  ```

- **Research Data Analysis**
  ```python
  # Experimental Data Analysis
  python src/cli.py analyze --input experimental_data.csv --type corr --output experimental_analysis.json
  ```

### 6. Social Media and Content Analysis

- **Sentiment Analysis**
  ```python
  # Social Media Sentiment Analysis
  python src/cli.py train --input social_media_data.csv --type classification --model logistic_regression --output sentiment_analysis.json
  ```
- **Content Recommendation System**
  ```python
  # User Preference Analysis
  python src/cli.py insight --input user_preferences.csv --type tsne --output preference_analysis.json
  ```

### 7. Energy and Environment

- **Energy Consumption Prediction**

  ```python
  # Energy Usage Analysis
  python src/cli.py train --input energy_data.csv --type regression --model random_forest --output consumption_prediction.json

  # Environmental Data Analysis
  python src/cli.py analyze --input environmental_data.csv --type trend --output environmental_analysis.json
  ```

### 8. Retail and Supply Chain

- **Demand Prediction**

  ```python
  # Sales Prediction
  python src/cli.py train --input sales_data.csv --type regression --model linear_regression --output sales_prediction.json

  # Inventory Analysis
  python src/cli.py analyze --input inventory_data.csv --type anomaly --output inventory_analysis.json
  ```

### 9. Security and Fraud Detection

- **Anomaly Detection**

  ```python
  # Fraud Detection
  python src/cli.py train --input transaction_data.csv --type classification --model random_forest --output fraud_detection.json

  # Security Threat Analysis
  python src/cli.py analyze --input security_logs.csv --type anomaly --output threat_analysis.json
  ```

### 10. Automotive and Transportation

- **Vehicle Maintenance Prediction**

  ```python
  # Vehicle Failure Prediction
  python src/cli.py train --input vehicle_data.csv --type classification --model random_forest --output maintenance_prediction.json

  # Traffic Analysis
  python src/cli.py analyze --input traffic_data.csv --type trend --output traffic_analysis.json
  ```

### 11. Natural Language Processing

- **Text Classification**

  ```python
  # Document classification
  python src/cli.py train --input text_data.csv --type classification --model random_forest --output text_classification.json

  # Sentiment analysis
  python src/cli.py train --input sentiment_data.csv --type classification --model logistic_regression --output sentiment_analysis.json
  ```

- **Text Generation**
  ```python
  # Text generation analysis
  python src/cli.py insight --input text_data.csv --type pca --output text_analysis.json
  ```

### 12. Image Processing

- **Image Classification**

  ```python
  # Image classification
  python src/cli.py train --input image_data.csv --type classification --model random_forest --output image_classification.json

  # Object detection
  python src/cli.py analyze --input object_data.csv --type anomaly --output object_detection.json
  ```

### 13. Time Series Analysis

- **Forecasting**

  ```python
  # Time series forecasting
  python src/cli.py train --input time_series.csv --type regression --model random_forest --output forecasting.json

  # Seasonality analysis
  python src/cli.py analyze --input seasonal_data.csv --type trend --output seasonality_analysis.json
  ```

### 14. IoT and Sensor Data Analysis

- **Sensor Data Processing**

  ```python
  # Sensor data analysis
  python src/cli.py analyze --input sensor_data.csv --type anomaly --output sensor_analysis.json

  # Predictive maintenance
  python src/cli.py train --input iot_data.csv --type classification --model random_forest --output maintenance_prediction.json
  ```

### 15. Blockchain and Cryptocurrency Analysis

- **Cryptocurrency Price Prediction**

  ```python
  # Crypto price analysis
  python src/cli.py analyze --input crypto_data.csv --type trend --output crypto_analysis.json

  # Blockchain transaction analysis
  python src/cli.py train --input blockchain_data.csv --type classification --model random_forest --output transaction_analysis.json
  ```

### 16. Augmented Reality and Virtual Reality

- **AR/VR Data Analysis**

  ```python
  # User interaction analysis
  python src/cli.py analyze --input ar_vr_data.csv --type stats --output interaction_analysis.json

  # Performance optimization
  python src/cli.py train --input performance_data.csv --type regression --model random_forest --output optimization.json
  ```

Each use case provides:

- Data loading and preprocessing
- Analysis and visualization
- Model training and evaluation
- Insight generation
- Report generation

features. The template allows you to quickly develop and deploy data science projects in these areas.

# Türkçe

# Veri Analizi ve Makine Öğrenmesi Template

Bu template, veri analizi, makine öğrenmesi ve yapay zeka uygulamaları için kapsamlı bir başlangıç noktası sunar. Streamlit tabanlı bu template, veri bilimi projelerinizi hızlıca geliştirmenize ve dağıtmanıza olanak tanır.

## 🚀 Özellikler

### Veri Yönetimi

- 📂 Çoklu dosya formatı desteği (CSV, Excel, JSON)
- 🔍 Veri doğrulama ve temizleme
- 🔄 Veri dönüştürme ve ön işleme
- 📊 Veri görselleştirme

### Analiz ve Modelleme

- 📈 Temel istatistiksel analizler
- 🔗 Korelasyon analizi
- 📉 Trend analizi
- ⚠️ Anomali tespiti
- 🤖 Makine öğrenmesi modelleri
- 🧠 Yapay zeka ile içgörü oluşturma

### Raporlama

- 📄 PDF rapor oluşturma
- 🌐 HTML rapor oluşturma
- 📊 CSV rapor oluşturma

### Diğer Özellikler

- 🛡️ Kapsamlı hata yönetimi
- ⚙️ Yapılandırılabilir ayarlar
- 📝 Detaylı loglama
- 🔄 API entegrasyonu

## 🛠️ Kurulum

### 1. Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)

### 2. Projeyi Klonlama

```bash
git clone https://github.com/yourusername/template.git
cd template
```

### 3. Sanal Ortam Oluşturma (Önerilen)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

### 4. Gerekli Paketleri Yükleme

```bash
pip install -r requirements.txt
```

### 5. Ortam Değişkenlerini Ayarlama

```bash
cp .env.example .env
# .env dosyasını düzenleyerek gerekli ayarları yapın
```

## 📝 Kullanım Kılavuzu

### 1. Veri Yükleme

#### Dosya Yükleme

1. Uygulamayı başlatın:

```bash
streamlit run src/main.py
```

2. Kenar çubuğundan "Dosya Yükle" seçeneğini seçin
3. Desteklenen formatlardan birini seçin (CSV, Excel, JSON)
4. Dosyanızı yükleyin

#### Örnek Veri Kullanma

1. Kenar çubuğundan "Örnek Veri" seçeneğini seçin
2. Sistem otomatik olarak örnek veri setini yükleyecektir

#### API'den Veri Çekme

1. Kenar çubuğundan "API" seçeneğini seçin
2. API URL'sini girin
3. "Veri Çek" butonuna tıklayın

### 2. Veri Analizi

#### Temel İstatistikler

1. Kenar çubuğundan "Temel İstatistikler" seçeneğini seçin
2. Sistem otomatik olarak:
   - Sayısal değişkenler için temel istatistikleri
   - Kategorik değişkenler için frekans dağılımlarını
   - Eksik değer analizini gösterecektir

#### Korelasyon Analizi

1. Kenar çubuğundan "Korelasyon" seçeneğini seçin
2. Sistem otomatik olarak:
   - Korelasyon matrisini
   - Heatmap görselleştirmesini
   - En yüksek korelasyonlu değişken çiftlerini gösterecektir

#### Trend Analizi

1. Kenar çubuğundan "Trend Analizi" seçeneğini seçin
2. Sistem otomatik olarak:
   - Zaman serisi grafiklerini
   - Trend analizini
   - Mevsimsellik analizini gösterecektir

#### Anomali Tespiti

1. Kenar çubuğundan "Anomali Tespiti" seçeneğini seçin
2. Sistem otomatik olarak:
   - Anomali skorlarını
   - Anomali dağılımını
   - Anomali detaylarını gösterecektir

### 3. Model Eğitimi

#### Regresyon

1. Kenar çubuğundan "Regresyon" seçeneğini seçin
2. Model tipini seçin (Linear Regression, Random Forest)
3. Sistem otomatik olarak:
   - Model eğitimini
   - Performans metriklerini
   - Tahmin sonuçlarını gösterecektir

#### Sınıflandırma

1. Kenar çubuğundan "Sınıflandırma" seçeneğini seçin
2. Model tipini seçin (Logistic Regression, Random Forest)
3. Sistem otomatik olarak:
   - Model eğitimini
   - Performans metriklerini
   - Karışıklık matrisini gösterecektir

#### Kümeleme

1. Kenar çubuğundan "Kümeleme" seçeneğini seçin
2. Model tipini seçin (K-Means)
3. Sistem otomatik olarak:
   - Kümeleme sonuçlarını
   - Silhouette skorunu
   - Küme merkezlerini gösterecektir

### 4. İçgörü Oluşturma

#### PCA Analizi

1. Kenar çubuğundan "PCA Analizi" seçeneğini seçin
2. Sistem otomatik olarak:
   - PCA sonuçlarını
   - Varyans açıklama oranını
   - PCA görselleştirmesini gösterecektir

#### t-SNE Görselleştirme

1. Kenar çubuğundan "t-SNE Görselleştirme" seçeneğini seçin
2. Sistem otomatik olarak:
   - t-SNE sonuçlarını
   - t-SNE görselleştirmesini gösterecektir

#### Özellik Önemliliği

1. Kenar çubuğundan "Özellik Önemliliği" seçeneğini seçin
2. Sistem otomatik olarak:
   - Özellik önemlilik skorlarını
   - Özellik önemlilik grafiğini gösterecektir

### 5. Rapor Oluşturma

#### PDF Rapor

1. Kenar çubuğundan "PDF Rapor" seçeneğini seçin
2. Rapor başlığını girin
3. "Rapor Oluştur" butonuna tıklayın

#### HTML Rapor

1. Kenar çubuğundan "HTML Rapor" seçeneğini seçin
2. Rapor başlığını girin
3. "Rapor Oluştur" butonuna tıklayın

#### CSV Rapor

1. Kenar çubuğundan "CSV Rapor" seçeneğini seçin
2. Rapor başlığını girin
3. "Rapor Oluştur" butonuna tıklayın

## 💻 CLI Kullanımı

Template'i komut satırından kullanmak için aşağıdaki komutları kullanabilirsiniz:

### 1. Veri Yükleme

```bash
# Dosyadan veri yükleme
python src/cli.py load --file data.csv --output output.csv

# API'den veri yükleme
python src/cli.py load --api https://api.example.com/data --output output.csv

# Örnek veri kullanma
python src/cli.py load --sample --output output.csv
```

### 2. Veri Analizi

```bash
# Temel istatistikler
python src/cli.py analyze --input data.csv --type stats --output stats.json

# Korelasyon analizi
python src/cli.py analyze --input data.csv --type corr --output corr.json

# Trend analizi
python src/cli.py analyze --input data.csv --type trend --output trend.json

# Anomali tespiti
python src/cli.py analyze --input data.csv --type anomaly --output anomaly.json
```

### 3. Model Eğitimi

```bash
# Regresyon modeli
python src/cli.py train --input data.csv --type regression --model linear_regression --output model.json

# Sınıflandırma modeli
python src/cli.py train --input data.csv --type classification --model random_forest --output model.json

# Kümeleme modeli
python src/cli.py train --input data.csv --type clustering --model kmeans --output model.json
```

### 4. İçgörü Oluşturma

```bash
# PCA analizi
python src/cli.py insight --input data.csv --type pca --output pca.json

# t-SNE görselleştirme
python src/cli.py insight --input data.csv --type tsne --output tsne.json

# Özellik önemliliği
python src/cli.py insight --input data.csv --type feature --output feature.json
```

### 5. Rapor Oluşturma

```bash
# PDF rapor
python src/cli.py report --input data.csv --type pdf --output report.pdf

# HTML rapor
python src/cli.py report --input data.csv --type html --output report.html

# CSV rapor
python src/cli.py report --input data.csv --type csv --output report.csv
```

### Yardım Alma

```bash
# Genel yardım
python src/cli.py --help

# Komut yardımı
python src/cli.py load --help
python src/cli.py analyze --help
python src/cli.py train --help
python src/cli.py insight --help
python src/cli.py report --help
```

## 🏗️ Proje Yapısı

```
template/
├── src/
│   ├── main.py              # Ana uygulama dosyası
│   ├── cli.py               # Komut satırı arayüzü
│   └── api/                 # API endpoint'leri
│       ├── __init__.py
│       ├── routes.py        # API rotaları
│       └── schemas.py       # API şemaları
├── utils/
│   ├── data_loader.py       # Veri yükleme modülü
│   ├── data_processor.py    # Veri işleme modülü
│   ├── data_analyzer.py     # Veri analizi modülü
│   ├── ml_model.py          # Makine öğrenmesi modülü
│   ├── ai_processor.py      # Yapay zeka işleme modülü
│   ├── report_generator.py  # Rapor oluşturma modülü
│   ├── error_handler.py     # Hata yönetimi modülü
│   └── visualization.py     # Görselleştirme yardımcıları
├── config/
│   ├── settings.py          # Ayarlar modülü
│   └── logging_config.py    # Loglama yapılandırması
├── data/                    # Veri dosyaları
│   ├── raw/                 # Ham veriler
│   ├── processed/           # İşlenmiş veriler
│   └── external/            # Harici veri kaynakları
├── models/                  # Eğitilmiş modeller
│   ├── saved/               # Kaydedilmiş model dosyaları
│   └── checkpoints/         # Model kontrol noktaları
├── reports/                 # Oluşturulan raporlar
│   ├── figures/             # Rapor figürleri
│   └── templates/           # Rapor şablonları
├── assets/                  # Statik dosyalar
│   ├── images/              # Görsel varlıklar
│   └── styles/              # CSS stilleri
├── tests/                   # Test dosyaları
│   ├── unit/                # Birim testleri
│   ├── integration/         # Entegrasyon testleri
│   └── fixtures/            # Test sabitleri
├── docs/                    # Dokümantasyon
│   ├── api/                 # API dokümantasyonu
│   └── guides/              # Kullanıcı kılavuzları
├── notebooks/               # Jupyter notebook'ları
├── requirements.txt         # Gereksinimler
├── requirements-dev.txt     # Geliştirme gereksinimleri
├── setup.py                 # Paket kurulumu
├── .env.example             # Örnek ortam değişkenleri
├── .gitignore               # Git ignore dosyası
├── LICENSE                  # Lisans dosyası
└── README.md                # Bu dosya
```

## 🔧 Geliştirme

### 1. Yeni Özellik Ekleme

1. İlgili modülü güncelleyin
2. Testler ekleyin
3. Dokümantasyonu güncelleyin

### 2. Hata Düzeltme

1. Hata raporunu inceleyin
2. Düzeltmeyi yapın
3. Testleri çalıştırın

### 3. Performans İyileştirme

1. Performans sorunlarını tespit edin
2. İyileştirmeleri yapın
3. Performans testlerini çalıştırın

## 🤝 Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

## 📞 İletişim

- Proje Sahibi: [Buğra Görmüş](mailto:bugra.gormus@hotmail.com)
- Proje Linki: [https://github.com/bugragormus/Data-Analysis-and-Machine-Learning-Template](https://github.com/bugragormus/Data-Analysis-and-Machine-Learning-Template)

## 🙏 Teşekkürler

Bu template'i kullandığınız için teşekkür ederiz! Herhangi bir sorunuz veya öneriniz varsa, lütfen iletişime geçmekten çekinmeyin.

## 🎯 Kullanım Alanları ve Örnekler

Bu template, aşağıdaki alanlarda ve amaçlarla kullanılabilir:

### 1. Finansal Analiz ve Tahmin

- **Borsa Verileri Analizi**

  ```python
  # Hisse senedi fiyat tahmini
  python src/cli.py train --input stock_data.csv --type regression --model random_forest --output stock_prediction.json

  # Finansal risk analizi
  python src/cli.py analyze --input financial_data.csv --type anomaly --output risk_analysis.json
  ```

- **Kredi Skorlama**
  ```python
  # Müşteri kredi riski değerlendirmesi
  python src/cli.py train --input customer_data.csv --type classification --model random_forest --output credit_score.json
  ```

### 2. Pazarlama ve Müşteri Analizi

- **Müşteri Segmentasyonu**

  ```python
  # Müşteri kümeleri oluşturma
  python src/cli.py train --input customer_data.csv --type clustering --model kmeans --output customer_segments.json

  # Müşteri davranış analizi
  python src/cli.py analyze --input customer_behavior.csv --type trend --output behavior_analysis.json
  ```

- **Marketing Campaign Optimization**
  ```python
  # Campaign Effectiveness Analysis
  python src/cli.py analyze --input campaign_data.csv --type stats --output campaign_analysis.json
  ```

### 3. Sağlık ve Biyoinformatik

- **Hastalık Teşhisi**

  ```python
  # Medikal veri analizi
  python src/cli.py train --input medical_data.csv --type classification --model random_forest --output diagnosis_model.json

  # Hasta risk analizi
  python src/cli.py analyze --input patient_data.csv --type anomaly --output risk_assessment.json
  ```

- **Genomik Veri Analizi**
  ```python
  # Gen ifadesi analizi
  python src/cli.py insight --input gene_expression.csv --type pca --output gene_analysis.json
  ```

### 4. Üretim ve Kalite Kontrol

- **Üretim Hattı Optimizasyonu**

  ```python
  # Üretim verimliliği analizi
  python src/cli.py analyze --input production_data.csv --type trend --output efficiency_analysis.json

  # Kalite kontrol tahmini
  python src/cli.py train --input quality_data.csv --type classification --model logistic_regression --output quality_prediction.json
  ```

- **Arıza Tespiti**
  ```python
  # Makine arıza tahmini
  python src/cli.py train --input machine_data.csv --type classification --model random_forest --output failure_prediction.json
  ```

### 5. Eğitim ve Araştırma

- **Öğrenci Başarı Analizi**

  ```python
  # Öğrenci performans tahmini
  python src/cli.py train --input student_data.csv --type regression --model linear_regression --output performance_prediction.json

  # Eğitim etkinliği analizi
  python src/cli.py analyze --input education_data.csv --type stats --output effectiveness_analysis.json
  ```

- **Araştırma Veri Analizi**
  ```python
  # Deneysel veri analizi
  python src/cli.py analyze --input experimental_data.csv --type corr --output experimental_analysis.json
  ```

### 6. Sosyal Medya ve İçerik Analizi

- **Duygu Analizi**
  ```python
  # Sosyal medya duygu analizi
  python src/cli.py train --input social_media_data.csv --type classification --model logistic_regression --output sentiment_analysis.json
  ```
- **İçerik Öneri Sistemi**
  ```python
  # Kullanıcı tercih analizi
  python src/cli.py insight --input user_preferences.csv --type tsne --output preference_analysis.json
  ```

### 7. Enerji ve Çevre

- **Enerji Tüketimi Tahmini**

  ```python
  # Enerji kullanım analizi
  python src/cli.py train --input energy_data.csv --type regression --model random_forest --output consumption_prediction.json

  # Çevresel veri analizi
  python src/cli.py analyze --input environmental_data.csv --type trend --output environmental_analysis.json
  ```

### 8. Retail and Supply Chain

- **Demand Prediction**

  ```python
  # Satış tahmini
  python src/cli.py train --input sales_data.csv --type regression --model linear_regression --output sales_prediction.json

  # Stok optimizasyonu
  python src/cli.py analyze --input inventory_data.csv --type anomaly --output inventory_analysis.json
  ```

### 9. Security and Fraud Detection

- **Anomali Tespiti**

  ```python
  # Dolandırıcılık tespiti
  python src/cli.py train --input transaction_data.csv --type classification --model random_forest --output fraud_detection.json

  # Güvenlik tehdidi analizi
  python src/cli.py analyze --input security_logs.csv --type anomaly --output threat_analysis.json
  ```

### 10. Otomotiv ve Ulaşım

- **Araç Bakım Tahmini**

  ```python
  # Araç arıza tahmini
  python src/cli.py train --input vehicle_data.csv --type classification --model random_forest --output maintenance_prediction.json

  # Trafik analizi
  python src/cli.py analyze --input traffic_data.csv --type trend --output traffic_analysis.json
  ```

### 11. Doğal Dil İşleme

- **Metin Sınıflandırma**

  ```python
  # Belge sınıflandırma
  python src/cli.py train --input text_data.csv --type classification --model random_forest --output text_classification.json

  # Duygu analizi
  python src/cli.py train --input sentiment_data.csv --type classification --model logistic_regression --output sentiment_analysis.json
  ```

- **Metin Üretimi**
  ```python
  # Metin üretimi analizi
  python src/cli.py insight --input text_data.csv --type pca --output text_analysis.json
  ```

### 12. Görüntü İşleme

- **Görüntü Sınıflandırma**

  ```python
  # Görüntü sınıflandırma
  python src/cli.py train --input image_data.csv --type classification --model random_forest --output image_classification.json

  # Nesne tespiti
  python src/cli.py analyze --input object_data.csv --type anomaly --output object_detection.json
  ```

### 13. Zaman Serisi Analizi

- **Tahmin**

  ```python
  # Zaman serisi tahmini
  python src/cli.py train --input time_series.csv --type regression --model random_forest --output forecasting.json

  # Mevsimsellik analizi
  python src/cli.py analyze --input seasonal_data.csv --type trend --output seasonality_analysis.json
  ```

### 14. IoT ve Sensör Veri Analizi

- **Sensör Veri İşleme**

  ```python
  # Sensör veri analizi
  python src/cli.py analyze --input sensor_data.csv --type anomaly --output sensor_analysis.json

  # Öngörülü bakım
  python src/cli.py train --input iot_data.csv --type classification --model random_forest --output maintenance_prediction.json
  ```

### 15. Blockchain ve Kripto Para Analizi

- **Kripto Para Fiyat Tahmini**

  ```python
  # Kripto fiyat analizi
  python src/cli.py analyze --input crypto_data.csv --type trend --output crypto_analysis.json

  # Blockchain işlem analizi
  python src/cli.py train --input blockchain_data.csv --type classification --model random_forest --output transaction_analysis.json
  ```

### 16. Artırılmış Gerçeklik ve Sanal Gerçeklik

- **AR/VR Veri Analizi**

  ```python
  # Kullanıcı etkileşim analizi
  python src/cli.py analyze --input ar_vr_data.csv --type stats --output interaction_analysis.json

  # Performans optimizasyonu
  python src/cli.py train --input performance_data.csv --type regression --model random_forest --output optimization.json
  ```

Each use case provides:

- Data loading and preprocessing
- Analysis and visualization
- Model training and evaluation
- Insight generation
- Report generation

features. The template allows you to quickly develop and deploy data science projects in these areas.

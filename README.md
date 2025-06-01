# What I've Built

A full-stack application that lets user add their business name and tries to find it using SerpAPI and return the details it could find with an AI analysis of it. Teh user can also enter the name of a competitor business and the API would fetch both business and run a comparison of both and score them, it will also show an AI based comaprison with instructions to improve the score.


### What you skipped and why

- Charts for visual comparison
Why? I prioratized the core features that show my skils in building a full stack system and AI integration, this feature was skipped due to time constraint.

- Style or tone toggles (e.g., “casual” vs “data-driven” suggestions)
Why? I initally decided to do it & thats why there is still an option on UI to choose but I figured that it would be better to implement this if I make agents for both and I decied to not do it in this time frame.

### What you'd improve with more time

With more time I'd mostly work on better error handling and taking care of edge cases. I'd improve AI suggestions and summarizations by creating agents specifically created for this use case. Work on the security of the system more.

### 🚀 How to run

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn
- OpenAI API Key ([Get it here](https://platform.openai.com/api-keys))
- SerpAPI Key ([Get it here](https://serpapi.com/dashboard))

### Environment Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd mobal.io
   ```

2. **Setup environment variables:**
   ```bash
   cd backend
   # Edit .env file and add your API keys:
   # OPENAI_API_KEY=your_actual_openai_api_key
   # SERPAPI_KEY=your_actual_serpapi_key
   # SECRET_KEY=your_django_secret_key
   ```

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Setup virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the backend server:**
   ```bash
   python manage.py runserver 8000
   ```

The Django API will be available at: `http://localhost:8000/api/`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend/mobal
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev -- --port 3000
   ```

The Vue.js app will be available at: `http://localhost:3000/`

## 📱 How to Use

1. **Open the frontend** at `http://localhost:3000/`
2. **Enter your business name, preferably with location** (e.g., "Burger King Joensuu")
3. **Optionally add competitors** or leave empty for analysis only
4. **Click "Start Analysis"** to get insights
5. **View the results** including:
   - Business profile score
   - Competitor comparison table
   - AI-generated suggestions

## 🔑 API Keys Required

For this application to work properly, you need:

1. **OpenAI API Key**: Used for AI-powered business analysis and suggestions
   - Get it from: https://platform.openai.com/api-keys
   - Add to `.env` as: `OPENAI_API_KEY=your_key_here`

2. **SerpAPI Key**: Used for fetching real business data from search results
   - Get it from: https://serpapi.com/dashboard
   - Add to `.env` as: `SERPAPI_KEY=your_key_here`

**Note**: The application includes fallback mechanisms if API keys are not provided, but full functionality requires both keys.

## 🎯 Project Overview

### What you skipped and why

- Charts for visual comparison
Why? I prioratized the core features that show my skils in building a full stack system and AI integration, this feature was skipped due to time constraint.

- Style or tone toggles (e.g., "casual" vs "data-driven" suggestions)
Why? I initally decided to do it & thats why there is still an option on UI to choose but I figured that it would be better to implement this if I make agents for both and I decied to not do it in this time frame.

### What you'd improve with more time

With more time I'd mostly work on better error handling and taking care of edge cases. I'd improve AI suggestions and summarizations by creating agents specifically created for this use case. Work on the security of the system more.

## 🏗️ Architecture

### Backend (Django)
```
backend/
├── comparator/
│   ├── models.py              # BusinessProfile model
│   ├── views.py               # 3 core API endpoints  
│   ├── services.py            # Business analysis logic wrapper
│   ├── services/              # Detailed service implementations
│   │   ├── __init__.py
│   │   ├── ai_service.py      # AI-powered analysis
│   │   ├── business_analysis_service.py
│   │   ├── business_service.py    # Core business logic
│   │   ├── comparison_service.py  # Business comparison logic
│   │   ├── config.py          # Configuration settings
│   │   ├── scoring_service.py # Business scoring algorithms
│   │   └── serpapi_service.py # Search API integration
│   ├── urls.py                # API routing
│   ├── admin.py               # Django admin
│   ├── apps.py                # App configuration
│   └── migrations/            # Database migrations
├── competitor_insights/       # Django project settings
│   ├── __init__.py
│   ├── settings.py           # Project configuration
│   ├── urls.py               # Main URL routing
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── test_api.py               # API test script
├── requirements.txt          # Python dependencies
├── manage.py                 # Django management
└── db.sqlite3               # SQLite database
```

### Frontend (Vue.js)
```
frontend/mobal/
├── src/
│   ├── views/
│   │   ├── Home.vue          # Main input form
│   │   └── Results.vue       # Results dashboard
│   ├── components/
│   │   ├── analysis/         # Analysis-related components
│   │   ├── business/         # Business profile components
│   │   ├── comparison/       # Comparison components
│   │   ├── forms/            # Form components
│   │   ├── layout/           # Layout components
│   │   └── ui/               # Reusable UI components
│   ├── services/
│   │   └── api.js            # API service layer
│   ├── stores/               # Pinia state management
│   ├── router/               # Vue Router configuration
│   ├── composables/          # Vue composables
│   ├── utils/                # Utility functions
│   ├── constants/            # Application constants
│   ├── main.js               # Application entry point
│   ├── App.vue               # Root component
│   └── index.css             # Global styles
```

## 🔌 API Endpoints

### 1. Business Analysis
```http
POST /api/analyze/
{
    "business_name": "My Restaurant",
    "website": "https://myrestaurant.com" // optional
}
```

### 3. Compare Businesses
```http
POST /api/compare/
{
    "your_business": "My Restaurant",
    "competitor_business": "Luigi's Kitchen"
}
```

## 🧪 Testing

### Backend Testing
```bash
cd backend
source venv/bin/activate
python test_api.py
```

### Manual API Testing
```bash
# Test business analysis
curl -X POST http://localhost:8000/api/analyze/ \
     -H "Content-Type: application/json" \
     -d '{"business_name": "Burger King Joensuu"}'


# Test business comparison
curl -X POST http://localhost:8000/api/compare/ \
     -H "Content-Type: application/json" \
     -d '{"your_business": "Burger King Joensuu", "competitor_business": "Subway Joensuu"}'
```



## 📱 How to Use

1. **Open the frontend** at `http://localhost:3000/`
2. **Enter your business namem, preferably with location** (e.g., "Burger King Joensuu")
3. **Optionally add competitors** or leave empty for analysis only
4. **Click "Start Analysis"** to get insights
5. **View the results** including:
   - Business profile score
   - Competitor comparison table
   - AI-generated suggestions



# Geaux Academy

Geaux Academy is an interactive learning platform built with React, TypeScript, Firebase, and FastAPI. This project aims to provide a seamless learning experience through various features and functionalities.

## Features

- User authentication and profile management
- Learning style assessment and personalized content
- Interactive UI components
- API integration for data handling
- Comprehensive testing for reliability

## Getting Started

To get a local copy up and running, follow these steps:

### Prerequisites

- Node.js (version 14 or higher)
- Python (version 3.7 or higher)
- Firebase account for authentication and database

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/geaux-academy.git
   ```
2. Navigate to the project directory:
   ```bash
   cd geaux-academy
   ```
3. Install the frontend dependencies:
   ```bash
   cd src
   npm install
   ```
4. Set up the backend:
   - Navigate to the backend directory:
     ```bash
     cd ../backend
     ```
   - Install the backend dependencies (needed for both local runs and CI):
     ```bash
     pip install -r requirements.txt
     ```
   - Configure environment variables for JWT authentication. Create a `.env` file in `backend/` (or set the variables in your shell) with:
    ```bash
      SECRET_KEY="your_secret_key"          # Required: non-empty string used to sign JWTs
      ALGORITHM="HS256"                     # Optional: JWT signing algorithm (default: HS256)
      ACCESS_TOKEN_EXPIRE_MINUTES=30         # Optional: positive integer token lifetime in minutes (default: 30)
      ```

### Running the Application

1. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```
2. Start the frontend application:
   ```bash
   cd ../src
   npm start
   ```

## Usage

- Access the application in your browser at `http://localhost:3000`.
- Use the authentication features to log in or create a new account.
- Explore the learning materials and track your progress.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
# FoodSnap AI - Web Application

🎉 **Welcome to FoodSnap AI!** 🎉

FoodSnap AI is a web application designed to help users estimate the nutritional content of food items by simply uploading an image. The app utilizes advanced AI models to identify food items and fetches nutritional information from reliable databases.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
5. [API Keys](#api-keys)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [License](#license)

---

## Project Overview

**Project Name:** FoodSnap AI

FoodSnap AI allows users to upload images of food, which are then processed to identify the food items and retrieve their nutritional information. The application is designed to be user-friendly and responsive, making it accessible on various devices.

## Features

- Upload food images and display a preview.
- Identify food items using the Clarifai Food model API.
- Fetch nutritional information (calories, macronutrients) from the Spoonacular API.
- Display results in a styled card section.
- Basic error handling and loading spinner for better user experience.

## Technologies Used

- HTML
- CSS
- JavaScript
- Clarifai API
- Spoonacular API

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/YOUR_USERNAME/foodsnap-ai.git
   cd foodsnap-ai
   ```

2. Open `index.html` in your web browser to view the application.

## API Keys

To use the Clarifai and Spoonacular APIs, you will need to sign up for their services and obtain API keys. Replace the placeholders in the `script.js` file with your actual API keys.

```javascript
const CLARIFAI_API_KEY = 'YOUR_CLARIFAI_API_KEY';
const SPOONACULAR_API_KEY = 'YOUR_SPOONACULAR_API_KEY';
```

## Usage

1. Open the application in your web browser.
2. Click on the file input to upload a food image.
3. Wait for the image to be processed and the nutritional information to be displayed.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Thank you for checking out FoodSnap AI! We hope you find it useful and enjoyable. Happy food snapping!
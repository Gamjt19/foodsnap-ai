// assets/js/script.js

const imageInput = document.getElementById('imageInput');
const previewContainer = document.getElementById('previewContainer');
const resultContainer = document.getElementById('resultContainer');
const loadingSpinner = document.getElementById('loadingSpinner');
const clarifaiApiKey = 'a4c1cbca59074e3da79337cb43314c26'; // Replace with your Clarifai API key
const spoonacularApiKey = 'YOUR_SPOONACULAR_API_KEY'; // Replace with your Spoonacular API key

imageInput.addEventListener('change', handleImageUpload);

function handleImageUpload(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            displayImagePreview(e.target.result);
            identifyFood(e.target.result);
        };
        reader.readAsDataURL(file);
    }
}

function displayImagePreview(imageSrc) {
    previewContainer.innerHTML = `<img src="${imageSrc}" alt="Food Image" class="preview-image" />`;
}

function identifyFood(imageSrc) {
    loadingSpinner.style.display = 'block';
    fetch('https://api.clarifai.com/v2/models/food-image-recognition/outputs', {
        method: 'POST',
        headers: {
            'Authorization': `Key ${clarifaiApiKey}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            inputs: [
                {
                    data: {
                        image: {
                            base64: imageSrc.split(',')[1]
                        }
                    }
                }
            ]
        })
    })
    .then(response => response.json())
    .then(data => {
        const foodItem = data.outputs[0].data.concepts[0].name;
        fetchNutritionalInfo(foodItem);
    })
    .catch(error => {
        console.error('Error identifying food:', error);
        loadingSpinner.style.display = 'none';
        resultContainer.innerHTML = '<p>Error identifying food. Please try again.</p>';
    });
}

function fetchNutritionalInfo(foodItem) {
    fetch(`https://api.spoonacular.com/food/ingredients/${foodItem}/information?apiKey=${spoonacularApiKey}`)
    .then(response => response.json())
    .then(data => {
        displayNutritionalInfo(data);
    })
    .catch(error => {
        console.error('Error fetching nutritional info:', error);
        loadingSpinner.style.display = 'none';
        resultContainer.innerHTML = '<p>Error fetching nutritional information. Please try again.</p>';
    });
}

function displayNutritionalInfo(data) {
    loadingSpinner.style.display = 'none';
    resultContainer.innerHTML = `
        <div class="result-card">
            <h2>${data.name}</h2>
            <p>Calories: ${data.nutrition.nutrients[0].amount} kcal</p>
            <p>Protein: ${data.nutrition.nutrients[1].amount} g</p>
            <p>Carbohydrates: ${data.nutrition.nutrients[3].amount} g</p>
            <p>Fats: ${data.nutrition.nutrients[2].amount} g</p>
        </div>
    `;
}
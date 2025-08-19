// Get the class grid and search input elements
const classGrid = document.querySelector('.class-grid');
const searchInput = document.getElementById('search-input');
const searchBtn = document.getElementById('search-btn');

// Define the classes array
const classes = [
    {
        name: 'GMM-Pro',
        description: 'Google,Microsoft,Meta Full Preparation',
        price:5999,
        image: '72d24e4d-e3b7-4613-b5ee-061f7af2e00a.jpg'
    },
    {
        name: 'A-Pro',
        description: 'wipro,Congnigent,Amazone,Flipcart Full Preparation',
        price: 6499,
        image: 'https://source.unsplash.com/300x200/?html'
    },
    {
        name: 'Tcs-Pro',
        description: 'Tcs,Dlettoi,etc Full Preparation',
        price: 5999,
        image: 'https://source.unsplash.com/300x200/?react'
    },
    {
        name: 'Fullstack Devolopment',
        description: 'Full Stack Dev. With sql',
        price: 3999,
        image: 'https://source.unsplash.com/300x200/?nodejs'
    },
    {
        name: 'Python Class',
        description: 'Learn Python basics to Avd.(class 8-12,bigenner)',
        price: 999,
        image: 'https://source.unsplash.com/300x200/?python'
    },
];

// Function to generate class cards
function generateClassCards(classes) {
    classGrid.innerHTML = '';
    classes.forEach((cls) => {
        const classCard = document.createElement('div');
        classCard.classList.add('class-card');
        classCard.innerHTML = `
            <img src="${cls.image}" alt="${cls.name}">
            <h2>${cls.name}</h2>
            <p>${cls.description}</p>
            <p>Price: ${cls.price}</p>
            <button class="explore-btn">Explore</button>
            <button class="buy-now-btn">Buy Now</button>
        `;
        classGrid.appendChild(classCard);
    });
}


// Generate class cards on page load
generateClassCards(classes);

// Add event listener to search button
searchBtn.addEventListener('click', () => {
    const searchTerm = searchInput.value.toLowerCase();
    const filteredClasses = classes.filter((cls) => cls.name.toLowerCase().includes(searchTerm));
    generateClassCards(filteredClasses);
});

// Add event listener to search input
searchInput.addEventListener('input', () => {
    const searchTerm = searchInput.value.toLowerCase();
    const filteredClasses = classes.filter((cls) => cls.name.toLowerCase().includes(searchTerm));
    generateClassCards(filteredClasses);
});

// banner scroll
const bannerSlides = document.querySelectorAll('.banner-slide');
let currentSlide = 0;

function showNextSlide() {
    bannerSlides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % bannerSlides.length;
    bannerSlides[currentSlide].classList.add('active');
}

setInterval(showNextSlide, 3000);


// explore category

// Add event listener to explore category
document.querySelectorAll('.explore-category').forEach((element) => {
    element.addEventListener('click', () => {
        // Add your logic here
        console.log('Explore category clicked');
    });
});

// explore boutton

// Function to generate class cards
function generateClassCards(classes) {
    classGrid.innerHTML = '';
    classes.forEach((cls) => {
        const classCard = document.createElement('div');
        classCard.classList.add('class-card');
        classCard.innerHTML = `
            <img src="${cls.image}" alt="${cls.name}">
            <h2>${cls.name}</h2>
            <p>${cls.description}</p>
            <p>Price: ${cls.price}</p>
            <button class="explore-btn">Explore</button>
            <button class="buy-now-btn">Buy Now</button>
        `;
        classGrid.appendChild(classCard);

        // Add event listener to explore button
        const exploreBtn = classCard.querySelector('.explore-btn');
        exploreBtn.addEventListener('click', () => {
            displayClassDetails(cls);
        });
    });
}
// Function to display class details
function displayClassDetails(cls) {
    const modal = document.createElement('div');
    modal.className = 'modal';
    modal.innerHTML = `
        <img src="${cls.image}" alt="${cls.name}">
        <h2>${cls.name}</h2>
        <p>${cls.description}</p>
        <p>Price: ${cls.price}</p>
        <div class="modal-buttons">
            <button class="buy-now-btn">Buy Now</button>
            <button class="close-modal">Close</button>
        </div>
    `;

    // Add event listener to close the modal
    modal.querySelector('.close-modal').addEventListener('click', () => {
        modal.remove();
    });

    // Add event listener to buy now button
    modal.querySelector('.buy-now-btn').addEventListener('click', () => {
        buyClass(cls);
        modal.remove();
    });

    // Add the modal to the page
    document.body.appendChild(modal);
}

// Function to buy class
function buyClass(cls) {
    // Add logic to handle the purchase
    alert(`You have purchased ${cls.name} for $${cls.price}`);
}

// 3 dot
const menuBtn = document.querySelector('.menu-btn');
const menuOptions = document.querySelector('.menu-options');

menuBtn.addEventListener('click', () => {
    menuOptions.style.display = menuOptions.style.display === 'block' ? 'none' : 'block';
});

document.addEventListener('click', (e) => {
    if (!e.target.closest('.menu-dot')) {
        menuOptions.style.display = 'none';
    }
});

const nightModeBtn = document.getElementById('night-mode-btn');
let isNightMode = false;

nightModeBtn.addEventListener('click', () => {
    document.body.classList.toggle('night-mode');
    isNightMode = !isNightMode;
});
nightModeBtn.addEventListener('click', () => {
    if (!isNightMode) {
        document.body.style.backgroundColor = '#313131ff';
        document.body.style.color = '#fff';
        isNightMode = true;
    } else {
        document.body.style.backgroundColor = '';
        document.body.style.color = '';
        isNightMode = false;
    }
});

const exitBtn = document.getElementById('exit-btn');

exitBtn.addEventListener('click', () => {
    if (confirm('Are you sure you want to exit?')) {
        window.close();
    }
});


// see


const categoryCards = document.querySelectorAll('.category-card');
const seeAllBtn = document.querySelector('.see-all-categories button');

// Calculate the number of cards to show initially
const initialCards = 4;

// Hide all category cards except the initial cards
for (let i = initialCards; i < categoryCards.length; i++) {
    categoryCards[i].style.display = 'none';
}

// Add event listener to the "See All" button
let seeAll = true;
seeAllBtn.addEventListener('click', () => {
    if (seeAll) {
        // Show all category cards
        for (let i = 0; i < categoryCards.length; i++) {
            categoryCards[i].style.display = 'flex';
        }
        seeAllBtn.textContent = 'View less ';
        seeAll = false;
    } else {
        // Hide all category cards except the initial cards
        for (let i = initialCards; i < categoryCards.length; i++) {
            categoryCards[i].style.display = 'none';
        }
        seeAllBtn.textContent = 'View All Categories(2)';
        seeAll = true;
    }
});

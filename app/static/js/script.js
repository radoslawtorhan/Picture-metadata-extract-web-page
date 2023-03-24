const rotateLeftButton = document.querySelector('.rotate-button-left');
const rotateRightButton = document.querySelector('.rotate-button-right');
const imageElement = document.querySelector('.image');

let rotation = 0;

rotateLeftButton.addEventListener('click', () => {
    rotation -= 90;
    imageElement.style.transform = `rotate(${rotation}deg)`;
    console.log('Left button clicked');
});

rotateRightButton.addEventListener('click', () => {
    rotation += 90;
    imageElement.style.transform = `rotate(${rotation}deg)`;
    console.log('Right button clicked');
});

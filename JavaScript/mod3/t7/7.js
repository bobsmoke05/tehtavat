const triggerElement = document.getElementById('trigger');
const targetImage = document.getElementById('target');

const handleMouseOver = () => {
    targetImage.src = 'picB.jpg';
};

const handleMouseOut = () => {
    targetImage.src = 'picA.jpg';
};

triggerElement.addEventListener('mouseover', handleMouseOver);
triggerElement.addEventListener('mouseout', handleMouseOut);
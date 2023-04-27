"TheWelcomeBaner" - script for a slideshow component. The component displays a set of slides with images and names of video games. The data for the slides are stored in an array called slides, which contains objects with properties name (the name of the game) and url (the URL of the image for the slide).

Methods:
- nextSlide(), prevSlide(), and autoChangeSlide(). nextSlide() and prevSlide(): update the activeIndex variable to show the next or previous slide, respectively. 
- autoChangeSlide(): called at an interval of 5000ms (5 seconds) and automatically changes the slide to the next one by calling nextSlide().
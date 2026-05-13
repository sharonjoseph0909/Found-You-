const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

recognition.onstart = () => {
    console.log('Voice recognition started. Try speaking into the microphone.');
};

recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    console.log('You said: ', transcript);
    // You can add code here to handle the transcript, such as displaying it on the page or using it for a search query.
};

// Start voice recognition when the microphone button is clicked
function startVoiceRecognition() {
    recognition.start();
}
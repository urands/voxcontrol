let recognition;

export function startRecognition(commandHandler) {
  recognition = new webkitSpeechRecognition();
  recognition.continuous = true;
  recognition.lang = 'ru-RU';
  console.log('startRecognition');
  recognition.onresult = function (event) {
    const last = event.results.length - 1;
    const command = event.results[last][0].transcript;
    console.log('Recognized:', command);
    console.log('event:', event);
    commandHandler(command);
  };

  recognition.start();
}

export function stopRecognition() {
  if (recognition) {
    recognition.stop();
  }
}

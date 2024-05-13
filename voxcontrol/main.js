import { startRecognition, stopRecognition } from './speechapi.js';
import { commandHandler } from './commands.js';
import { getDOMStructure } from './structure.js';
import { sendDOMStructure } from './api.js';
import { processingCommand } from './processing.js';

document.querySelector('#app').innerHTML = `
  <div>
    <button id="start-btn">Start VoxControl</button>
    <button id="stop-btn">Stop VoxControl</button>
  </div>
`;

document
  .getElementById('start-btn')
  .addEventListener('click', startRecognition(commandHandler));
document.getElementById('stop-btn').addEventListener('click', stopRecognition);

// Получаем структуру DOM в виде JSON
document.addEventListener('DOMContentLoaded', function () {
  const domStructureJSON = JSON.stringify(
    getDOMStructure(document.documentElement),
    null,
    2
  );
  console.log(domStructureJSON);
  sendDOMStructure(domStructureJSON);
});

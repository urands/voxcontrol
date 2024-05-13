import { processingCommand } from './processing';

let sessionId = null;

export function sendDOMStructure(domStructure) {
  // Преобразуем JSON объект в строку
  const json = JSON.stringify(domStructure);

  const url = (import.meta.env.VITE_BE_URL || '') + '/api/v1/structure';

  // Настраиваем параметры запроса
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: json,
  };

  // Отправляем запрос
  fetch(url, requestOptions)
    .then(async (response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      console.log('DOM structure sent successfully!');
      const resp = await response.json();
      sessionId = resp.sessionId;
    })
    .then((data) => console.log(data))
    .catch((error) =>
      console.error('There was a problem with your fetch operation:', error)
    );
}

export function sendRecognize(text) {
  // Преобразуем JSON объект в строку
  const json = JSON.stringify({
    text: text,
    sessionId: sessionId,
  });
  const url = (import.meta.env.VITE_BE_URL || '') + '/api/v1/recognition';

  // Настраиваем параметры запроса
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: json,
  };

  // Отправляем запрос
  fetch(url, requestOptions)
    .then(async (response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      console.log('DOM structure sent successfully!');
      const resp = await response.json();
      console.log('Action:', resp);
      resp.forEach((e) => {
        processingCommand(e);
      });
    })
    .then((data) => {})
    .catch((error) =>
      console.error('There was a problem with your fetch operation:', error)
    );
}

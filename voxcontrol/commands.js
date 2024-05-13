import { sendRecognize } from './api';

export function commandHandler(command) {
  console.log('COmand:', command);

  sendRecognize(command);
}

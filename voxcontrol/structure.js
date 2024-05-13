function getAttributes(node) {
  const ariaAttributes = {};
  const attributes = node.attributes;
  for (let i = 0; i < attributes.length; i++) {
    const attributeName = attributes[i].nodeName;
    if (attributeName.startsWith('aria-')) {
      ariaAttributes[attributeName] = node.getAttribute(attributeName);
    }
    if (attributeName == 'id') {
      ariaAttributes[attributeName] = node.getAttribute(attributeName);
    }
  }
  return ariaAttributes;
}

function getButtonLabels(node) {
  const buttonLabels = [];
  if (
    node.tagName.toLowerCase() === 'button' ||
    (node.tagName.toLowerCase() === 'input' && node.type === 'button')
  ) {
    buttonLabels.push(node.textContent.trim());
  }
  return buttonLabels;
}

function getInputLabels(node) {
  const inputLabels = [];
  if (node.tagName.toLowerCase() === 'label' && node.htmlFor) {
    const targetInput = document.getElementById(node.htmlFor);
    if (targetInput) {
      inputLabels.push(targetInput.value || targetInput.placeholder);
    }
  }
  return inputLabels;
}

function getSelector(node) {
  let selector = '';

  // Получаем селекторы родительских элементов
  const parents = [];
  let parent = node.parentElement;
  while (parent) {
    let parentSelector = parent.tagName.toLowerCase();
    if (parent.id) {
      parentSelector += `#${parent.id}`;
      parents.unshift(parentSelector); // Добавляем селекторы родительских элементов в начало массива
      break; // Прерываем цикл, если у родительского элемента есть id
    } else if (parent.classList.length > 0) {
      parentSelector += `.${parent.classList[0]}`;
    }
    parents.unshift(parentSelector); // Добавляем селекторы родительских элементов в начало массива
    parent = parent.parentElement;
  }

  // Объединяем селекторы родительских элементов с селектором текущего элемента
  selector = parents.join(' > ') + ' ' + node.tagName.toLowerCase();
  let elID = undefined;
  const attributes = node.attributes;
  for (let i = 0; i < attributes.length; i++) {
    const attributeName = attributes[i].nodeName;
    if (attributeName == 'id') {
      elID = node.getAttribute(attributeName);
      break;
    }
  }
  console.log(elID);
  if (elID) selector += '#' + elID;

  console.log(selector);

  return selector;
}

// Функция для преобразования структуры DOM в JSON
export function getDOMStructure(node) {
  const obj = {};

  // Добавляем информацию о текущем узле
  obj.tagName = node.tagName;
  obj.selector = getSelector(node);
  obj.textContent = node.textContent.trim();
  obj.buttonLabels = getButtonLabels(node);
  obj.inputLabels = getInputLabels(node);
  obj.text = node.text;
  obj.attributes = getAttributes(node);
  obj.children = [];

  // Рекурсивно обходим всех дочерних узлов
  for (let i = 0; i < node.children.length; i++) {
    obj.children.push(getDOMStructure(node.children[i]));
  }

  return obj;
}
